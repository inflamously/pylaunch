import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import { selectPage } from 'src/app/domain/navigation/navigation.selector';

@Component({
  selector: 'app-frame',
  templateUrl: './frame.component.html',
  styleUrls: ['./frame.component.css']
})
export class FrameComponent implements OnInit {

  page$: Observable<string>;

  constructor(
    private store: Store
  ) {
    this.queryPageChangeEvent();
  }

  ngOnInit(): void {

  }

  queryPageChangeEvent() {
      this.page$ = this.store.select(selectPage);
  }
}
