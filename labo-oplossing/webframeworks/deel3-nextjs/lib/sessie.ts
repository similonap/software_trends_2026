import { cookies } from 'next/headers'

// Een sterk vereenvoudigde "login": je rol staat in een cookie.
// (In een echte app zou dit een ondertekende sessie zijn, bv. via Auth.js.)
export type Rol = 'lezer' | 'beheerder'

export async function huidigeRol(): Promise<Rol> {
  const jar = await cookies()
  return jar.get('rol')?.value === 'beheerder' ? 'beheerder' : 'lezer'
}
