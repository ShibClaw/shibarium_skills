import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add the directory containing sou_client.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from sou_client import SOUClient

class TestSOUClient(unittest.TestCase):

    def setUp(self):
        self.bsc_client = SOUClient("bsc")
        self.eth_client = SOUClient("eth")
        self.shibarium_client = SOUClient("shibarium")

    @patch("requests.post")
    def test_get_token_balance(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        # 0x8ac7230489e80000 in wei is 10000000000000000000 in decimal, which is 10 tokens
        mock_response.json.return_value = {"jsonrpc": "2.0", "id": 1, "result": "0x8ac7230489e80000"}
        mock_post.return_value = mock_response

        balance = self.bsc_client.get_token_balance("0xaddress", self.bsc_client.BSC_SOU)
        self.assertAlmostEqual(balance, 10.0)
        
        # Verify the call
        data = "0x70a08231" + "0xaddress"[2:].lower().zfill(64)
        mock_post.assert_called_with(self.bsc_client.rpc_url, json={
            "jsonrpc": "2.0", "method": "eth_call", "params": [{"to": self.bsc_client.BSC_SOU, "data": data}, "latest"], "id": 1
        })

    def test_constants(self):
        self.assertEqual(SOUClient.BSC_SOU, "0xb65bd36fef84ebc5114cfd803a4f25b2b57f7777")
        self.assertEqual(SOUClient.ETH_SOU, "0xdea2a2a166e2fdc47b934bee68e6032f8f1ca09c")
        self.assertEqual(SOUClient.SHIBARIUM_SOU, "0x5e1aee526d1aa049b4d95e5b68ae7bb556e2d799")
        self.assertEqual(SOUClient.SHIU_ETH, "0x393a0ff130702c2dc6bfc500368394953450765f")
        self.assertEqual(SOUClient.SHIU_SHIBARIUM, "0x43bcc765ea97f48f5ba5b0801cefecb703f6c8fd")

    def test_network_config(self):
        self.assertEqual(self.bsc_client.network, "bsc")
        self.assertEqual(self.eth_client.network, "eth")
        self.assertEqual(self.shibarium_client.network, "shibarium")

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
