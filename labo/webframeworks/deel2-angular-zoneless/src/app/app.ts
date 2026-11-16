import { Component } from '@angular/core';
import { Boeken } from './boeken';
import { Klok } from './klok';
import { Teller } from './teller';

@Component({
  selector: 'app-root',
  imports: [Klok, Teller, Boeken],
  styleUrl: './app.css',
  template: `
    <main>
      <h1>Bibliotheek</h1>
      <app-klok />
      <app-teller />
      <app-boeken />
    </main>
  `,
})
export class App {}
