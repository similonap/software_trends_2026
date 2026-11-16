// Bonus: het formulier met Signal Forms (stabiel sinds Angular 22).
// Kopieer dit bestand naar src/app/boeken.ts om het te proberen.
import { Component, computed, resource, signal } from '@angular/core';
import { form, FormField, maxLength, required, submit } from '@angular/forms/signals';
import { Boek } from './boek';
import { BoekenLijst } from './boeken-lijst';

@Component({
  selector: 'app-boeken',
  imports: [BoekenLijst, FormField],
  template: `
    <section class="kaart">
      <h2>Boeken ({{ aantal() }})</h2>
      @if (boeken.isLoading()) {
        <p>Laden…</p>
      } @else {
        <app-boeken-lijst [boeken]="boeken.value()" />
      }
      <form (submit)="voegToe($event)">
        <input [formField]="nieuwBoek.titel" placeholder="Titel" />
        <input [formField]="nieuwBoek.auteur" placeholder="Auteur" />
        <button [disabled]="nieuwBoek().invalid()">Toevoegen</button>
        @for (fout of nieuwBoek.titel().errors(); track fout.kind) {
          @if (nieuwBoek.titel().touched()) {
            <p class="fout">{{ fout.message }}</p>
          }
        }
      </form>
    </section>
  `,
})
export class Boeken {
  boeken = resource({
    loader: async () => (await (await fetch('/boeken.json')).json()) as Boek[],
    defaultValue: [],
  });
  aantal = computed(() => this.boeken.value().length);

  // Het model van het formulier is een gewone signal ...
  model = signal({ titel: '', auteur: '' });
  // ... en form() maakt er een boom van velden van, elk met waarde, validatie en status als signals.
  nieuwBoek = form(this.model, (pad) => {
    required(pad.titel, { message: 'Geef een titel op' });
    maxLength(pad.titel, 80, { message: 'Maximaal 80 tekens' });
  });

  voegToe(event: Event) {
    event.preventDefault();
    submit(this.nieuwBoek, async () => {
      const { titel, auteur } = this.model();
      this.boeken.update((lijst) => [...lijst, { id: Date.now(), titel, auteur: auteur || 'onbekend' }]);
      // reset(): waarde terugzetten én touched/dirty wissen, anders verschijnt de foutmelding meteen opnieuw
      this.nieuwBoek().reset({ titel: '', auteur: '' });
    });
  }
}
