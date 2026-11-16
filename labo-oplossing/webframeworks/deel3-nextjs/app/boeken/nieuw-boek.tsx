'use client'

import { useActionState } from 'react'
import { voegBoekToe, type Resultaat } from '../acties'

export default function NieuwBoek() {
  const [resultaat, actie, bezig] = useActionState(voegBoekToe, {} as Resultaat)

  return (
    <form action={actie} className="kaart">
      <input name="titel" placeholder="Titel" required maxLength={80} />{' '}
      <input name="auteur" placeholder="Auteur" required maxLength={80} />{' '}
      <button disabled={bezig}>{bezig ? 'Bezig…' : 'Toevoegen'}</button>
      {resultaat.fout && <p className="fout">{resultaat.fout}</p>}
    </form>
  )
}
