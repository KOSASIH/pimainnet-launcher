export interface NodeInfo {
  nodeUrl: string;
  nodeName: string;
  nodeDescription: string;
}

export interface WalletBalance {
  walletAddress: string;
  balance: number;
}

export interface LaunchResponse {
  success: boolean;
  message: string;
}
