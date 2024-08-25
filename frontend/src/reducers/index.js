import { combineReducers } from 'redux';
import launchReducer from './launchReducer';
import nodeReducer from './nodeReducer';
import walletReducer from './walletReducer';

export default combineReducers({
  launch: launchReducer,
  node: nodeReducer,
  wallet: walletReducer,
});
