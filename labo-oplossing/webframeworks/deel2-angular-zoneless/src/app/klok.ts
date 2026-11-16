import { DatePipe } from '@angular/common';
import { Component, DestroyRef, inject, signal } from '@angular/core';

@Component({
  selector: 'app-klok',
  imports: [DatePipe],
  template: `<p class="kaart">Het is nu <strong>{{ nu() | date: 'HH:mm:ss' }}</strong></p>`,
})
export class Klok {
  // Een signal: elke set() meldt aan Angular dat deze view opnieuw getekend moet worden.
  nu = signal(new Date());

  constructor() {
    const timer = setInterval(() => this.nu.set(new Date()), 1000);
    inject(DestroyRef).onDestroy(() => clearInterval(timer));
  }
}
