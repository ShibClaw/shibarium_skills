---
name: shib-owes-you-skill
description: "Comprehensive toolkit for interacting with the Shib Owes You (SOU) ecosystem. Use for: querying SOU/SHIU balances, managing ShibOwesYouID (.sou domains), interacting with SOU contracts across BSC, Ethereum, and Shibarium, and using ecosystem tools."
---

# Shib Owes You (SOU) Skill 🐾

This skill provides a set of tools and workflows for interacting with the Shib Owes You (SOU) ecosystem, a compensation and IOU mechanism within the Shiba Inu community.

## Ecosystem Overview

For detailed token contract addresses across BSC, Ethereum, and Shibarium, please refer to: `references/tokens.md`.

For official links, trading platforms, and utility tools, please refer to: `references/tools.md`.

## Core Capabilities

1.  **Balance Queries**: Check $SOU and $SHIU balances across supported networks, including Smart Wallet balances.
2.  **Trading & Acquisition**: Access to DEXs and direct purchase methods.
3.  **Cross-Chain Tools**: Access to official bridges and utility tools like the Holder Booster.
4.  **ShibOwesYouID**: Management and information regarding `.sou` domain names and numeric IDs.
5.  **Smart Contract Wallets**: Support for SOU Smart Contract Wallets on BSC, including ID resolution and wallet management.

## Usage Guide

### Using the SOU Client

The skill includes a Python client for common ecosystem operations, including Smart Wallet support.

```python
from scripts.sou_client import SOUClient

# Initialize for BSC
client = SOUClient("bsc")

# Get SOU balance of an address (EOA)
balance = client.get_sou_balance("0x...")
print(f"SOU Balance: {balance}")

# --- Smart Wallet Features (BSC) ---

# Get Smart Wallet address from an EOA owner
smart_wallet = client.get_smart_wallet_address("0x...")
print(f"Smart Wallet: {smart_wallet}")

# Resolve a numeric ID to its Smart Wallet address
id_wallet = client.resolve_id_to_wallet("123")
print(f"Wallet for ID 123: {id_wallet}")
```

### ShibOwesYouID (.sou Domains & IDs)

Your personal Web3 identity on BSC.
- **Requirement**: Burn 1000 $SOU for a `.sou` domain.
- **Action**: [Manage ShibOwesYouID](https://shibfun.github.io/ShibOwesYou/DSOU/)
- **Resolution**: Supports both `.sou` domain names and numeric IDs.

## Security First 🛡️
Always include security reminders. Remind the community to:
- **Verify** contract addresses only on official sources.
- **Never** share seed phrases or private keys.
- **Avoid** clicking on suspicious links or unofficial dApps.

---
**Created by: ShibClaw**
