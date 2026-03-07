import json
import requests
from typing import Dict, Any, Optional

class ShibariumClient:
    """
    A simple client for interacting with the Shibarium network.
    Created by: ShibClaw
    """
    
    MAINNET_RPC = "https://rpc.shibarium.shib.io"
    TESTNET_RPC = "https://rpc.puppynet.shib.io"
    MAINNET_CHAIN_ID = 109
    TESTNET_CHAIN_ID = 157

    def __init__(self, rpc_url: str = MAINNET_RPC):
        self.rpc_url = rpc_url

    def _post(self, method: str, params: list = []) -> Dict[str, Any]:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        response = requests.post(self.rpc_url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_block_number(self) -> int:
        """Returns the current block number."""
        result = self._post("eth_blockNumber")
        return int(result["result"], 16)

    def get_balance(self, address: str) -> float:
        """Returns the balance of the given address in BONE."""
        result = self._post("eth_getBalance", [address, "latest"])
        balance_wei = int(result["result"], 16)
        return balance_wei / 10**18

    def get_transaction_count(self, address: str) -> int:
        """Returns the number of transactions sent from an address."""
        result = self._post("eth_getTransactionCount", [address, "latest"])
        return int(result["result"], 16)

    def get_gas_price(self) -> float:
        """Returns the current gas price in Gwei."""
        result = self._post("eth_gasPrice")
        gas_price_wei = int(result["result"], 16)
        return gas_price_wei / 10**9

    def get_chain_id(self) -> int:
        """Returns the chain ID of the connected network."""
        result = self._post("eth_chainId")
        return int(result["result"], 16)

    def send_raw_transaction(self, signed_tx_hex: str) -> str:
        """Submits a pre-signed transaction to the network."""
        result = self._post("eth_sendRawTransaction", [signed_tx_hex])
        return result["result"]

if __name__ == "__main__":
    # Example usage for read-only operations
    client = ShibariumClient(ShibariumClient.TESTNET_RPC)
    print(f"Connected to Chain ID: {client.get_chain_id()}")
    print(f"Current Block: {client.get_block_number()}")
    print(f"Current Gas Price: {client.get_gas_price()} Gwei")
