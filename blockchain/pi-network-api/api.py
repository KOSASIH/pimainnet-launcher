import requests
import json
from .models import Block, Transaction, Wallet
from .utils import hex_to_bytes, bytes_to_hex

class PiNetworkAPI:
    def __init__(self, base_url='https://api.pi.network'):
        self.base_url = base_url

    def get_block(self, block_hash):
        response = requests.get(f'{self.base_url}/blocks/{block_hash}')
        return Block.from_json(response.json())

    def get_transaction(self, transaction_hash):
        response = requests.get(f'{self.base_url}/transactions/{transaction_hash}')
        return Transaction.from_json(response.json())

    def get_wallet(self, wallet_address):
        response = requests.get(f'{self.base_url}/wallets/{wallet_address}')
        return Wallet.from_json(response.json())

    def send_transaction(self, transaction):
        response = requests.post(f'{self.base_url}/transactions', json=transaction.to_json())
        return response.json()

    def get_blockchain_info(self):
        response = requests.get(f'{self.base_url}/blockchain/info')
        return response.json()
