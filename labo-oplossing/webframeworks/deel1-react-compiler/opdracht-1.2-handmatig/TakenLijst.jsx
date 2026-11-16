import { memo, useMemo } from 'react'
import { traagFilter } from './data.js'
import TaakItem from './TaakItem.jsx'

const TakenLijst = memo(function TakenLijst({ taken, filter, onWissel }) {
  // useMemo: de trage filter loopt enkel opnieuw als taken of filter veranderen
  const zichtbaar = useMemo(() => traagFilter(taken, filter), [taken, filter])
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
})

export default TakenLijst
