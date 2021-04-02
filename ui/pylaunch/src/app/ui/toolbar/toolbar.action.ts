import { createAction, props } from "@ngrx/store";
import { ToolbarActionPayload } from "./toolbar-item.payload";

const toolbarAction = (name) => createAction(`[Toolbar] ${name}`, props<ToolbarActionPayload>())

export const navigateToPage = toolbarAction('Navigate To Page')
