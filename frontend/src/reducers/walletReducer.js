const initialState = {
  walletBalance: null,
  error: null,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case GET_WALLET_BALANCE_REQUEST:
      return { ...state, walletBalance: null, error: null };
    case GET_WALLET_BALANCE_SUCCESS:
      return { ...state, walletBalance: action.payload, error: null };
    case GET_WALLET_BALANCE_FAILURE:
      return { ...state, walletBalance: null, error: action.payload };
    default:
      return state;
  }
};
