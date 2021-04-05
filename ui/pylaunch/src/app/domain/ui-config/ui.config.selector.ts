import { AppConfigState } from "./ui.config.interface";
import { AppConfigStateMap } from "./ui.config.reducer";

export const selectAppConfigState = (state: AppConfigStateMap) => state.configuration;
export const selectAppConfig = (state: AppConfigState) => state.params;
