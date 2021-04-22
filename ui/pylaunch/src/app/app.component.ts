import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { asyncLoadConfig } from './domain/ui-config/ui.config.action';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  title = 'pylaunch';

  constructor(
    private store: Store
  ) {}

  ngOnInit(): void {
    this.loadConfig();
  }

  loadConfig() {
    this.store.dispatch(asyncLoadConfig(null));
  }
}
