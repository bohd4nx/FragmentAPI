import requests

"""
This example demonstrates how to check TON wallet balance 
using the Fragment API by @bohd4nx.

Required parameters:
- Either seed: Wallet seed phrase for authentication
- Or address: TON wallet address
"""

# Check balance using seed phrase
response = requests.post(
    'https://api.bohd4n.dev/api/v1/GetBalance',
    json={
        'seed': ''  # Your wallet seed phrase
    }
)

print(response.json())

# Alternative: Check balance using wallet address
"""
response = requests.post(
    'https://api.bohd4n.dev/api/v1/GetBalance',
    json={
        'address': ''  # TON wallet address
    }
)
"""

# Example: Successful response
"""
SUCCESS (Status code: 200)
{
    "success": true,
    "data": {
        "address": "EQAJgLBs8xqFAqFmswDPVlfrmeoDMGi-1up4HzzqYxqrC1Fs",
        "balance": {
            "value": 12.345,
            "currency": "TON"
        },
        "timestamp": 1747948357
    }
}
"""

# Example: Missing both seed and address
"""
INVALID_REQUEST (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_REQUEST",
        "code": 400,
        "message": "At least one of these fields must be provided: seed, address"
    }
}
"""

# Example: Invalid seed phrase
"""
INVALID_REQUEST (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_REQUEST",
        "code": 400,
        "message": "Invalid seed phrase: Mnemonic length should be equal to 24"
    }
}
"""

# Example: Wallet not found
"""
INVALID_REQUEST (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_REQUEST",
        "code": 400,
        "message": "No wallet found for the provided seed/address"
    }
}
"""

# Example: Internal server error
"""
INTERNAL_ERROR (Status code: 500)
{
    "success": false,
    "error": {
        "type": "INTERNAL_ERROR",
        "code": 500,
        "message": "Failed to retrieve wallet balance"
    }
}
"""
