import { createReducer, on } from "@ngrx/store";

interface ConfigStore {
  uiPath?: string;
  indexFile?: string;
}

const initialState: ConfigStore = {}

export const configReducer = createReducer(
  initialState,
)
