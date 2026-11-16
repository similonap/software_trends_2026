import { DatePipe } from '@angular/common';
import { Component, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-klok',
  imports: [DatePipe],
  template: `<p class="kaart">Het is nu <strong>{{ nu | date: 'HH:mm:ss' }}</strong></p>`,
})
export class Klok implements OnDestroy {
  nu = new Date();
  private timer = setInterval(() => {
    this.nu = new Date();
  }, 1000);

  ngOnDestroy() {
    clearInterval(this.timer);
  }
}
