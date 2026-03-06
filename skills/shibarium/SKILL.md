---
name: Shibarium Blockchain Interaction
description: A comprehensive skill package for interacting with the Shibarium blockchain, including network monitoring, account management, smart contract interaction, and asset bridging.
---

# Shibarium Blockchain Interaction Skill

This skill package provides a robust and easy-to-use interface for interacting with the Shibarium blockchain, both on its Mainnet and Puppynet (testnet). It encapsulates common functionalities required for blockchain development and interaction, adhering to the JSON-RPC standard.

## Network Information

The Shibarium network consists of a Mainnet for live operations and a Puppynet for testing and development. Below are the key details for connecting to these networks.

| Network   | RPC Endpoint                      | Chain ID | Explorer URL                  |
| :-------- | :-------------------------------- | :------- | :---------------------------- |
| Mainnet   | `https://rpc.shibarium.shib.io`   | 109      | `https://shibariumscan.io`    |
| Puppynet  | `https://rpc.puppynet.shib.io`    | 157      | `https://puppyscan.shib.io`   |

## Core Capabilities

This skill package offers the following core capabilities:

*   **Network Monitoring**: Retrieve current block numbers, gas prices, and chain IDs.
*   **Account Management**: Query account balances and transaction counts.
*   **Smart Contract Interaction**: Facilitate interaction with smart contracts (via raw transaction submission).
*   **Asset Bridging**: Provides information and tools to understand asset bridging between Ethereum and Shibarium.

## Usage Guide

To use this skill, you can instantiate the `ShibariumClient` with the desired RPC endpoint. Below is a Python example demonstrating basic usage.

```python
from shibarium_client import ShibariumClient

# Initialize client for Mainnet
client = ShibariumClient("https://rpc.shibarium.shib.io")

# Get current block number
block_number = client.get_block_number()
print(f"Current Block Number: {block_number}")

# Get balance of an address (example address)
address = "0x..."
balance = client.get_balance(address)
print(f"Balance of {address}: {balance} BONE")

# Get transaction count
tx_count = client.get_transaction_count(address)
print(f"Transaction count for {address}: {tx_count}")

# Get gas price
gas_price = client.get_gas_price()
print(f"Current Gas Price: {gas_price} Gwei")

# Get chain ID
chain_id = client.get_chain_id()
print(f"Chain ID: {chain_id}")

# Example of sending a raw transaction (requires a signed transaction hex)
# signed_tx_hex = "0x..."
# try:
#     tx_hash = client.send_raw_transaction(signed_tx_hex)
#     print(f"Transaction sent with hash: {tx_hash}")
# except Exception as e:
#     print(f"Error sending transaction: {e}")
```

## Common RPC Methods Documentation

The `ShibariumClient` class abstracts the following common JSON-RPC methods:

*   `eth_blockNumber`: Returns the number of most recent block.
*   `eth_getBalance`: Returns the balance of the account of a given address.
*   `eth_getTransactionCount`: Returns the number of transactions sent from an address.
*   `eth_gasPrice`: Returns the current price per gas in wei.
*   `eth_chainId`: Returns the chain ID of the current network.
*   `eth_sendRawTransaction`: Submits a signed transaction for broadcast.

## Important Token Addresses (Shibarium Mainnet)

Below are the addresses for key tokens on the Shibarium Mainnet.

| Token | Address                                    |
| :---- | :----------------------------------------- |
| BONE  | `0x0000000000000000000000000000000000001010` |
| SHIB  | `0xC76F4c819D820369Fb2d7C1531aB3Bb18e6fE8d8` |
| LEASH | `0xaB082b8ad96c7f47ED70ED971Ce2116469954cFB` |
| WBONE | `0xC76F4c819D820369Fb2d7C1531aB3Bb18e6fE8d8` |
| USDT  | `0xaB082b8ad96c7f47ED70ED971Ce2116469954cFB` |
| USDC  | `0xf010f12dcA0b96D2d6685bf4dB3dbB4Ad500B6Ad` |
| DAI   | `0x0726959d22361B79e4D50A5D157b044A83eC870d` |
| WBTC  | `0xE984D89fb00D0B44E798A55dc41EA598B0b0899d` |
| XFUND | `0x89dc93C6c12CaE47aCAf4aD9305d7A442C30dBB2` |

## Bridging Assets

Shibarium utilizes bridging mechanisms to transfer assets between the Ethereum mainnet and the Shibarium network. The primary bridges are:

*   **PoS Bridge**: For general asset transfers, leveraging Polygon's Proof-of-Stake bridge technology.
*   **Plasma Bridge**: A more secure, but slower, bridge for critical asset transfers, based on Plasma technology.

For detailed instructions on bridging, please refer to the official Shibarium documentation.

---
Created by: ShibClaw
