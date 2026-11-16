import { Component, OnInit } from '@angular/core';
import { Boek } from './boek';
import { BoekenLijst } from './boeken-lijst';

@Component({
  selector: 'app-boeken',
  imports: [BoekenLijst],
  template: `
    <section class="kaart">
      <h2>Boeken ({{ boeken.length }})</h2>
      @if (laden) {
        <p>Laden…</p>
      } @else {
        <app-boeken-lijst [boeken]="boeken" />
      }
      <form (submit)="voegToe($event, titel)">
        <input #titel placeholder="Titel van een nieuw boek" />
        <button>Toevoegen</button>
      </form>
    </section>
  `,
})
export class Boeken implements OnInit {
  boeken: Boek[] = [];
  laden = true;

  async ngOnInit() {
    const antwoord = await fetch('/boeken.json');
    await new Promise((klaar) => setTimeout(klaar, 800)); // doe alsof de server traag is
    this.boeken = await antwoord.json();
    this.laden = false;
  }

  voegToe(event: Event, veld: HTMLInputElement) {
    event.preventDefault();
    if (!veld.value.trim()) return;
    this.boeken.push({ id: Date.now(), titel: veld.value.trim(), auteur: 'onbekend' });
    veld.value = '';
  }
}
