import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com',
});

export const API_LAUNCH_PI_MAIN_NET = (nodeUrl, walletAddress) =>
  api.post('/launch', { nodeUrl, walletAddress });

export const API_GET_NODE_INFO = (nodeUrl) => api.get(`/node/${nodeUrl}`);

export const API_GET_WALLET_BALANCE = (walletAddress) =>
  api.get(`/wallet/${walletAddress}/balance`);

export default api;
