import { ActionReducerMap, createReducer, on } from "@ngrx/store";
import { asyncLoadConfig, asyncLoadConfigAvailable } from "./ui.config.action";
import { AppConfigState } from "./ui.config.interface";

const initialState: AppConfigState = {
  params: {}
}

export const configReducer = createReducer(
  initialState,
  on(asyncLoadConfig, (state, action) => ({...state, ...action})),
  on(asyncLoadConfigAvailable, (state, action) => {
    const {type, ...params} = action;

    return {
      ...state,
      params
    }
  })
)

export interface AppConfigStateMap {
  configuration: AppConfigState
}

export const AppConfigStateReducerMap: ActionReducerMap<AppConfigStateMap> = {
  configuration: configReducer
}
