import { createReducer, on } from "@ngrx/store";
import { testConfig } from "./ui.config.action";

const initialState = {}

export function configReducer(state, action) {
  return createReducer(
    initialState,
    on(testConfig, (state) => {
      return {...state, test: "Hello World"}
    })
  )
}
