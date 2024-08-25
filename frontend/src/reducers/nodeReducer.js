const initialState = {
  nodeInfo: null,
  error: null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_NODE_INFO_REQUEST:
      return { ...state, nodeInfo: null, error: null };
    case GET_NODE_INFO_SUCCESS:
      return { ...state, nodeInfo: action.payload, error: null };
    case GET_NODE_INFO_FAILURE:
      return { ...state, nodeInfo: null, error: action.payload };
    default:
      return state;
  }
};
