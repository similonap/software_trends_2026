// Opdracht 1.4: dit component breekt Rules of React. Welke?
let keerGetoond = 0

export default function Statistiek({ taken }) {
  keerGetoond++
  const open = taken.filter((t) => !t.klaar)
  const nieuwste = open.sort((a, b) => b.id - a.id)[0]
  taken.laatsteTelling = open.length

  return (
    <p className="statistiek">
      {open.length} van de {taken.length} taken staan nog open. Nieuwste open taak: {nieuwste?.titel}.
      <br />
      <small>Dit blok werd al {keerGetoond} keer getoond.</small>
    </p>
  )
}
