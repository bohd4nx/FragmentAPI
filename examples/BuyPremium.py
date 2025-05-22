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

print(response.json())

# Example: Successful response
"""
SUCCESS (Status code: 200)
{
    "success": true,
    "message": "3 months premium sent to @bohd4nx. They will receive it within a minute.",
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
        "type": "INVALID_PARAMS",
        "code": 400,
        "message": "Missing required fields: seed"
    }
}
"""

# Example: Missing fragment hash
"""
MISSING_HASH (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_PARAMS",
        "code": 400,
        "message": "Missing required fields: hash"
    }
}
"""

# Example: Missing cookies
"""
MISSING_COOKIES (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_PARAMS",
        "code": 400,
        "message": "Missing required fields: cookies"
    }
}
"""

# Example: User not found
"""
USER_NOT_FOUND (Status code: 404)
{
    "success": false,
    "error": {
        "type": "USER_NOT_FOUND",
        "code": 404,
        "message": "Invalid recipient: Recipient not found"
    }
}
"""

# Example: Authentication failed
"""
AUTH_FAILED (Status code: 401)
{
    "success": false,
    "error": {
        "type": "AUTH_FAILED",
        "code": 401,
        "message": "Authentication failed (invalid cookies, seed, or hash)"
    }
}
"""

# Example: Insufficient funds
"""
INSUFFICIENT_FUNDS (Status code: 402)
{
    "success": false,
    "error": {
        "type": "PAYMENT_REQUIRED",
        "code": 402,
        "message": "Insufficient balance: 0.1 TON available, 9.17 TON required"
    }
}
"""
