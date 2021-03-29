import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Store, StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from 'src/environments/environment.prod';
import { filter } from 'rxjs/operators';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { testConfig } from './domain/ui-config/ui.config.action';
import { configReducer } from './domain/ui-config/ui.config.reducer';
import { selectTestConfig } from './domain/ui-config/ui.config.selector';
import { BridgeTestComponent } from './infrastructure/bridge-backend/bridge-test/bridge-test.component';
import { HeaderComponent } from './ui/header/header.component';

@NgModule({
  declarations: [
    AppComponent,
    BridgeTestComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({ config: configReducer }),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(
    store: Store
  ) {
    store.dispatch(testConfig());
    store.select(selectTestConfig).subscribe((v) => console.log(v));
  }
}
