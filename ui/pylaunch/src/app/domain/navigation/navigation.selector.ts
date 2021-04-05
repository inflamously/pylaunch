import { createSelector } from "@ngrx/store";
import { NavigationState } from "./navigation.interface";
import { NavigationStateMap } from "./navigation.reducer";

export const selectNavigationState = (state: NavigationStateMap) => state.navigation;
export const selectPage = createSelector(
  selectNavigationState,
  (state: NavigationState) => state.page
)
