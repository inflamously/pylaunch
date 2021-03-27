import { createSelector } from "@ngrx/store";

export const selectTestConfig = (state: {test: any}) => state.test;
