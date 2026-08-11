# Changelog

All notable changes to pyfragment are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Calendar Versioning](https://calver.org/) (`YYYY.MINOR.MICRO`).

---

## [Unreleased]

### Fixed

- Transaction balance validation now reserves GRAM for network fees instead of allowing a payment to consume the entire available balance.

## [2026.3.2] — 2026-06-16

### Added

- Added `ApiProvider` enum with `TONAPI` (tonconsole.com, default) and `TONCENTER` (t.me/toncenter) values.
- Added `api_provider` parameter to `FragmentClient` — select the blockchain API provider at init time (`"tonapi"` or `"toncenter"`).
- Both providers accept `api_key` with the same interface; the correct `tonutils` client is selected automatically.

- New `AlreadySubscribedError` exception for Premium purchase flows when Fragment returns: `This account is already subscribed to Telegram Premium.`
- New `UserNotFoundError.NOT_A_USER` message for when Fragment returns: `Please enter a username assigned to a user.` (e.g. when the username belongs to a channel or bot).
- Added `WalletVersion.HighloadV2` and `WalletVersion.HighloadV3R1` to `WalletVersion`

### Changed

- Updated purchase and giveaway flow state nonces (`dh`) to use nonce-like dynamic values with a wider integer range.
- Stars and Premium giveaway flows now include explicit price update steps before init requests:
  - `updateStarsGiveawayPrices`
  - `updatePremiumGiveawayPrices`
- Updated `DEVICE_INFO` fingerprint: Tonkeeper `appVersion` -> `26.05.0`.
- Updated client docstrings and purchase examples to document all supported payment methods.

### Renamed — TON -> GRAM (ex TON)

The TON blockchain has been rebranded to **GRAM (ex TON)**. All identifiers, messages, and documentation have been updated accordingly.

**Public API**

- `FragmentClient.topup_ton()` → `topup_gram()`
- `PaymentMethod.TON` → `PaymentMethod.GRAM`
- `PaymentMethod.USDT_TON` → `PaymentMethod.USDT_GRAM`
- `WalletInfo.ton_balance` → `WalletInfo.gram_balance`

**Constants**

- `TON_TOPUP_MIN` / `TON_TOPUP_MAX` → `GRAM_TOPUP_MIN` / `GRAM_TOPUP_MAX`
- `MIN_TON_BALANCE` → `MIN_GRAM_BALANCE`
- `USDT_TON_MASTER_ADDRESS` → `USDT_GRAM_MASTER_ADDRESS`

**Exceptions**

- `ConfigurationError.INVALID_TON_AMOUNT` → `INVALID_GRAM_AMOUNT`
- `WalletError.LOW_TON_BALANCE` → `LOW_GRAM_BALANCE`
- `WalletError.TON_BALANCE_CHECK_FAILED` → `GRAM_BALANCE_CHECK_FAILED`

**Internals**

- `pyfragment/core/constants/ton.py` → `gram.py`
- `check_ton_payment_balance()` → `check_gram_payment_balance()`

---

## [2026.3.1] — 2026-05-29

### Added

- Python 3.13 and 3.14 are now officially supported and included in the CI test matrix and PyPI classifiers.
- `WalletVersion` is now exported from the top-level `pyfragment` package.

### Changed

- `process_transaction` (internal) refactored into focused subfunctions: `_extract_message`, `_check_payment_balances`, `_broadcast_with_retry`.
- `raw_api_call()` moved from `FragmentClient` into `pyfragment.domains.base` and exposed as a standalone helper.
- `tonapi` domain internal helpers removed from public `__init__.py` exports; only `TonapiService` is exported.
- README rewritten with badges, structured sections, and complete usage examples.
- Added `CONTRIBUTING.md` and `SECURITY.md`.

### Fixed

- CI: `mypy` now runs with `--explicit-package-bases` to avoid false-positive import errors.
- CI: `pip` dependency cache enabled to speed up workflow runs.
- CI: `warn_unused_ignores` suppressed for `pyfragment.core.cookies` to handle the optional `rookiepy` dependency correctly across environments where the package may or may not be installed.
