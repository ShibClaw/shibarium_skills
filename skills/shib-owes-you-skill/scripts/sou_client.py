import json
import requests
from typing import Dict, Any, Optional

class SOUClient:
    """
    A client for interacting with the Shib Owes You (SOU) ecosystem.
    Created by: ShibClaw
    """
    
    # Contract Addresses
    BSC_SOU = "0xb65bd36fef84ebc5114cfd803a4f25b2b57f7777"
    ETH_SOU = "0xdea2a2a166e2fdc47b934bee68e6032f8f1ca09c"
    SHIBARIUM_SOU = "0x5e1aee526d1aa049b4d95e5b68ae7bb556e2d799"
    
    SHIU_ETH = "0x393a0ff130702c2dc6bfc500368394953450765f"
    SHIU_SHIBARIUM = "0x43bcc765ea97f48f5ba5b0801cefecb703f6c8fd"
    
    # Smart Wallet & ID Contracts (BSC)
    # Addresses are examples, ABI-based methods provided for interaction
    BSC_FACTORY = "0x31CCB08535398AFEe394E8cd8d34e72973C08cc9" 
    
    # Special Addresses
    DIRECT_BUY_BSC = "0x1401ADEf004F94aD27F13Ad7ad48de38b8F1Df2C"
    HOLDER_BOOSTER_BSC = "0x4a7D7f1e44a7B3bEd43f2EdeB2c653f9C86756cc"
    
    # RPC Endpoints (Defaults)
    RPC_URLS = {
        "bsc": "https://bsc-dataseed.binance.org/",
        "eth": "https://eth.llamarpc.com",
        "shibarium": "https://rpc.shibarium.shib.io"
    }

    def __init__(self, network: str = "bsc"):
        self.network = network.lower()
        self.rpc_url = self.RPC_URLS.get(self.network)

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

    def get_token_balance(self, address: str, token_address: str) -> float:
        """Returns the balance of a specific token for an address."""
        # Standard ERC20 balanceOf data: 0x70a08231 + 32 bytes address
        data = "0x70a08231" + address[2:].lower().zfill(64)
        result = self._post("eth_call", [{"to": token_address, "data": data}, "latest"])
        balance_wei = int(result["result"], 16)
        return balance_wei / 10**18

    def get_sou_balance(self, address: str) -> float:
        """Returns the SOU balance for the current network."""
        token_map = {
            "bsc": self.BSC_SOU,
            "eth": self.ETH_SOU,
            "shibarium": self.SHIBARIUM_SOU
        }
        token_address = token_map.get(self.network)
        if not token_address:
            raise ValueError(f"SOU token not supported on {self.network}")
        return self.get_token_balance(address, token_address)

    def get_shiu_balance(self, address: str) -> float:
        """Returns the SHIU balance for the current network."""
        token_map = {
            "eth": self.SHIU_ETH,
            "shibarium": self.SHIU_SHIBARIUM
        }
        token_address = token_map.get(self.network)
        if not token_address:
            raise ValueError(f"SHIU token not supported on {self.network}")
        return self.get_token_balance(address, token_address)

    # --- Smart Wallet Methods (BSC) ---

    def get_smart_wallet_address(self, owner_address: str) -> str:
        """
        Calls ownerToWallet(address) on the factory contract.
        Returns the smart wallet address associated with the owner.
        """
        if self.network != "bsc":
            raise ValueError("Smart Wallet functionality is only available on BSC.")
        
        # ownerToWallet selector: 0x6e768652
        data = "0x6e768652" + owner_address[2:].lower().zfill(64)
        result = self._post("eth_call", [{"to": self.BSC_FACTORY, "data": data}, "latest"])
        return "0x" + result["result"][-40:]

    def get_smart_wallet_id(self, wallet_address: str) -> str:
        """
        Calls walletToId(address) on the factory contract.
        Returns the ID string associated with the smart wallet.
        """
        if self.network != "bsc":
            raise ValueError("Smart Wallet functionality is only available on BSC.")
        
        # walletToId selector: 0x86866166
        data = "0x86866166" + wallet_address[2:].lower().zfill(64)
        result = self._post("eth_call", [{"to": self.BSC_FACTORY, "data": data}, "latest"])
        
        # Decode dynamic string
        hex_data = result["result"][2:]
        offset = int(hex_data[0:64], 16) * 2
        length = int(hex_data[offset:offset+64], 16) * 2
        string_hex = hex_data[offset+64:offset+64+length]
        return bytes.fromhex(string_hex).decode('utf-8')

    def resolve_id_to_wallet(self, id_str: str) -> str:
        """
        Calls idToWallet(string) on the factory contract.
        Returns the wallet address associated with the given ID.
        """
        if self.network != "bsc":
            raise ValueError("ID resolution is only available on BSC.")
        
        # idToWallet selector: 0x3678096c
        id_hex = id_str.encode('utf-8').hex()
        # Header (32 bytes) + Length (32 bytes) + String data padded to 32 bytes
        data = "0x3678096c"
        data += "0000000000000000000000000000000000000000000000000000000000000020"
        data += hex(len(id_str))[2:].zfill(64)
        data += id_hex.ljust(64, '0')
        
        result = self._post("eth_call", [{"to": self.BSC_FACTORY, "data": data}, "latest"])
        return "0x" + result["result"][-40:]

if __name__ == "__main__":
    # Example usage
    client = SOUClient("bsc")
    print(f"Network: {client.network}")
    print(f"BSC SOU Contract: {client.BSC_SOU}")
    print(f"Direct Buy Address: {client.DIRECT_BUY_BSC}")
    print(f"DSOU Service Link: https://shibfun.github.io/ShibOwesYou/DSOU/")
