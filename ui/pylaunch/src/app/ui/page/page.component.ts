import { AfterContentInit } from '@angular/core';
import { ContentChildren, Component, OnInit, QueryList } from '@angular/core';
import { PageFragmentComponent } from './page-fragment.component';

@Component({
  selector: 'app-page',
  templateUrl: './page.component.html',
  styleUrls: ['./page.component.css']
})
export class PageComponent implements OnInit, AfterContentInit {

  fragmentPresent = false;

  @ContentChildren(PageFragmentComponent) appPageFragments: QueryList<PageFragmentComponent>;

  constructor() {}

  ngAfterContentInit(): void {
    this.fragmentPresent = this.appPageFragments && this.appPageFragments.length > 0
  }

  ngOnInit(): void {
  }
}
