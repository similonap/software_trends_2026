// Oplossing opdracht 1.4
// - Geen globale teller meer die tijdens het renderen verhoogd wordt (side effect, niet puur).
// - De props worden niet meer aangepast (immutability).
// open.sort(...) mocht eigenlijk wel: filter() maakt een nieuwe, lokale array.
// toSorted() maakt de bedoeling wel duidelijker: altijd een kopie.
export default function Statistiek({ taken }) {
  const open = taken.filter((t) => !t.klaar)
  const nieuwste = open.toSorted((a, b) => b.id - a.id)[0]

  return (
    <p className="statistiek">
      {open.length} van de {taken.length} taken staan nog open. Nieuwste open taak: {nieuwste?.titel}.
    </p>
  )
}
