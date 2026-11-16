import { Suspense } from 'react'
import { huidigeRol } from '@/lib/sessie'
import { wisselRol } from '../acties'

// De rol staat in een cookie: die is pas bekend tijdens het request.
// Daarom staat dit stuk in een <Suspense>: de rest van de pagina kan al vooraf gerenderd worden.
async function Rol() {
  const rol = await huidigeRol()
  return (
    <div className="kaart">
      Je bent aangemeld als <strong>{rol}</strong>.{' '}
      <form action={wisselRol.bind(null, rol === 'lezer' ? 'beheerder' : 'lezer')} style={{ display: 'inline' }}>
        <button>Word {rol === 'lezer' ? 'beheerder' : 'lezer'}</button>
      </form>
    </div>
  )
}

export default function BeheerPagina() {
  return (
    <>
      <h1>Aanmelden</h1>
      <Suspense fallback={<p className="kaart">Rol ophalen…</p>}>
        <Rol />
      </Suspense>
    </>
  )
}
