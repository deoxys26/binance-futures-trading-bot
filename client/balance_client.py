import time
import hmac
import hashlib
from urllib.parse import urlencode

import requests


class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, base_url, logger):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url.rstrip("/")
        self.logger = logger

    def _generate_signature(self, params):
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return signature

    def _send_signed_request(self, method, endpoint, params):
        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._generate_signature(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        url = self.base_url + endpoint

        self.logger.info(f"API Request: {method} {url}")
        safe_params = params.copy()
        safe_params.pop("signature", None)
        self.logger.info(f"Request Params: {safe_params}")

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                timeout=10
            )

            try:
                data = response.json()
            except ValueError:
                data = {"raw_response": response.text}

            self.logger.info(f"API Response Status Code: {response.status_code}")
            self.logger.info(f"API Response Body: {data}")

            if response.status_code >= 400:
                error_message = data.get("msg", "Unknown Binance API error")
                raise Exception(f"Binance API Error: {error_message}")

            return data

        except requests.exceptions.Timeout:
            self.logger.error("Network Error: Request timed out")
            raise Exception("Network error: request timed out")

        except requests.exceptions.ConnectionError:
            self.logger.error("Network Error: Failed to connect to Binance")
            raise Exception("Network error: failed to connect to Binance")

        except requests.exceptions.RequestException as error:
            self.logger.error(f"Network Error: {str(error)}")
            raise Exception(f"Network error: {str(error)}")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "newOrderRespType": "RESULT"
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self._send_signed_request(
            method="POST",
            endpoint=endpoint,
            params=params
        )