'use client'

import { useState, useTransition } from 'react'
import { verwijderBoek } from '../acties'
import type { Boek } from '@/lib/db'

export default function BoekenZoeker({ boeken, magVerwijderen }: { boeken: Boek[]; magVerwijderen: boolean }) {
  const [zoekterm, setZoekterm] = useState('')
  const [bezig, startTransition] = useTransition()
  const zichtbaar = boeken.filter((b) => b.titel.toLowerCase().includes(zoekterm.toLowerCase()))

  return (
    <section className="kaart">
      <input placeholder="Zoek op titel" value={zoekterm} onChange={(e) => setZoekterm(e.target.value)} />
      <ul>
        {zichtbaar.map((boek) => (
          <li key={boek.id}>
            {boek.titel} <small>({boek.auteur})</small>{' '}
            {magVerwijderen && (
              <button disabled={bezig} onClick={() => startTransition(() => verwijderBoek(boek.id))}>
                Verwijder
              </button>
            )}
          </li>
        ))}
      </ul>
    </section>
  )
}
