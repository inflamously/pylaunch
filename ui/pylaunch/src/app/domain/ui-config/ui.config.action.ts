import { createAction, props } from '@ngrx/store';
import { AppConfigState } from './ui.config.interface';

const bridgeAction = (name) => createAction(`[Bridge Frontend] ${name}`, props<AppConfigState>());

export const asyncLoadConfig = bridgeAction('Config Loading')
export const asyncLoadConfigAvailable = bridgeAction('Config Available')
