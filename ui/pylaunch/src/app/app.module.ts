import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from 'src/environments/environment.prod';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BridgeTestComponent } from './infrastructure/bridge-backend/bridge-test/bridge-test.component';
import { HeaderComponent } from './ui/header/header.component';
import { EffectsModule } from '@ngrx/effects';
import { ConfigEffects } from './domain/ui-config/ui.config.effects';
import { ToolbarComponent } from './ui/toolbar/toolbar.component';
import { ToolbarItemComponent } from './ui/toolbar/toolbar-item.component';
import { PageComponent } from './ui/page/page.component';
import { PageFragmentComponent } from './ui/page/page-fragment.component';
import { PageLayoutComponent } from './ui/page/page-layout.component';
import { FrameComponent } from './ui/frame/frame.component';
import { NavigationReducerMap } from './domain/navigation/navigation.reducer';
import { AppConfigStateReducerMap } from './domain/ui-config/ui.config.reducer';
import { EditorComponent } from './ui/editor/editor.component';

@NgModule({
  declarations: [
    AppComponent,
    BridgeTestComponent,
    HeaderComponent,
    ToolbarComponent,
    ToolbarItemComponent,
    PageComponent,
    PageFragmentComponent,
    PageLayoutComponent,
    FrameComponent,
    EditorComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot({
      ...AppConfigStateReducerMap,
      ...NavigationReducerMap
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
