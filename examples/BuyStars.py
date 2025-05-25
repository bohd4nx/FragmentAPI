import requests

"""
This example demonstrates how to purchase Telegram Stars 
for a username using the Fragment API by @bohd4nx.

Required parameters:
- username: Target Telegram username to send stars to
- amount: Number of stars to purchase (integer, minimum 50)
- cookies: Fragment authentication cookies
- seed: Wallet seed phrase for purchase transaction
- hash: Fragment account hash
"""

# Send Telegram Stars to a username
response = requests.post(
    'https://api.bohd4n.dev/api/v1/BuyStars',
    json={
        'username': '@bohd4nx',  # Target username
        'amount': 50,  # Amount of stars to send (minimum 50)
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
    "message": "50 stars sent to @bohd4nx. They will receive them within a minute.",
    "data": {
        "transaction_id": "8f7e32a19c5694bb72d7b7b30139902e55e2ffab30c5b37bc36770e25a1e89a1",
        "username": "@bohd4nx",
        "amount": 50,
        "timestamp": 1694792445
    }
}
"""

# Example: Missing required fields
"""
INVALID_REQUEST (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_REQUEST",
        "code": 400,
        "message": "Missing required fields: cookies, seed, hash"
    }
}
"""

# Example: Invalid amount (less than 50)
"""
INVALID_REQUEST (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_REQUEST",
        "code": 400,
        "message": "Stars amount must be at least 50"
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
        "message": "Invalid recipient: User not found or cannot receive stars"
    }
}
"""

# Example: Authentication failed
"""
AUTHENTICATION_FAILED (Status code: 401)
{
    "success": false,
    "error": {
        "type": "AUTHENTICATION_FAILED",
        "code": 401,
        "message": "Authentication failed"
    }
}
"""

# Example: Insufficient funds
"""
INSUFFICIENT_FUNDS (Status code: 402)
{
    "success": false,
    "error": {
        "type": "INSUFFICIENT_FUNDS",
        "code": 402,
        "message": "Insufficient balance: 0.1 TON available, 2.5 TON required"
    }
}
"""

# Example: Blockchain transaction error
"""
BLOCKCHAIN_ERROR (Status code: 502)
{
    "success": false,
    "error": {
        "type": "BLOCKCHAIN_ERROR",
        "code": 502,
        "message": "Transaction rejected by blockchain. Please try again."
    }
}
"""
