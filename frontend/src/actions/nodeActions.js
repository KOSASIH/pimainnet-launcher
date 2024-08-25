import { API_GET_NODE_INFO } from '../api';

export const GET_NODE_INFO_REQUEST = 'GET_NODE_INFO_REQUEST';
export const GET_NODE_INFO_SUCCESS = 'GET_NODE_INFO_SUCCESS';
export const GET_NODE_INFO_FAILURE = 'GET_NODE_INFO_FAILURE';

export const getNodeInfo = (nodeUrl) => async (dispatch) => {
  dispatch({ type: GET_NODE_INFO_REQUEST });
  try {
    const response = await API_GET_NODE_INFO(nodeUrl);
    dispatch({ type: GET_NODE_INFO_SUCCESS, payload: response.data });
  } catch (error) {
    dispatch({ type: GET_NODE_INFO_FAILURE, payload: error.message });
  }
};
