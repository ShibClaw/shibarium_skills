import requests
import json

class ShibariumClient:
    """
    ShibariumClient provides a robust and easy-to-use interface for interacting with the Shibarium blockchain.
    It encapsulates common JSON-RPC methods for network monitoring, account management, and transaction submission.
    """

    # Class constants for network configuration
    MAINNET_RPC = "https://rpc.shibarium.shib.io"
    TESTNET_RPC = "https://rpc.puppynet.shib.io"
    MAINNET_CHAIN_ID = 109
    TESTNET_CHAIN_ID = 157

    def __init__(self, rpc_url: str):
        """
        Initialize the ShibariumClient with a specific RPC endpoint.

        Args:
            rpc_url (str): The URL of the Shibarium RPC endpoint.
        """
        self.rpc_url = rpc_url
        self.session = requests.Session()

    def _post(self, method: str, params: list = None) -> dict:
        """
        Internal JSON-RPC call handler for making requests to the Shibarium node.

        Args:
            method (str): The JSON-RPC method name.
            params (list, optional): The parameters for the JSON-RPC call. Defaults to None.

        Returns:
            dict: The 'result' field from the JSON-RPC response.

        Raises:
            Exception: If the RPC call fails or returns an error.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1
        }
        
        try:
            response = self.session.post(
                self.rpc_url,
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            
            result = response.json()
            if 'error' in result:
                raise Exception(f"RPC Error: {result['error'].get('message', 'Unknown error')}")
            
            return result.get('result')
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP Request failed: {str(e)}")

    def get_block_number(self) -> int:
        """
        Retrieve the current block number of the Shibarium network.

        Returns:
            int: The current block number.
        """
        hex_block = self._post("eth_blockNumber")
        return int(hex_block, 16)

    def get_balance(self, address: str) -> float:
        """
        Retrieve the BONE balance for a specific address.

        Args:
            address (str): The Ethereum-style address to query.

        Returns:
            float: The balance in BONE (converted from wei).
        """
        hex_balance = self._post("eth_getBalance", [address, "latest"])
        wei_balance = int(hex_balance, 16)
        return wei_balance / 10**18

    def get_transaction_count(self, address: str) -> int:
        """
        Retrieve the transaction count (nonce) for a specific address.

        Args:
            address (str): The Ethereum-style address to query.

        Returns:
            int: The transaction count.
        """
        hex_count = self._post("eth_getTransactionCount", [address, "latest"])
        return int(hex_count, 16)

    def get_gas_price(self) -> float:
        """
        Retrieve the current gas price on the Shibarium network.

        Returns:
            float: The gas price in Gwei.
        """
        hex_price = self._post("eth_gasPrice")
        wei_price = int(hex_price, 16)
        return wei_price / 10**9

    def get_chain_id(self) -> int:
        """
        Retrieve the chain ID of the connected Shibarium network.

        Returns:
            int: The chain ID.
        """
        hex_chain_id = self._post("eth_chainId")
        return int(hex_chain_id, 16)

    def send_raw_transaction(self, signed_tx_hex: str) -> str:
        """
        Submit a signed raw transaction to the Shibarium network.

        Args:
            signed_tx_hex (str): The hex string of the signed transaction.

        Returns:
            str: The transaction hash.
        """
        if not signed_tx_hex.startswith("0x"):
            signed_tx_hex = "0x" + signed_tx_hex
        return self._post("eth_sendRawTransaction", [signed_tx_hex])

if __name__ == "__main__":
    # Example usage for demonstration purposes
    print("--- Shibarium Client Demo ---")
    
    # Using Puppynet (Testnet) for demonstration
    client = ShibariumClient(ShibariumClient.TESTNET_RPC)
    
    try:
        # 1. Get Block Number
        block_num = client.get_block_number()
        print(f"Current Block Number (Puppynet): {block_num}")
        
        # 2. Get Gas Price
        gas_price = client.get_gas_price()
        print(f"Current Gas Price: {gas_price:.2f} Gwei")
        
        # 3. Get Chain ID
        chain_id = client.get_chain_id()
        print(f"Chain ID: {chain_id}")
        
        # 4. Get Balance (using a zero address as example)
        example_addr = "0x0000000000000000000000000000000000000000"
        balance = client.get_balance(example_addr)
        print(f"Balance of {example_addr}: {balance} BONE")
        
    except Exception as e:
        print(f"Error during demo: {e}")
