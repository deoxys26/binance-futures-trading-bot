import argparse


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Simplified Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run bot in interactive prompt mode"
    )

    parser.add_argument(
        "--symbol",
        required=False,
        help="Trading pair symbol, example: BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=False,
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=False,
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=False,
        type=float,
        help="Order quantity, example: 0.001"
    )

    parser.add_argument(
        "--price",
        required=False,
        type=float,
        help="Price required for LIMIT orders"
    )

    args = parser.parse_args()

    if args.interactive:
        return interactive_prompt()

    normalize_arguments(args)
    validate_arguments(args)

    return args


def interactive_prompt():
    print("\n========== INTERACTIVE TRADING BOT ==========\n")

    symbol = input("Enter symbol, example BTCUSDT: ").strip().upper()

    side = input("Enter side (BUY/SELL): ").strip().upper()

    order_type = input("Enter order type (MARKET/LIMIT): ").strip().upper()

    try:
        quantity = float(input("Enter quantity, example 0.001: ").strip())
    except ValueError:
        raise ValueError("Quantity must be a valid number")

    price = None

    if order_type == "LIMIT":
        try:
            price = float(input("Enter limit price: ").strip())
        except ValueError:
            raise ValueError("Price must be a valid number")

    args = argparse.Namespace(
        symbol=symbol,
        side=side,
        type=order_type,
        quantity=quantity,
        price=price,
        interactive=True
    )

    validate_arguments(args)

    return args


def normalize_arguments(args):
    if args.symbol:
        args.symbol = args.symbol.upper()

    if args.side:
        args.side = args.side.upper()

    if args.type:
        args.type = args.type.upper()


def validate_arguments(args):
    if not args.symbol:
        raise ValueError("Symbol is required. Example: --symbol BTCUSDT")

    if not args.side:
        raise ValueError("Side is required. Use BUY or SELL")

    if args.side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    if not args.type:
        raise ValueError("Order type is required. Use MARKET or LIMIT")

    if args.type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    if args.quantity is None:
        raise ValueError("Quantity is required. Example: --quantity 0.001")

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if args.type == "LIMIT":
        if args.price is None:
            raise ValueError("Price is required for LIMIT orders")

        if args.price <= 0:
            raise ValueError("Price must be greater than 0 for LIMIT orders")

    if args.type == "MARKET" and args.price is not None:
        raise ValueError("Price is not required for MARKET orders")