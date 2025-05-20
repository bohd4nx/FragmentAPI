import json

import requests

"""
This example demonstrates how to purchase Telegram Premium
for a username using the Fragment API by @bohd4nx.

Required parameters:
- username: Target Telegram username to send premium to
- duration: Duration in months (integer)
- cookies: Fragment authentication cookies
- seed: Wallet seed phrase for purchase transaction
- hash: Fragment account hash
"""

# Send Telegram Premium to a username
response = requests.post(
    'https://api.bohd4n.dev/api/v1/BuyPremium',
    json={
        'username': '@bohd4nx',  # Target username
        'duration': 3,  # Duration in months (3, 6, or 12)
        'hash': '',  # Fragment account hash
        'cookies': '',  # Your Fragment cookies
        'seed': ''  # Seed phrase for purchase
    }
)

print("Response:", json.dumps(response.json(), indent=4))

# Example: Successful response
"""
SUCCESS (Status code: 200)
{
    "success": true,
    "message": "3 months premium sent to @bohd4nx",
    "data": {
        "transaction_id": "6a9d37f1c32e507b7d4b5c6a90a45c7f8e12d6ba31f98c43e56b9ca7d11e47ab",
        "username": "@bohd4nx",
        "duration": 3,
        "timestamp": 1694792522
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
                "Seed phrase is required. You must provide your wallet seed phrase."
            ]
        }
    }
}
"""

# Example: Missing fragment hash
"""
MISSING_HASH (Status code: 400)
{
    "success": false,
    "error": {
        "code": "INVALID_PARAMS",
        "message": "Missing or invalid parameters in request",
        "details": {
            "missing_fields": [
                "Fragment hash is required. You can find it in your Fragment API calls."
            ]
        }
    }
}
"""

# Example: Missing cookies
"""
MISSING_COOKIES (Status code: 400)
{
    "success": false,
    "error": {
        "code": "INVALID_PARAMS",
        "message": "Missing or invalid parameters in request",
        "details": {
            "missing_fields": [
                "Fragment cookies are required. You must provide valid authentication cookies."
            ]
        }
    }
}
"""

# Example: User not found
"""
USER_NOT_FOUND (Status code: 404)
{
    "success": false,
    "error": {
        "code": "USER_NOT_FOUND",
        "message": "Target username not found",
        "details": {}
    }
}
"""

# Example: Authentication failed
"""
AUTH_FAILED (Status code: 401)
{
    "success": false,
    "error": {
        "code": "AUTH_FAILED",
        "message": "Authentication failed (invalid cookies, seed, or hash)",
        "details": {}
    }
}
"""

# Example: Insufficient funds
"""
INSUFFICIENT_FUNDS (Status code: 402)
{
    "success": false,
    "error": {
        "code": "PAYMENT_REQUIRED",
        "message": "Not enough funds in your Fragment wallet",
        "details": {}
    }
}
"""
