import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { from } from "rxjs";
import { map, mergeMap, tap } from "rxjs/operators";
import { eel } from "src/app/infrastructure/bridge-backend/eel";
import { asyncLoadConfig, asyncLoadConfigAvailable } from "./ui.config.action";

@Injectable()
export class ConfigEffects {

  config$ = createEffect(
    () => this.actions$
      .pipe(
        ofType(asyncLoadConfig),
        mergeMap(() => from(eel.exec("get_app_config"))
          .pipe(
            map((v) => asyncLoadConfigAvailable(v))
          ))
      ),
    // { dispatch: false }
  )

  constructor(private actions$: Actions) {

  }
}
