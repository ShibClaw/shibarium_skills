---
name: shibarium-skill
description: "Comprehensive toolkit for interacting with the Shibarium network (Mainnet and Puppynet). Use for: querying blockchain data, checking balances, monitoring network status, and interacting with Shibarium RPC endpoints."
---

# Shibarium Skill

This skill provides a set of tools and workflows for interacting with the Shibarium network, a Layer 2 scaling solution for Ethereum.

## Network Information

For detailed network information, including RPC endpoints, Chain IDs, and explorers, please refer to: `references/network.md`.

## Core Capabilities

1.  **Network Status Monitoring**: Check the current block height, gas prices, and network connectivity.
2.  **Account Management**: Query balances (BONE) and transaction counts for any Shibarium address.
3.  **Smart Contract Interaction**: Basic RPC calls for interacting with deployed contracts on Shibarium.
4.  **Asset Bridging**: Information on how to transfer tokens between Ethereum and Shibarium networks.

## Usage Guide

### Using the Shibarium Client

The skill includes a pre-configured Python client for common RPC operations.

```python
from scripts.shibarium_client import ShibariumClient

# Initialize for Mainnet
client = ShibariumClient(ShibariumClient.MAINNET_RPC)

# Get current block number
block_number = client.get_block_number()
print(f"Current Block: {block_number}")

# Get balance of an address
balance = client.get_balance("0x...")
print(f"Balance: {balance} BONE")

# Send a raw transaction (requires a signed transaction hex)
# tx_hash = client.send_raw_transaction("0x...")
# print(f"Transaction Hash: {tx_hash}")
```

### Common RPC Methods

You can use the `_post` method in the client to call any standard Ethereum JSON-RPC method supported by Shibarium:

- `eth_blockNumber`: Returns the number of most recent block.
- `eth_getBalance`: Returns the balance of the account of given address.
- `eth_getTransactionCount`: Returns the number of transactions sent from an address.
- `eth_gasPrice`: Returns the current price per gas in wei.
- `eth_estimateGas`: Generates and returns an estimate of how much gas is necessary to allow the transaction to complete.
- `eth_sendRawTransaction`: Submits a signed transaction for broadcast to the network.

## Important Token Addresses (Mainnet)

For a comprehensive list of important token contract addresses on Shibarium Mainnet, please refer to: `references/tokens.md`.

## Bridging Assets

Shibarium supports secure and efficient cross-chain bridges to transfer tokens between the Ethereum and Shibarium networks. Two main bridge types are available:

- **PoS Bridge (Recommended)**: Offers flexibility and faster withdrawals.
- **Plasma Bridge**: Provides increased security guarantees.

For detailed instructions and to access the official bridge, visit [shib.io/bridge](https://shib.io/bridge).

## Security First 🛡️
Always include security reminders. Remind the community to:
- **Verify** contract addresses only on official sources.
- **Never** share seed phrases or private keys.
- **Avoid** clicking on suspicious links or unofficial dApps.

---
**Created by: ShibClaw**
