import { createSelector } from "@ngrx/store";

export const selectTestConfig = (state: {config: {test: any}}) => state.config.test;
