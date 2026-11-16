import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-teller',
  template: `
    <p class="kaart">
      Bezoekers vandaag: <strong>{{ aantal() }}</strong>
      <button (click)="plusEen()">+1</button>
    </p>
  `,
})
export class Teller {
  // Werkte al zonder signal (een template-event is een melding én maakt het component dirty),
  // maar met een signal hangt het niet meer af van wáár de wijziging vandaan komt.
  aantal = signal(0);

  plusEen() {
    this.aantal.update((n) => n + 1);
  }
}
