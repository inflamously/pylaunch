import { createReducer, on } from "@ngrx/store";
import { testConfig } from "./ui.config.action";

const initialState = {}

export const configReducer = createReducer(
  initialState,
  on(testConfig, (state) => {
    return {...state, test: "Hello World"}
  })
)
