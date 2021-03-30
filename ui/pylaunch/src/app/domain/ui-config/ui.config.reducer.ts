import { createReducer, on } from "@ngrx/store";
import { asyncLoadConfig, asyncLoadConfigAvailable } from "./ui.config.action";
import { AppConfigState } from "./ui.config.interface";

const initialState: AppConfigState = {}

export const configReducer = createReducer(
  initialState,
  on(asyncLoadConfig, (state, action) => ({...state, ...action})),
  on(asyncLoadConfigAvailable, (state, action) => ({...state, ...action}))
)
