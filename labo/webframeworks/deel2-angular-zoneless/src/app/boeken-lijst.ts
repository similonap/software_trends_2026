import { Component, input } from '@angular/core';
import { Boek } from './boek';

@Component({
  selector: 'app-boeken-lijst',
  template: `
    <ul>
      @for (boek of boeken(); track boek.id) {
        <li>{{ boek.titel }} <small>({{ boek.auteur }})</small></li>
      }
    </ul>
  `,
})
export class BoekenLijst {
  boeken = input.required<Boek[]>();
}
