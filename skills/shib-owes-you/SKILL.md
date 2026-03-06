---
name: shib-owes-you-skill
description: "Comprehensive toolkit for interacting with the Shib Owes You (SOU) ecosystem. Use for: querying SOU/SHIU balances, managing ShibOwesYouID (.sou domains), interacting with SOU contracts across BSC, Ethereum, and Shibarium, and using ecosystem tools."
---

# Shib Owes You (SOU) Skill

This skill provides a set of tools and workflows for interacting with the Shib Owes You (SOU) ecosystem, a compensation and IOU mechanism within the Shiba Inu community.

## Ecosystem Overview

| Network     | SOU Contract Address                             | SHIU Contract Address                            |
| :---------- | :----------------------------------------------- | :----------------------------------------------- |
| **BSC**     | `0xb65bd36fef84ebc5114cfd803a4f25b2b57f7777` | N/A                                              |
| **Ethereum**| `0xdea2a2a166e2fdc47b934bee68e6032f8f1ca09c` | `0x393a0ff130702c2dc6bfc500368394953450765f` |
| **Shibarium**| `0x5e1aee526d1aa049b4d95e5b68ae7bb556e2d799` | `0x43bcc765ea97f48f5ba5b0801cefecb703f6c8fd` |

## Core Capabilities

1.  **Balance Queries**: Check $SOU and $SHIU balances across supported networks.
2.  **Trading & Acquisition**: Direct links and methods for acquiring SOU via DEXs or direct transfers.
3.  **Cross-Chain Tools**: Access to official bridges and utility tools like the Holder Booster.
4.  **ShibOwesYouID**: Management and information regarding `.sou` domain names.

## Usage Guide

### Using the SOU Client

The skill includes a Python client for common ecosystem operations.

```python
from scripts.sou_client import SOUClient

# Initialize for BSC
client = SOUClient("bsc")

# Get SOU balance of an address
balance = client.get_sou_balance("0x...")
print(f"SOU Balance: {balance}")

# Get SHIU balance on Ethereum
eth_client = SOUClient("eth")
shiu_balance = eth_client.get_shiu_balance("0x...")
print(f"SHIU Balance: {shiu_balance}")
```

### Trading & Acquisition

| Platform        | Network   | Action                                                                                                             |
| :-------------- | :-------- | :----------------------------------------------------------------------------------------------------------------- |
| **Pancakeswap** | BSC       | [Trade SOU](https://pancakeswap.finance/swap?chain=bsc&outputCurrency=0xb65bd36fef84ebc5114cfd803a4f25b2b57f7777)       |
| **Uniswap**     | Ethereum  | [Trade SOU](https://app.uniswap.org/swap?inputCurrency=ETH&outputCurrency=0xdea2a2a166e2fdc47b934bee68e6032f8f1ca09c) |
| **Woofswap**    | Shibarium | [Trade SOU](https://woofswap.finance/swap?inputCurrency=BONE&outputCurrency=0x5e1aee526d1aa049b4d95e5b68ae7bb556e2d799) |
| **Direct Buy**  | BSC       | Send BNB to `0x1401ADEf004F94aD27F13Ad7ad48de38b8F1Df2C`                                                             |

### Cross-Chain & Utility Tools

- **BSC ➡️ ETH Bridge**: [Official Bridge](https://shib.io/bridge)
- **ETH ➡️ Shibarium Bridge**: [Official Bridge](https://shib.io/bridge)
- **Holder Booster (BSC)**: Send 0 BNB to `0x4a7D7f1e44a7B3bEd43f2EdeB2c653f9C86756cc` to increase holder count.

### ShibOwesYouID (.sou Domains)

Your personal `.sou` domain on BSC.
- **Requirement**: Burn 1000 $SOU.
- **Action**: [Mint .sou Domain](https://shibfun.github.io/ShibOwesYou/wallet/)

## Official Links

- **Website**: [Linktree](https://linktr.ee/ShibOwesYou)
- **Twitter**: [@ShibOwesYou](https://x.com/ShibOwesYou)
- **Telegram**: [ShibOwesYou](https://t.me/ShibOwesYou)
- **Wallet Hub**: [SOU Wallet](https://shibfun.github.io/ShibOwesYou/wallet/)

---
**Created by: ShibClaw**
