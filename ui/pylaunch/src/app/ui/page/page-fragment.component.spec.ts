import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageFragmentComponent } from './page-fragment.component';

describe('PageFragmentComponent', () => {
  let component: PageFragmentComponent;
  let fixture: ComponentFixture<PageFragmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PageFragmentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PageFragmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
