// Een nep-database: een JSON-bestand in de map data/ (wordt aangemaakt bij de eerste wijziging).
// Opnieuw beginnen? Verwijder data/boeken.json én de map .next (daar zit de cache van Next.js).
import { mkdir, readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'

export type Boek = { id: number; titel: string; auteur: string }

const BESTAND = path.join(process.cwd(), 'data', 'boeken.json')
const STARTDATA: Boek[] = [
  { id: 1, titel: 'Clean Code', auteur: 'Robert C. Martin' },
  { id: 2, titel: 'The Pragmatic Programmer', auteur: 'Andrew Hunt en David Thomas' },
  { id: 3, titel: 'Refactoring', auteur: 'Martin Fowler' },
]

async function lees(): Promise<Boek[]> {
  try {
    return JSON.parse(await readFile(BESTAND, 'utf8'))
  } catch {
    return structuredClone(STARTDATA)
  }
}

async function schrijf(boeken: Boek[]) {
  await mkdir(path.dirname(BESTAND), { recursive: true })
  await writeFile(BESTAND, JSON.stringify(boeken, null, 2))
}

const wacht = (ms: number) => new Promise((klaar) => setTimeout(klaar, ms))

export async function haalBoekenOp(): Promise<Boek[]> {
  await wacht(1500) // een trage query
  console.log(`[db] boeken opgehaald om ${new Date().toLocaleTimeString('nl-BE')}`)
  return lees()
}

export async function bewaarBoek(titel: string, auteur: string) {
  await wacht(200)
  const boeken = await lees()
  const id = Math.max(0, ...boeken.map((b) => b.id)) + 1
  await schrijf([...boeken, { id, titel, auteur }])
}

export async function wisBoek(id: number) {
  await schrijf((await lees()).filter((b) => b.id !== id))
}
