import requests

"""
This example demonstrates how to purchase Telegram Stars 
for a username using the Fragment API by @bohd4nx.

Required parameters:
- username: Target Telegram username to send stars to
- amount: Number of stars to purchase (integer)
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

# Example: Invalid amount (less than 50)
"""
INVALID_AMOUNT (Status code: 400)
{
    "success": false,
    "error": {
        "type": "INVALID_PARAMS",
        "code": 400,
        "message": "Stars amount must be at least 50"
    }
}
"""

# Example: Blockchain error
"""
BLOCKCHAIN_ERROR (Status code: 402)
{
    "success": false,
    "error": {
        "type": "PAYMENT_REQUIRED",
        "code": 402,
        "message": "Payment error on TON blockchain. Please try again in a minute or contact the developer."
    }
}
"""
