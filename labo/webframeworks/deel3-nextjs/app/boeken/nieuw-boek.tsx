import { voegBoekToe } from '../acties'

export default function NieuwBoek() {
  return (
    <form action={voegBoekToe} className="kaart">
      <input name="titel" placeholder="Titel" required maxLength={80} />{' '}
      <input name="auteur" placeholder="Auteur" required maxLength={80} />{' '}
      <button>Toevoegen</button>
    </form>
  )
}
