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
| Balance | `https://api.bohd4n.dev/api/v1/GetBalance` | Check TON wallet balance           |

## Authentication

To use the API, you'll need:

1. **Fragment cookies** - Your authentication cookies from Fragment
2. **Seed phrase** - Your wallet seed phrase for transaction signing
3. **Fragment hash** - Your Fragment API hash

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
        'seed': ''  # TON wallet seed phrase (W5)
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
        'seed': ''  # TON wallet seed phrase (W5)
    }
)

print("Response:", json.dumps(response.json(), indent=4))
```

### Python Example (Check Balance)

```python
import requests
import json

response = requests.post(
    'https://api.bohd4n.dev/api/v1/GetBalance',
    json={
        'seed': ''  # TON wallet seed phrase (W5)
        # Alternatively, you can use 'address' instead of 'seed'
    }
)

print("Response:", json.dumps(response.json(), indent=4))
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
