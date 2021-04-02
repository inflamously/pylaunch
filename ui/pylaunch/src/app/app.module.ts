import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Store, StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from 'src/environments/environment.prod';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { configReducer } from './domain/ui-config/ui.config.reducer';
import { selectConfig } from './domain/ui-config/ui.config.selector';
import { BridgeTestComponent } from './infrastructure/bridge-backend/bridge-test/bridge-test.component';
import { HeaderComponent } from './ui/header/header.component';
import { EffectsModule } from '@ngrx/effects';
import { ConfigEffects } from './domain/ui-config/ui.config.effects';
import { asyncLoadConfig } from './domain/ui-config/ui.config.action';
import { ToolbarComponent } from './ui/toolbar/toolbar.component';
import { ToolbarItemComponent } from './ui/toolbar/toolbar-item.component';
import { navigationReducer } from './domain/navigation/navigation.reducer';

@NgModule({
  declarations: [
    AppComponent,
    BridgeTestComponent,
    HeaderComponent,
    ToolbarComponent,
    ToolbarItemComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({
      configuration: configReducer,
      navigation: navigationReducer
    }),
    StoreDevtoolsModule.instrument({
      maxAge: 25,
      logOnly: environment.production
    }),
    EffectsModule.forRoot([
      ConfigEffects
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {

}
