'use server'

import { cookies } from 'next/headers'
import { bewaarBoek, wisBoek } from '@/lib/db'
import type { Rol } from '@/lib/sessie'

export async function voegBoekToe(formData: FormData) {
  const titel = String(formData.get('titel') ?? '')
  const auteur = String(formData.get('auteur') ?? '')
  await bewaarBoek(titel, auteur)
}

export async function verwijderBoek(id: number) {
  await wisBoek(id)
}

export async function wisselRol(rol: Rol) {
  const jar = await cookies()
  jar.set('rol', rol)
}
