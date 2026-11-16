import { Component, computed, resource } from '@angular/core';
import { Boek } from './boek';
import { BoekenLijst } from './boeken-lijst';

@Component({
  selector: 'app-boeken',
  imports: [BoekenLijst],
  template: `
    <section class="kaart">
      <h2>Boeken ({{ aantal() }})</h2>
      @if (boeken.isLoading()) {
        <p>Laden…</p>
      } @else if (boeken.error()) {
        <p>De boeken konden niet geladen worden.</p>
      } @else {
        <app-boeken-lijst [boeken]="boeken.value()" />
      }
      <form (submit)="voegToe($event, titel)">
        <input #titel placeholder="Titel van een nieuw boek" />
        <button>Toevoegen</button>
      </form>
    </section>
  `,
})
export class Boeken {
  // resource(): asynchrone data als signals (value, isLoading, error).
  // Als de Promise klaar is, zet resource de signals, en dat is een melding voor Angular.
  boeken = resource({
    loader: async ({ abortSignal }) => {
      const antwoord = await fetch('/boeken.json', { signal: abortSignal });
      await new Promise((klaar) => setTimeout(klaar, 800)); // doe alsof de server traag is
      return (await antwoord.json()) as Boek[];
    },
    defaultValue: [],
  });

  aantal = computed(() => this.boeken.value().length);

  voegToe(event: Event, veld: HTMLInputElement) {
    event.preventDefault();
    const titel = veld.value.trim();
    if (!titel) return;
    // Nieuwe array = nieuwe referentie: de input van BoekenLijst verandert, dus wordt die dirty.
    this.boeken.update((lijst) => [...lijst, { id: Date.now(), titel, auteur: 'onbekend' }]);
    veld.value = '';
  }
}
