<div align="center">

# Fragment Stars & Premium API

A powerful API service for programmatically sending Telegram Stars and gifting Premium subscriptions through Fragment.

[![API Status](https://img.shields.io/badge/API-Online-brightgreen)](https://api.bohd4n.dev)
[![Documentation](https://img.shields.io/badge/Docs-Available-blue)](https://fragment.bohd4n.dev/docs)

</div>

## API Endpoints

The API is publicly available at **[api.bohd4n.dev](https://api.bohd4n.dev)** with the following endpoints:

| Service | Endpoint                                   | Description                        |
|---------|--------------------------------------------|------------------------------------|
| Stars   | `https://api.bohd4n.dev/api/v1/BuyStars`   | Send stars to Telegram usernames   |
| Premium | `https://api.bohd4n.dev/api/v1/BuyPremium` | Gift premium to Telegram usernames |

## Authentication

To use the API, you'll need:

1. **Fragment cookies**  - Your authentication cookies from Fragment
2. **Seed phrase**  - Your wallet seed phrase for transaction signing
3. **Fragment hash** - Your Fragment API hash

## Sending Stars

### Request

```http
POST https://api.bohd4n.dev/api/v1/BuyStars
Content-Type: application/json

{
  "username": "@username",
  "amount": 50,
  "cookies": "your_fragment_cookies",
  "seed": "your_seed_phrase",
  "hash": "your_fragment_hash"
}
```

### Parameters

| Parameter | Type   | Required | Description                                |
|-----------|--------|----------|--------------------------------------------|
| username  | string | Yes      | Target Telegram username                   |
| amount    | int    | Yes      | Amount of stars to send (must be positive) |
| cookies   | string | Yes      | Your Fragment cookies                      |
| seed      | string | Yes      | Your wallet seed phrase                    |
| hash      | string | Yes      | Your Fragment API hash                     |

### Success Response

```json
{
  "success": true,
  "message": "50 stars sent to @username",
  "data": {
    "transaction_id": "8f7e32a19c5694bb72d7b7b30139902e55e2ffab30c5b37bc36770e25a1e89a1",
    "username": "@username",
    "amount": 50,
    "timestamp": 1694792445
  }
}
```

## Gifting Premium

### Request

```http
POST https://api.bohd4n.dev/api/v1/BuyPremium
Content-Type: application/json

{
  "username": "@username",
  "duration": 3,
  "cookies": "your_fragment_cookies",
  "seed": "your_seed_phrase",
  "hash": "your_fragment_hash"
}
```

### Parameters

| Parameter | Type   | Required | Description                      |
|-----------|--------|----------|----------------------------------|
| username  | string | Yes      | Target Telegram username         |
| duration  | int    | Yes      | Duration in months (3, 6, or 12) |
| cookies   | string | Yes      | Your Fragment cookies            |
| seed      | string | Yes      | Your wallet seed phrase          |
| hash      | string | Yes      | Your Fragment API hash           |

### Success Response

```json
{
  "success": true,
  "message": "3 months premium sent to @username",
  "data": {
    "transaction_id": "6a9d37f1c32e507b7d4b5c6a90a45c7f8e12d6ba31f98c43e56b9ca7d11e47ab",
    "username": "@username",
    "duration": 3,
    "timestamp": 1694792522
  }
}
```

## Error Responses

All error responses follow this format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  }
}
```

### Error Codes

| Status Code | Error Code       | Description                                            |
|-------------|------------------|--------------------------------------------------------|
| 400         | INVALID_PARAMS   | Invalid or missing request parameters                  |
| 401         | AUTH_FAILED      | Authentication failed (invalid cookies, seed, or hash) |
| 402         | PAYMENT_REQUIRED | Not enough funds in your Fragment wallet               |
| 404         | USER_NOT_FOUND   | Target username not found                              |
| 500         | SERVER_ERROR     | Internal server error                                  |

## Example Usage

### Python Example (Stars)

```python
import requests
import json

response = requests.post(
    'https://api.bohd4n.dev/api/v1/BuyStars',
    json={
        'username': '@username',  # Target username
        'amount': 50,  # Amount of stars to send
        'hash': '',  # Fragment account hash
        'cookies': '',  # Your Fragment cookies
        'seed': ''  # Seed phrase for purchase
    }
)

print("Response:", json.dumps(response.json(), indent=4))
```

### Python Example (Premium)

```python
import requests
import json

response = requests.post(
    'https://api.bohd4n.dev/api/v1/BuyPremium',
    json={
        'username': '@username',  # Target username
        'duration': 3,  # Duration in months (3, 6, or 12)
        'hash': '',  # Fragment account hash
        'cookies': '',  # Your Fragment cookies
        'seed': ''  # Seed phrase for purchase
    }
)

print("Response:", json.dumps(response.json(), indent=4))
```

## Notes

- The API handles all Fragment interactions and TON blockchain transactions
- Successful transactions return a transaction ID that can be used for tracking
- The timestamp in responses is in Unix time format (seconds since January 1, 1970)
- Rate limits may apply to prevent abuse

## Security

- Your seed phrase and private keys are never stored on our servers
- All API requests should be made over HTTPS
- Keep your Fragment cookies and seed phrase secure

## Support

For support or feature requests, contact [@bohd4nx](https://t.me/bohd4nx) on Telegram.

---
<div align="center">
    <h4>Built with ❤️ by <a href="https://t.me/bohd4nx" target="_blank">Bohdan</a></h4>
</div>
