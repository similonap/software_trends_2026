import { Component } from '@angular/core';

@Component({
  selector: 'app-teller',
  template: `
    <p class="kaart">
      Bezoekers vandaag: <strong>{{ aantal }}</strong>
      <button (click)="plusEen()">+1</button>
    </p>
  `,
})
export class Teller {
  aantal = 0;

  plusEen() {
    this.aantal++;
  }
}
