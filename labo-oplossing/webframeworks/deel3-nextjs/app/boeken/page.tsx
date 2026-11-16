import { Suspense } from 'react'
import { haalBoekenOp } from '@/lib/db'
import { huidigeRol } from '@/lib/sessie'
import BoekenZoeker from './boeken-zoeker'
import NieuwBoek from './nieuw-boek'

// Opdracht 3.1: titel en formulier zitten in de statische shell,
// de lijst (die de cookie met je rol nodig heeft) streamt binnen in de <Suspense>.
export default function BoekenPagina() {
  return (
    <>
      <h1>Boeken</h1>
      <Suspense fallback={<p className="kaart">Boeken laden…</p>}>
        <Boekenlijst />
      </Suspense>
      <NieuwBoek />
    </>
  )
}

async function Boekenlijst() {
  // De boeken komen uit de cache (gedeeld voor iedereen), de rol is persoonlijk en dus altijd vers.
  const [boeken, rol] = await Promise.all([haalBoekenOp(), huidigeRol()])
  return <BoekenZoeker boeken={boeken} magVerwijderen={rol === 'beheerder'} />
}
