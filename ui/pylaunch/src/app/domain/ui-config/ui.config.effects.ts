import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { tap } from "rxjs/operators";
import { asyncLoadConfig } from "./ui.config.action";

@Injectable()
export class ConfigEffect {

  config$ = createEffect(() => this.actions$
    .pipe(
      tap((x) => console.log(x)),
      tap((_) => {
        // of(eel.exec("get_app_config"))
        // .subscribe((y) => console.log(y))
        // .pipe(map((_) => asyncLoadConfig()))
      })
      // switchMap((_) => {
      //   return of(eel
      //     .exec("get_app_config"))
      //     .pipe(map((_) => asyncLoadConfig()))
      // }),
    )
  )

  constructor(private actions$: Actions) {

  }
}
