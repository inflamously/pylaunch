import { ActionReducerMap, createReducer, on } from "@ngrx/store";
import { navigateToPage } from "src/app/ui/toolbar/toolbar.action";
import { NavigationState } from "./navigation.interface";

const initialState: NavigationState = {
  page: 'root-view'
}

export const navigationReducer = createReducer(
  initialState,
  on(navigateToPage, (state, action) => ({...state, page: action.value}))
)

export interface NavigationStateMap {
  navigation: NavigationState
}

export const NavigationReducerMap: ActionReducerMap<NavigationStateMap> = {
  navigation: navigationReducer
}
