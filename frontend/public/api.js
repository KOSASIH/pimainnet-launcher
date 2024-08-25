// API endpoints for interacting with PiMainNet
const api = {
    async getNodeInfo(nodeUrl) {
        // Make API call to retrieve node info
        const response = await fetch(`${nodeUrl}/api/node-info`);
        return response.json();
    },

    async getWalletBalance(walletAddress) {
        // Make API call to retrieve wallet balance
        const response = await fetch(`${nodeUrl}/api/wallet-balance?address=${walletAddress}`);
        return response.json();
    },

    async launchPiMainNet(nodeUrl, walletAddress) {
        // Make API call to launch PiMainNet
        const response = await fetch(`${nodeUrl}/api/launch`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                walletAddress
            })
        });
        return response.json();
    }
};

export default api;
