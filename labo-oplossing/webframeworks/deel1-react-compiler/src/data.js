// Testdata: 3000 taken.
export function maakTaken(aantal) {
  return Array.from({ length: aantal }, (_, i) => ({
    id: i + 1,
    titel: `Taak ${i + 1}`,
    klaar: i % 3 === 0,
  }))
}

// Een bewust trage filter: zo zie je in het meetpaneel duidelijk hoeveel werk een render kost.
export function traagFilter(taken, filter) {
  const einde = performance.now() + 15
  while (performance.now() < einde) {
    // 15 ms "rekenwerk"
  }
  if (filter === 'open') return taken.filter((t) => !t.klaar)
  if (filter === 'klaar') return taken.filter((t) => t.klaar)
  return taken
}
