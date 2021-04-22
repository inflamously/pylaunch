import { TestBed } from '@angular/core/testing';
import { Store } from '@ngrx/store';
import { NavigatorDirective } from './navigator.directive';

describe('NavigatorDirective', () => {
  let store = undefined;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [],
      declarations: [
        NavigatorDirective
      ],
    }).compileComponents();

    store = TestBed.inject(Store);
  });

  it('should create an instance', () => {
    // TODO: Fix this
    // const directive = new NavigatorDirective();
    // expect(directive).toBeTruthy();
  });
});
