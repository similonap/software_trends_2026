'use server'

// Elke functie hier is een publiek HTTP-endpoint (slide "Een Server Action is een publiek endpoint").
// Ze controleert dus zelf: wie ben je, mag jij dit, en is de input geldig?
import { updateTag } from 'next/cache'
import { cookies } from 'next/headers'
import { bewaarBoek, wisBoek } from '@/lib/db'
import { huidigeRol } from '@/lib/sessie'

export type Resultaat = { fout?: string; ok?: boolean }

export async function voegBoekToe(_vorige: Resultaat, formData: FormData): Promise<Resultaat> {
  // Validatie op de server: required en maxLength in de HTML zijn gebruiksgemak, geen beveiliging.
  const titel = formData.get('titel')
  const auteur = formData.get('auteur')
  if (typeof titel !== 'string' || typeof auteur !== 'string') return { fout: 'Ongeldige invoer.' }
  if (!titel.trim() || !auteur.trim()) return { fout: 'Titel en auteur zijn verplicht.' }
  if (titel.length > 80 || auteur.length > 80) return { fout: 'Titel en auteur zijn maximaal 80 tekens.' }

  await bewaarBoek(titel.trim(), auteur.trim())
  // Opdracht 3.2: de gecachte lijst meteen ongeldig maken, zodat de gebruiker zijn eigen wijziging ziet.
  updateTag('boeken')
  return { ok: true }
}

export async function verwijderBoek(id: unknown) {
  // Autorisatie: de knop verbergen voor lezers is geen beveiliging, deze controle wel.
  if ((await huidigeRol()) !== 'beheerder') throw new Error('Enkel beheerders mogen boeken verwijderen.')
  // Validatie: het argument komt van de client en kan dus om het even wat zijn.
  if (typeof id !== 'number' || !Number.isInteger(id)) throw new Error('Ongeldig id.')

  await wisBoek(id)
  updateTag('boeken')
}

// Let op: dit is een gesimuleerde login. Iedereen kan zich hier beheerder maken.
// In een echte app controleer je hier een wachtwoord of een identity provider.
export async function wisselRol(rol: unknown) {
  if (rol !== 'lezer' && rol !== 'beheerder') throw new Error('Ongeldige rol.')
  const jar = await cookies()
  jar.set('rol', rol, { httpOnly: true, sameSite: 'lax' })
}
