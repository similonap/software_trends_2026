import { traagFilter } from './data.js'
import TaakItem from './TaakItem.jsx'

export default function TakenLijst({ taken, filter, onWissel }) {
  const zichtbaar = traagFilter(taken, filter)
  return (
    <>
      <p>{zichtbaar.length} taken</p>
      <ul>
        {zichtbaar.map((taak) => (
          <TaakItem key={taak.id} taak={taak} onWissel={onWissel} />
        ))}
      </ul>
    </>
  )
}
