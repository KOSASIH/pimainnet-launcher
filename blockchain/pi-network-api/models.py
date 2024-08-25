from dataclasses import dataclass
from typing import List

@dataclass
class Block:
    block_hash: str
    block_number: int
    timestamp: int
    transactions: List[Transaction]

    @classmethod
    def from_json(cls, json_data):
        return cls(
            block_hash=json_data['block_hash'],
            block_number=json_data['block_number'],
            timestamp=json_data['timestamp'],
            transactions=[Transaction.from_json(tx) for tx in json_data['transactions']]
        )

@dataclass
class Transaction:
    transaction_hash: str
    from_address: str
    to_address: str
    amount: int
    timestamp: int

    @classmethod
    def from_json(cls, json_data):
        return cls(
            transaction_hash=json_data['transaction_hash'],
            from_address=json_data['from_address'],
            to_address=json_data['to_address'],
            amount=json_data['amount'],
            timestamp=json_data['timestamp']
        )

@dataclass
class Wallet:
    wallet_address: str
    balance: int

    @classmethod
    def from_json(cls, json_data):
        return cls(
            wallet_address=json_data['wallet_address'],
            balance=json_data['balance']
        )
