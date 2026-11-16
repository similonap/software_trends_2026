export default function TaakItem({ taak, onWissel }) {
  return (
    <li>
      <label>
        <input type="checkbox" checked={taak.klaar} onChange={() => onWissel(taak.id)} /> {taak.titel}
      </label>
    </li>
  )
}
