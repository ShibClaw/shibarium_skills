# Shibarium Blockchain Interaction Skill

This skill package provides a robust and production-ready interface for interacting with the **Shibarium** blockchain. It is designed for seamless integration with AI agents, allowing them to monitor the network, manage accounts, and facilitate asset bridging on both **Mainnet** and **Puppynet**.

## Features List

- **Network Connectivity**: Connect to Shibarium Mainnet and Puppynet via RPC endpoints.
- **Block Information**: Retrieve the latest block number and chain details.
- **Account Management**: Query BONE token balances and transaction counts.
- **Gas Price Oracle**: Get real-time network gas prices in Gwei.
- **Asset Bridging**: Comprehensive information for PoS and Plasma bridging.
- **Unit Tested**: Robust test suite ensures reliability and correctness.

## Installation Instructions

To use this skill package as a standalone module:

1. **Clone the repository**:
   ```shell
   git clone https://github.com/ShibClaw/shibarium_skills.git
   cd shibarium_skills/skills/shibarium
   ```

2. **Install Python dependencies**:
   ```shell
   pip install web3 requests
   ```

## Quick Start Guide

You can instantiate the `ShibariumClient` to interact with the network:

```python
from scripts.shibarium_client import ShibariumClient

# Initialize for Shibarium Mainnet
client = ShibariumClient(ShibariumClient.MAINNET_RPC)

# Fetch current network state
print(f"Current Block: {client.get_block_number()}")
print(f"Gas Price: {client.get_gas_price()} Gwei")
```

## Network Configuration Details

| Constant | Value | Description |
| :--- | :--- | :--- |
| `MAINNET_RPC` | `https://rpc.shibarium.shib.io` | Shibarium Mainnet RPC endpoint |
| `TESTNET_RPC` | `https://rpc.puppynet.shib.io` | Shibarium Puppynet RPC endpoint |
| `MAINNET_CHAIN_ID` | `109` | Shibarium Mainnet Chain ID |
| `TESTNET_CHAIN_ID` | `157` | Shibarium Puppynet Chain ID |

## Testing Instructions

Run the unit tests using the following command:

```shell
python -m unittest tests/test_shibarium_client.py
```

## License Information

This project is licensed under the MIT License.

---
Created by: **ShibClaw**
