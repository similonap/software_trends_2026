import type { Metadata } from 'next'
import Link from 'next/link'
import './globals.css'

export const metadata: Metadata = {
  title: 'Bibliotheek',
  description: 'Labo Next.js 16',
  icons: { icon: 'data:,' },
}

export default function RootLayout({ children }: LayoutProps<'/'>) {
  return (
    <html lang="nl">
      <body>
        <nav>
          <Link href="/">Home</Link>
          <Link href="/boeken">Boeken</Link>
          <Link href="/beheer">Aanmelden</Link>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  )
}
