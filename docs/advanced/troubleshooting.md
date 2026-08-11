# Troubleshooting

When something breaks, start here. Most issues are caused by cookies, session state, or wallet balance.

## Auth/session errors

Symptoms:

- Fragment page hash cannot be extracted,
- bad status loading Fragment pages,
- missing request IDs.

Actions:

- re-login on fragment.com,
- refresh cookies,
- ensure all `stel_*` keys are present.
- verify constructor payload in [Library and Configuration](../getting-started/configuration.md).

**Re-login + fresh cookies solves the majority of auth errors.**

## Cookie extraction errors

Symptoms:

- browser not supported,
- cannot read browser profile,
- required cookies not found.

Actions:

- install `pyfragment[browser]`,
- close locked browser profiles,
- use manual cookies if needed.

## Balance/transaction failures

Symptoms:

- low TON/USDT balance errors,
- broadcast failures,
- duplicate seqno retries.

Actions:

- keep GRAM (ex TON) reserve for fees,
- ensure USDT is on the **Fragment-linked wallet**,
- retry after short delay when seqno collisions happen.
- check operation constraints in Stars/Premium/Ads method pages.

## `confirmed` is `False` after a successful purchase

The transaction already broadcast successfully — `transaction_id` is set and the payment happened. `confirmed` is a
separate, best-effort signal: after broadcasting, the client reports the transaction to Fragment and waits up to ~60s
for Fragment's own backend to acknowledge it. A `False` value just means that acknowledgement didn't arrive in time
(slow Fragment backend, network blip); it does not mean the purchase failed or should be retried. See
[Result Models](../reference/models.md#confirmed).

## Purchase failed and the Fragment invoice was cancelled

If a purchase/giveaway/topup fails *after* Fragment already opened an invoice (e.g. `getBuyStarsLink` errors, KYC is
required, or the wallet fails to sign), the client calls Fragment's `cancelInvoice` before raising, so no dangling
invoice is left on your account. The one exception is a failure during the broadcast itself — in that case the client
can't tell whether the transaction reached the chain, so the invoice is left alone instead of being cancelled out from
under a possibly-successful payment. Check your GRAM (ex TON)/USDT balance and recent transactions if you're unsure.

## SSL-related broadcast failures

If you get SSL-related errors during **TON transaction broadcast** (not Fragment page loading — those use curl_cffi with bundled SSL):

```bash
pip install --upgrade certifi
```

On macOS, also run Python's `Install Certificates.command` if needed.
