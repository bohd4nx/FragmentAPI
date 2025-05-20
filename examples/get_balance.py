import json
import requests

"""
This example demonstrates how to check TON wallet balance 
using the Fragment API by @bohd4nx.

Required parameters:
- seed: Wallet seed phrase for authentication
"""

# Get wallet balance information
response = requests.post(
    'https://api.bohd4n.dev/api/v1/Balance',
    json={
        'seed': ''  # Your wallet seed phrase
    }
)

print("Response:", json.dumps(response.json(), indent=4))

# Example: Successful response
"""
SUCCESS (Status code: 200)
{
    "success": true,
    "message": "Wallet balance retrieved successfully",
    "data": {
        "address": "UQBvW8Z5Z81QS4V6UJCHxQKSXmKgVUvP3HLwKyL9nKPC1YY9",
        "balances": {
            "ton": 123.456789,
            "jettons": [
                {
                    "name": "Notcoin",
                    "symbol": "NOT",
                    "balance": 12345.67,
                    "price_usd": 0.00952,
                    "value_usd": 117.53
                },
                {
                    "name": "Tegro",
                    "symbol": "TGR",
                    "balance": 42.0,
                    "price_usd": 0.35,
                    "value_usd": 14.7
                }
            ]
        },
        "total_usd_value": 385.22
    }
}
"""

# Example: Missing seed phrase
"""
MISSING_SEED (Status code: 400)
{
    "success": false,
    "error": {
        "code": "INVALID_PARAMS",
        "message": "Missing or invalid parameters in request",
        "details": {
            "missing_fields": [
                "Seed phrase is required"
            ]
        }
    }
}
"""
