import { NavigationState } from "./navigation.interface";

// TODO: Check how to retrieve state data from specific reducer group.
export const selectPage = (state: {navigation: NavigationState}) => state.navigation.page;
