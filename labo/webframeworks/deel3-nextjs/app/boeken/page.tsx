import { haalBoekenOp } from '@/lib/db'
import { huidigeRol } from '@/lib/sessie'
import BoekenZoeker from './boeken-zoeker'
import NieuwBoek from './nieuw-boek'

export default async function BoekenPagina() {
  const boeken = await haalBoekenOp()
  const rol = await huidigeRol()

  return (
    <>
      <h1>Boeken</h1>
      <BoekenZoeker boeken={boeken} magVerwijderen={rol === 'beheerder'} />
      <NieuwBoek />
    </>
  )
}
