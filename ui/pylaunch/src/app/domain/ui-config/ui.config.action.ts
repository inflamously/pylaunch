import { createAction } from '@ngrx/store';

const createBridgeAction = (name) => createAction(`[Bridge Frontend] ${name}`);

export const asyncLoadConfig = createBridgeAction('Async Load Config')
