import { API_LAUNCH_PI_MAIN_NET } from '../api';

export const LAUNCH_PI_MAIN_NET_REQUEST = 'LAUNCH_PI_MAIN_NET_REQUEST';
export const LAUNCH_PI_MAIN_NET_SUCCESS = 'LAUNCH_PI_MAIN_NET_SUCCESS';
export const LAUNCH_PI_MAIN_NET_FAILURE = 'LAUNCH_PI_MAIN_NET_FAILURE';

export const launchPiMainNet = (nodeUrl, walletAddress) => async (dispatch) => {
  dispatch({ type: LAUNCH_PI_MAIN_NET_REQUEST });
  try {
    const response = await API_LAUNCH_PI_MAIN_NET(nodeUrl, walletAddress);
    dispatch({ type: LAUNCH_PI_MAIN_NET_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: LAUNCH_PI_MAIN_NET_FAILURE, payload: error.message });
  }
};
