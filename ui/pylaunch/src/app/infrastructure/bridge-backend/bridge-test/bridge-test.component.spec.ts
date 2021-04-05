import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BridgeTestComponent } from './bridge-test.component';

describe('BridgeTestComponent', () => {
  let component: BridgeTestComponent;
  let fixture: ComponentFixture<BridgeTestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BridgeTestComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BridgeTestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
