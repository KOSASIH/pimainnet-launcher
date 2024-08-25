import React, { useState, useEffect, useContext } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { AppContext } from '../context/AppContext';
import App from '../components/App';
import { api } from '../api';
import { NodeInfo, WalletBalance } from '../types';

const AppContainer = () => {
  const [nodeUrl, setNodeUrl] = useState('https://example.com/node');
  const [walletAddress, setWalletAddress] = useState('0x...');
  const [nodeInfo, setNodeInfo] = useState<NodeInfo | null>(null);
  const [walletBalance, setWalletBalance] = useState<WalletBalance | null>(null);
  const [launching, setLaunching] = useState(false);
  const [error, setError] = useState(null);

  const { theme, language } = useContext(AppContext);

  useEffect(() => {
    const fetchNodeInfo = async () => {
      try {
        const response = await api.getNodeInfo(nodeUrl);
        setNodeInfo(response.data);
      } catch (error) {
        setError(error.message);
      }
    };

    const fetchWalletBalance = async () => {
      try {
        const response = await api.getWalletBalance(walletAddress);
        setWalletBalance(response.data);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchNodeInfo();
    fetchWalletBalance();
  }, [nodeUrl, walletAddress]);

  const handleLaunch = async () => {
    setLaunching(true);
    try {
      await api.launchPiMainNet(nodeUrl, walletAddress);
      setLaunching(false);
    } catch (error) {
      setError(error.message);
      setLaunching(false);
    }
  };

  return (
    <BrowserRouter>
      <App
        theme={theme}
        language={language}
        nodeUrl={nodeUrl}
        walletAddress={walletAddress}
        nodeInfo={nodeInfo}
        walletBalance={walletBalance}
        launching={launching}
        error={error}
        onLaunch={handleLaunch}
      />
    </BrowserRouter>
  );
};

export default AppContainer;
