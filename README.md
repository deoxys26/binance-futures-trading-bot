# Simplified Trading Bot - Binance Futures Testnet

A Python CLI-based trading bot that places orders on **Binance Futures Testnet (USDT-M)**.
The bot supports MARKET and LIMIT orders for both BUY and SELL sides, validates user input, sends signed API requests, prints clean order responses, and logs API requests, responses, and errors.

---

## Features

* Place MARKET orders on Binance Futures Testnet
* Place LIMIT orders on Binance Futures Testnet
* Supports both BUY and SELL sides
* CLI input using `argparse`
* Input validation for:

  * symbol
  * side
  * order type
  * quantity
  * price for LIMIT orders
* Clear terminal output:

  * order request summary
  * order response details
  * success/failure message
* Structured code with separate CLI and API client layers
* Logging of API requests, responses, and errors
* Exception handling for:

  * invalid input
  * Binance API errors
  * network failures
  * timestamp mismatch errors
* Bonus: Enhanced CLI UX with interactive prompt mode

---

## Tech Stack

| Purpose               | Technology                     |
| --------------------- | ------------------------------ |
| Programming Language  | Python                         |
| CLI Handling          | argparse                       |
| API Requests          | requests                       |
| Environment Variables | python-dotenv                  |
| Authentication        | HMAC SHA256 Signature          |
| Logging               | Python logging module          |
| Trading Environment   | Binance Futures Testnet USDT-M |

---

## Project Structure

```text
trading_bot/
│
├── main.py
├── config.py
├── logger.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── client/
│   ├── __init__.py
│   └── binance_client.py
│
└── cli/
    ├── __init__.py
    └── parser.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/trading_bot.git
cd trading_bot
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it:

For Windows PowerShell:

```bash
myenv\Scripts\activate
```

For Mac/Linux:

```bash
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a `.env` file in the root folder and add:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BASE_URL=https://testnet.binancefuture.com
```

API keys should be generated from Binance Futures Testnet/Demo API Management.

Do not upload `.env` to GitHub.

---

## Usage

### MARKET BUY order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### MARKET SELL order

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### LIMIT BUY order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### LIMIT SELL order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000
```

---

## Bonus: Interactive CLI Mode

The project also supports an enhanced CLI UX using interactive mode.

Run:

```bash
python main.py --interactive
```

Example input flow:

```text
Enter symbol, example BTCUSDT: BTCUSDT
Enter side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): MARKET
Enter quantity, example 0.001: 0.001
```

For LIMIT order:

```text
Enter symbol, example BTCUSDT: BTCUSDT
Enter side (BUY/SELL): SELL
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity, example 0.001: 0.001
Enter limit price: 90000
```

---

## Sample Output

### MARKET Order Response

```text
========== ORDER REQUEST SUMMARY ==========
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001
==========================================

========== ORDER RESPONSE ==========
Order ID          : 13672367920
Status            : FILLED
Executed Quantity : 0.0010
Average Price     : 73045.600000
====================================

SUCCESS: Order placed successfully.
```

### LIMIT Order Response

```text
========== ORDER REQUEST SUMMARY ==========
Symbol      : BTCUSDT
Side        : SELL
Order Type  : LIMIT
Quantity    : 0.001
Price       : 90000.0
==========================================

========== ORDER RESPONSE ==========
Order ID          : 13672503985
Status            : NEW
Executed Quantity : 0.0000
Average Price     : 0.00
====================================

SUCCESS: Order placed successfully.
```

---

## Logging

The application logs API requests, responses, and errors in:

```text
logs/trading_bot.log
```

Example log entries:

```text
INFO - API Request: POST https://testnet.binancefuture.com/fapi/v1/order
INFO - Request Params: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}
INFO - API Response Status Code: 200
INFO - Order placed successfully
```

The `logs/` folder is ignored in GitHub using `.gitignore`.

---

## Validation Examples

### Missing price for LIMIT order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001
```

Expected output:

```text
INPUT ERROR: Price is required for LIMIT orders
```

### Price provided for MARKET order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --price 50000
```

Expected output:

```text
INPUT ERROR: Price is not required for MARKET orders
```

### Invalid quantity

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0
```

Expected output:

```text
INPUT ERROR: Quantity must be greater than 0
```

---

## Security Notes

* API keys are stored in `.env`
* `.env` is ignored using `.gitignore`
* API secret is never printed in terminal
* Request signature is not logged
* The bot uses Binance Futures Testnet only

---

##  Requirements Covered

* Place MARKET orders
* Place LIMIT orders
* Support BUY and SELL sides
* Accept CLI input
* Validate user input
* Print order request summary
* Print order response details
* Print success/failure message
* Separate API/client layer and CLI layer
* Log API requests, responses, and errors
* Handle invalid input, API errors, and network failures
* Bonus: Enhanced CLI UX using interactive mode

---

