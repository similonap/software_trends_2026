import { Profiler, useState } from 'react'
import { maakTaken } from './data.js'
import { meet } from './meting.js'
import Filter from './Filter.jsx'
import Statistiek from './Statistiek.jsx'
import TakenLijst from './TakenLijst.jsx'

export default function App() {
  const [koffie, setKoffie] = useState(0)
  const [taken, setTaken] = useState(() => maakTaken(3000))
  const [filter, setFilter] = useState('alle')

  function wissel(id) {
    setTaken((huidige) => huidige.map((t) => (t.id === id ? { ...t, klaar: !t.klaar } : t)))
  }

  return (
    <main>
      <h1>Takenbord</h1>
      <div className="balk">
        <button onClick={() => setKoffie(koffie + 1)}>Koffie gedronken: {koffie}</button>
        <Filter waarde={filter} onKies={setFilter} />
      </div>
      <Statistiek taken={taken} />
      <Profiler id="TakenLijst" onRender={meet}>
        <TakenLijst taken={taken} filter={filter} onWissel={wissel} />
      </Profiler>
    </main>
  )
}
