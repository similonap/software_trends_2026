import { memo } from 'react'

// memo: sla de render over als taak en onWissel dezelfde referentie hebben als vorige keer
const TaakItem = memo(function TaakItem({ taak, onWissel }) {
  return (
    <li>
      <label>
        <input type="checkbox" checked={taak.klaar} onChange={() => onWissel(taak.id)} /> {taak.titel}
      </label>
    </li>
  )
})

export default TaakItem
