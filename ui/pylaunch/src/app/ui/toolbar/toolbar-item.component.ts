import { Component, Input, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { ToolbarActionPayload } from './toolbar-item.payload';
import { navigateToPage } from './toolbar.action';

@Component({
  selector: 'app-toolbar-item',
  templateUrl: './toolbar-item.component.html',
  styleUrls: ['./toolbar-item.component.css']
})
export class ToolbarItemComponent implements OnInit {

  @Input() itemType;
  @Input() payload: ToolbarActionPayload;

  constructor(
    private store: Store
  ) {
  }

  ngOnInit(): void {
  }

  dispatchAction(ev: Event) {
    if (ev.type === 'click') {
      this.store.dispatch(navigateToPage(this.payload));
    }
  }
}
