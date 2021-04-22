import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { EffectsModule } from '@ngrx/effects';
import { Store, StoreModule } from '@ngrx/store';
import { AppComponent } from './app.component';
import { ConfigEffects } from './domain/ui-config/ui.config.effects';
import { configReducer } from './domain/ui-config/ui.config.reducer';

describe('AppComponent', () => {
  let store = undefined;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        RouterTestingModule,
        StoreModule.forRoot({ configuration: configReducer }),
        EffectsModule.forRoot([ConfigEffects])
      ],
      declarations: [
        AppComponent
      ],
    }).compileComponents();

    store = TestBed.inject(Store);
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should have injected store', (done) => {
    expect(store).toBeTruthy()
    done();
  });
});
