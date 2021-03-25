import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BridgeTestComponent } from './infrastructure/bridge-backend/bridge-test/bridge-test.component';

@NgModule({
  declarations: [
    AppComponent,
    BridgeTestComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
