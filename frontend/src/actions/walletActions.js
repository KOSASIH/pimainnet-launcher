import { API_GET_WALLET_BALANCE } from '../api';

export const GET_WALLET_BALANCE_REQUEST = 'GET_WALLET_BALANCE_REQUEST';
export const GET_WALLET_BALANCE_SUCCESS = 'GET_WALLET_BALANCE_SUCCESS';
export const GET_WALLET_BALANCE_FAILURE = 'GET_WALLET_BALANCE_FAILURE';

export const getWalletBalance = (walletAddress) => async (dispatch) => {
  dispatch({ type: GET_WALLET_BALANCE_REQUEST });
  try {
    const response = await API_GET_WALLET_BALANCE(walletAddress);
    dispatch({ type: GET_WALLET_BALANCE_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: GET_WALLET_BALANCE_FAILURE, payload: error.message });
  }
};
