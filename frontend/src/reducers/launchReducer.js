const initialState = {
  launching: false,
  error: null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case LAUNCH_PI_MAIN_NET_REQUEST:
      return { ...state, launching: true };
    case LAUNCH_PI_MAIN_NET_SUCCESS:
      return { ...state, launching: false, error: null };
    case LAUNCH_PI_MAIN_NET_FAILURE:
      return { ...state, launching: false, error: action.payload };
    default:
      return state;
  }
};
