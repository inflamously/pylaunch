import { OnInit, TemplateRef, ViewContainerRef } from '@angular/core';
import { Directive, Input } from '@angular/core';
import { Store } from '@ngrx/store';
import { distinctUntilChanged } from 'rxjs/operators';
import { selectPage } from './navigation.selector';

@Directive({
  selector: '[navigator]'
})
export class NavigatorDirective implements OnInit {

  @Input() navigator: string;

  constructor(
    private store: Store,
    private viewRef: ViewContainerRef,
    private templateRef: TemplateRef<any>
  ) {
    this.viewRef.clear();
  }

  ngOnInit(): void {
    this.store
    .select(selectPage)
    .pipe(distinctUntilChanged())
    .subscribe((page) => {
      if (page === this.navigator) {
        this.viewRef.clear();
        this.viewRef.createEmbeddedView(this.templateRef);
      } else {
        this.viewRef.clear();
      }
    })
  }
}
