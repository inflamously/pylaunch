import { AfterContentInit } from '@angular/core';
import { ContentChildren, QueryList, TemplateRef } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';
import { selectPage } from 'src/app/domain/navigation/navigation.selector';

@Component({
  selector: 'app-frame',
  templateUrl: './frame.component.html',
  styleUrls: ['./frame.component.css']
})
export class FrameComponent implements OnInit, AfterContentInit {

  $page: Observable<string>;

  @ContentChildren(TemplateRef) pageTemplates = new QueryList<TemplateRef<any>>();

  constructor(
    private store: Store
  ) {
    this.$page = this.store.select(selectPage);
  }

  ngAfterContentInit(): void {
    this.$page.subscribe((v) => console.log(v));
  }

  ngOnInit(): void {

  }
}
