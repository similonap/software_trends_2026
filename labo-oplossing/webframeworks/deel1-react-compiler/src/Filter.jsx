const KEUZES = ['alle', 'open', 'klaar']

export default function Filter({ waarde, onKies }) {
  return (
    <div role="group" aria-label="Filter">
      {KEUZES.map((k) => (
        <button key={k} aria-pressed={k === waarde} onClick={() => onKies(k)}>
          {k}
        </button>
      ))}
    </div>
  )
}
