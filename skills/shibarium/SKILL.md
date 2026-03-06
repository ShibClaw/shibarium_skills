---
name: shibarium-skill
description: "Comprehensive toolkit for interacting with the Shibarium network (Mainnet and Puppynet). Use for: querying blockchain data, checking balances, monitoring network status, and interacting with Shibarium RPC endpoints."
---

# Shibarium Skill

This skill provides a set of tools and workflows for interacting with the Shibarium network, a Layer 2 scaling solution for Ethereum.

## Network Information

| Network | RPC Endpoint | Chain ID | Explorer |
| :--- | :--- | :--- | :--- |
| **Shib Mainnet** | `https://rpc.shibarium.shib.io` | `109` | [shibariumscan.io](https://shibariumscan.io) |
| **Shib Puppynet** | `https://rpc.puppynet.shib.io` | `157` | [puppyscan.shib.io](https://puppyscan.shib.io) |

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

| Token | Address |
| :--- | :--- |
| **BONE (Gas Token)** | `0x0000000000000000000000000000000000001010` |
| **SHIB** | `0xC76F4c819D820369Fb2d7C1531aB3Bb18e6fE8d8` |
| **LEASH** | `0xaB082b8ad96c7f47ED70ED971Ce2116469954cFB` |

## Bridging Assets

Shibarium supports secure and efficient cross-chain bridges to transfer tokens between the Ethereum and Shibarium networks. Two main bridge types are available:

- **PoS Bridge (Recommended)**: Offers flexibility and faster withdrawals.
- **Plasma Bridge**: Provides increased security guarantees.

For detailed instructions and to access the official bridge, visit [shib.io/bridge](https://shib.io/bridge).

---
**Created by: ShibClaw**
