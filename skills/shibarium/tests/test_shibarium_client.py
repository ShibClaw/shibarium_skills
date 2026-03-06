import unittest
from unittest.mock import MagicMock, patch
import json
import sys
import os

# Add scripts directory to path for importing ShibariumClient
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from shibarium_client import ShibariumClient

class TestShibariumClient(unittest.TestCase):
    """
    Complete unit test suite for ShibariumClient, using mocks to isolate network calls.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the client with a dummy RPC URL.
        """
        self.rpc_url = "https://rpc.dummy.shib.io"
        self.client = ShibariumClient(self.rpc_url)

    @patch('requests.Session.post')
    def test_post_success(self, mock_post):
        """
        Test that _post correctly handles a successful JSON-RPC response.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"jsonrpc": "2.0", "result": "0x123", "id": 1}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = self.client._post("eth_dummyMethod", ["param1"])
        
        self.assertEqual(result, "0x123")
        mock_post.assert_called_once()

    @patch('requests.Session.post')
    def test_post_rpc_error(self, mock_post):
        """
        Test that _post correctly raises an exception when the RPC returns an error.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
            "id": 1
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.client._post("eth_nonExistentMethod")
        
        self.assertIn("RPC Error: Method not found", str(context.exception))

    @patch('shibarium_client.ShibariumClient._post')
    def test_get_block_number(self, mock_post):
        """
        Test that get_block_number correctly converts hex result to integer.
        """
        mock_post.return_value = "0x1234" # 4660 in decimal
        
        result = self.client.get_block_number()
        
        self.assertEqual(result, 4660)
        mock_post.assert_called_with("eth_blockNumber")

    @patch('shibarium_client.ShibariumClient._post')
    def test_get_balance(self, mock_post):
        """
        Test that get_balance correctly converts hex wei to BONE.
        """
        # 1 BONE in wei = 10^18 (0xDE0B6B3A7640000)
        mock_post.return_value = "0xDE0B6B3A7640000"
        
        address = "0x1234567890123456789012345678901234567890"
        result = self.client.get_balance(address)
        
        self.assertEqual(result, 1.0)
        mock_post.assert_called_with("eth_getBalance", [address, "latest"])

    @patch('shibarium_client.ShibariumClient._post')
    def test_get_transaction_count(self, mock_post):
        """
        Test that get_transaction_count correctly converts hex to integer.
        """
        mock_post.return_value = "0xA" # 10 in decimal
        
        address = "0x1234567890123456789012345678901234567890"
        result = self.client.get_transaction_count(address)
        
        self.assertEqual(result, 10)
        mock_post.assert_called_with("eth_getTransactionCount", [address, "latest"])

    @patch('shibarium_client.ShibariumClient._post')
    def test_get_gas_price(self, mock_post):
        """
        Test that get_gas_price correctly converts hex wei to Gwei.
        """
        # 20 Gwei = 20 * 10^9 wei = 0x4A817C800
        mock_post.return_value = "0x4A817C800"
        
        result = self.client.get_gas_price()
        
        self.assertEqual(result, 20.0)
        mock_post.assert_called_with("eth_gasPrice")

    @patch('shibarium_client.ShibariumClient._post')
    def test_get_chain_id(self, mock_post):
        """
        Test that get_chain_id correctly converts hex to integer.
        """
        mock_post.return_value = "0x6D" # 109 in decimal (Mainnet)
        
        result = self.client.get_chain_id()
        
        self.assertEqual(result, 109)
        mock_post.assert_called_with("eth_chainId")

    @patch('shibarium_client.ShibariumClient._post')
    def test_send_raw_transaction(self, mock_post):
        """
        Test that send_raw_transaction correctly submits a signed transaction.
        """
        mock_post.return_value = "0xhash123"
        
        signed_tx = "0x123456"
        result = self.client.send_raw_transaction(signed_tx)
        
        self.assertEqual(result, "0xhash123")
        mock_post.assert_called_with("eth_sendRawTransaction", [signed_tx])

    def test_network_constants(self):
        """
        Validate that the network constants are correct according to specifications.
        """
        self.assertEqual(ShibariumClient.MAINNET_RPC, "https://rpc.shibarium.shib.io")
        self.assertEqual(ShibariumClient.TESTNET_RPC, "https://rpc.puppynet.shib.io")
        self.assertEqual(ShibariumClient.MAINNET_CHAIN_ID, 109)
        self.assertEqual(ShibariumClient.TESTNET_CHAIN_ID, 157)

if __name__ == "__main__":
    unittest.main()
