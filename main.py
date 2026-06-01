from config import API_KEY, API_SECRET, BASE_URL, validate_config
from logger import setup_logger
from cli.parser import parse_arguments
from client.balance_client import BinanceFuturesClient


def print_order_summary(args):
    print("\ ORDER REQUEST SUMMARY ")
    print(f"Symbol      : {args.symbol}")
    print(f"Side        : {args.side}")
    print(f"Order Type  : {args.type}")
    print(f"Quantity    : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price       : {args.price}")

    print("-----------------------------\n")


def print_order_response(response):
    print("ORDER RESPONSE ")
    print(f"Order ID          : {response.get('orderId', 'N/A')}")
    print(f"Status            : {response.get('status', 'N/A')}")
    print(f"Executed Quantity : {response.get('executedQty', 'N/A')}")
    print(f"Average Price     : {response.get('avgPrice', 'N/A')}")
    print("------------------------------------\n")


def main():
    logger = setup_logger()

    try:
        validate_config()

        args = parse_arguments()

        print_order_summary(args)

        client = BinanceFuturesClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            base_url=BASE_URL,
            logger=logger
        )

        logger.info("Trading bot started")
        logger.info(
            f"Placing order: symbol={args.symbol}, side={args.side}, "
            f"type={args.type}, quantity={args.quantity}, price={args.price}"
        )

        response = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print_order_response(response)

        print("SUCCESS: Order placed successfully.")
        logger.info("Order placed successfully")

    except ValueError as error:
        print(f"INPUT ERROR: {error}")
        logger.error(f"Input error: {error}")

    except Exception as error:
        print(f"FAILED: {error}")
        print("Check logs/trading_bot.log for more details.")
        logger.error(f"Application error: {error}")


if __name__ == "__main__":
    main()