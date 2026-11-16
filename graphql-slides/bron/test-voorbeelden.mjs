import { buildSchema, graphql, parse, validate, experimentalExecuteIncrementally, version } from 'graphql';
import DataLoader from 'dataloader';
console.log('graphql-js', version);

// ---------- schema zoals op de slides ----------
const sdl = /* GraphQL */ `
  type Person {
    id: ID!
    name: String!
    age: Int!
    posts: [Post!]!
    followers(first: Int): [Person!]!
  }
  type Post {
    id: ID!
    title: String!
    author: Person!
  }
  input PersonLookup @oneOf {
    id: ID
    name: String
  }
  type Query {
    allPersons(last: Int): [Person!]!
    allPosts(last: Int): [Post!]!
    person(by: PersonLookup!): Person
  }
  type Mutation {
    createPerson(name: String!, age: Int!): Person!
    updatePerson(id: ID!, name: String, age: Int): Person!
    deletePerson(id: ID!): Person!
  }
  type Subscription {
    newPerson: Person!
  }
`;
const schema = buildSchema(sdl);

// ---------- data + resolvers (met teller voor N+1) ----------
const persons = [
  { id: '1', name: 'Johnny', age: 23 }, { id: '2', name: 'Sarah', age: 20 }, { id: '3', name: 'Alice', age: 20 },
];
const posts = [
  { id: 'p1', title: 'GraphQL is awesome', authorId: '1' },
  { id: 'p2', title: 'Relay is a powerful GraphQL Client', authorId: '1' },
  { id: 'p3', title: 'How to get started with React & GraphQL', authorId: '2' },
];
let dbCalls = 0;
const db = {
  personById: async (id) => { dbCalls++; return persons.find(p => p.id === id); },
  personsByIds: async (ids) => { dbCalls++; return persons.filter(p => ids.includes(p.id)); },
};

function makeRoot(useLoader) {
  const personLoader = new DataLoader(async (ids) => {
    const rows = await db.personsByIds(ids);
    return ids.map(id => rows.find(p => p.id === id));
  });
  const wrapPerson = (p) => p && ({
    ...p,
    posts: () => posts.filter(x => x.authorId === p.id).map(wrapPost),
    followers: ({ first }) => persons.filter(x => x.id !== p.id).slice(0, first ?? 10).map(wrapPerson),
  });
  const wrapPost = (x) => ({
    ...x,
    author: async () => wrapPerson(useLoader ? await personLoader.load(x.authorId) : await db.personById(x.authorId)),
  });
  return {
    allPersons: ({ last }) => (last ? persons.slice(-last) : persons).map(wrapPerson),
    allPosts: () => posts.map(wrapPost),
    person: ({ by }) => wrapPerson(persons.find(p => (by.id ? p.id === by.id : p.name === by.name))),
    createPerson: ({ name, age }) => { const p = { id: String(persons.length + 1), name, age }; persons.push(p); return wrapPerson(p); },
  };
}

async function run(label, source, variableValues, useLoader = true) {
  dbCalls = 0;
  const r = await graphql({ schema, source, rootValue: makeRoot(useLoader), variableValues });
  console.log(`\n## ${label}  (db-calls: ${dbCalls})`);
  console.log(JSON.stringify(r));
  if (r.errors) process.exitCode = 1;
  return r;
}

await run('names', `{ allPersons { name } }`);
await run('names+age', `{ allPersons { name age } }`);
await run('last 2', `{ allPersons(last: 2) { name age } }`);
await run('nested', `{ allPersons { name posts { title } } }`);
await run('mutation', `mutation { createPerson(name: "Bob", age: 36) { id name age } }`);
await run('variables+fragment+alias', `
  query PersonCard($id: ID!) {
    eerste: person(by: { id: $id }) { ...PersonInfo }
    tweede: person(by: { name: "Sarah" }) { ...PersonInfo }
  }
  fragment PersonInfo on Person { name age }`, { id: '1' });
await run('N+1 zonder DataLoader', `{ allPosts { title author { name } } }`, undefined, false);
await run('N+1 met DataLoader', `{ allPosts { title author { name } } }`, undefined, true);
await run('followers', `query { person(by: { id: "1" }) { name followers(first: 5) { name age } } }`);

// oneOf moet falen bij twee velden
const bad = validate(schema, parse(`{ person(by: { id: "1", name: "Sarah" }) { name } }`));
const badExec = await graphql({ schema, source: `{ person(by: { id: "1", name: "Sarah" }) { name } }`, rootValue: makeRoot(true) });
console.log('\n## oneOf met 2 velden:', bad.map(e => e.message), badExec.errors?.map(e => e.message));

// verkeerde type (de fout van vroeger): age als String
const wrongType = validate(schema, parse(`mutation { createPerson(name: "Bob", age: "36") { id } }`));
console.log('\n## age als String:', wrongType.map(e => e.message));

// onbestaand veld → validatiefout (relevant voor agents)
const typo = validate(schema, parse(`{ allPersons { nam } }`));
console.log('\n## typo:', typo.map(e => e.message));

// introspectie
const intro = await graphql({ schema, source: `{ __type(name: "Person") { name fields { name type { kind name ofType { name } } } } }` });
console.log('\n## introspectie:', JSON.stringify(intro.data.__type.fields.map(f => f.name)));

// @defer (experimenteel in v17)
const deferSchema = buildSchema(sdl + '\ndirective @defer(if: Boolean! = true, label: String) on FRAGMENT_SPREAD | INLINE_FRAGMENT\n');
const res = await experimentalExecuteIncrementally({
  schema: deferSchema,
  document: parse(`{ allPersons(last: 1) { name ... @defer { posts { title } } } }`),
  rootValue: makeRoot(true),
});
if ('initialResult' in res) {
  console.log('\n## defer initial:', JSON.stringify(res.initialResult));
  for await (const sub of res.subsequentResults) console.log('## defer later:', JSON.stringify(sub));
} else console.log('\n## defer: geen incrementeel resultaat', JSON.stringify(res));
