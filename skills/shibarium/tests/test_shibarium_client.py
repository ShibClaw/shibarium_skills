import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add the directory containing shibarium_client.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from shibarium_client import ShibariumClient

class TestShibariumClient(unittest.TestCase):

    def setUp(self):
        self.mainnet_client = ShibariumClient(ShibariumClient.MAINNET_RPC)
        self.testnet_client = ShibariumClient(ShibariumClient.TESTNET_RPC)

    @patch("requests.post")
    def test_get_block_number(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x100"}
        mock_post.return_value = mock_response

        block_number = self.mainnet_client.get_block_number()
        self.assertEqual(block_number, 256)
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1
        })

    @patch("requests.post")
    def test_get_balance(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x8ac7230489e80000"}
        mock_post.return_value = mock_response

        # 0x8ac7230489e80000 in wei is 10000000000000000000 in decimal, which is 10 BONE
        balance = self.mainnet_client.get_balance("0x123...")
        self.assertAlmostEqual(balance, 10.0)
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_getBalance", "params": ["0x123...", "latest"], "id": 1
        })

    @patch("requests.post")
    def test_get_transaction_count(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x5"}
        mock_post.return_value = mock_response

        tx_count = self.mainnet_client.get_transaction_count("0x123...")
        self.assertEqual(tx_count, 5)
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_getTransactionCount", "params": ["0x123...", "latest"], "id": 1
        })

    @patch("requests.post")
    def test_get_gas_price(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x2540BE400"}
        mock_post.return_value = mock_response

        # 0x2540BE400 in wei is 10000000000 in decimal, which is 10 Gwei
        gas_price = self.mainnet_client.get_gas_price()
        self.assertAlmostEqual(gas_price, 10.0)
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_gasPrice", "params": [], "id": 1
        })

    @patch("requests.post")
    def test_get_chain_id(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x6d"}
        mock_post.return_value = mock_response

        # 0x6d is 109 in decimal
        chain_id = self.mainnet_client.get_chain_id()
        self.assertEqual(chain_id, 109)
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_chainId", "params": [], "id": 1
        })

    @patch("requests.post")
    def test_send_raw_transaction(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0xhash123"}
        mock_post.return_value = mock_response

        signed_tx = "0xf86..."
        tx_hash = self.mainnet_client.send_raw_transaction(signed_tx)
        self.assertEqual(tx_hash, "0xhash123")
        mock_post.assert_called_once_with(self.mainnet_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_sendRawTransaction", "params": [signed_tx], "id": 1
        })

    def test_constants(self):
        self.assertEqual(ShibariumClient.MAINNET_RPC, "https://rpc.shibarium.shib.io")
        self.assertEqual(ShibariumClient.TESTNET_RPC, "https://rpc.puppynet.shib.io")
        self.assertEqual(ShibariumClient.MAINNET_CHAIN_ID, 109)
        self.assertEqual(ShibariumClient.TESTNET_CHAIN_ID, 157)

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
