from functools import lru_cache
import logging
import math
import sys
import typing

LOG_LEVEL = logging.INFO
# Allowed coins denominations from greater to lower:
COINS_DENOMINATIONS_IN_CENTS = [
    200,  # 2 Euros
    100,  # 1 Euro
    50,   # 50 Cents
    20,   # 20 Cents
    10,   # 10 Cents
    5,    # 5 Cents
    2,    # 2 Cents
    1     # 1 Cent
]


def usage(sys_argv) -> None:
    logging.info("Coins Calculator:")
    logging.info("Usage:")
    logging.info(f"\tpython {sys_argv[0]} <Amount in Euros>")
    logging.info(f"\tExample:")
    logging.info(f"\t\tpython {sys_argv[0]} 2.54")


@lru_cache(maxsize=128)
def convert_cents_to_euro(cents: int) -> float:
    return cents / 100


def convert_amount_in_cents_to_coins(amount: int) -> typing.List[float]:
    """Given an euro amount in cents, determines the minimal amounts of coins required to represent it"""

    logging.debug(f"convert_amount_in_cents_to_coins(amount={amount})")
    coins_list_in_cents = []
    # Iterate from coins of greater domination to coins of lower denomination:
    for coin_denomination in COINS_DENOMINATIONS_IN_CENTS:
        if coin_denomination > amount:
            # This coin_denomination shouldn't be included in the resulting bag of coins:
            continue

        if coin_denomination == amount:
            coins_list_in_cents.append(convert_cents_to_euro(coin_denomination))
            # If we're here is because we have fully converted the initial amount to coins:
            break

        # amount is greater than coin_denomination. Let's figure-out how many coins of this denomination
        # are required. The result of call divmod(a, b) would be a tuple with the result of (a // b, a % b):
        count_of_coins, amount = divmod(amount, coin_denomination)
        for _ in range(count_of_coins):
            coins_list_in_cents.append(convert_cents_to_euro(coin_denomination))

        if amount == 0:
            # There's no need to continue reviewing coins with a lower denomination, because we have
            # fully converted the initial amount to coins:
            break

    return coins_list_in_cents


def get_euro_coins(euros_amount):
    logging.debug(f"get_euro_coins(euros_amount={euros_amount})")
    # Truncate amount to at most 2 decimal places without round. Example: 5.6789 to 5.67:
    euros_amount = truncate(float(euros_amount), 2)
    # Convert from Euros to Cents. Example: 2.34€ = 234¢:
    euros_amount_in_cents = int(euros_amount * 100)

    coins_list_in_cents = convert_amount_in_cents_to_coins(euros_amount_in_cents)
    logging.debug(f"coins_list_in_cents={coins_list_in_cents}")

    return coins_list_in_cents


def truncate(number: float, decimals: int = 0) -> float:
    """Return a value truncated to a specific number of decimal places"""

    logging.debug(f"truncate(number={number}, decimals={decimals})")
    if not isinstance(decimals, int):
        raise TypeError("Decimal places must be an integer.")

    if decimals < 0:
        raise TypeError("Decimal places has to be 0 or more.")

    if decimals == 0:
        return math.trunc(number)

    correction_factor = 10.0 ** decimals
    return math.trunc(number * correction_factor) / correction_factor


def main(sys_argv) -> typing.Optional[typing.List[float]]:
    info_message_format = "%(message)s"
    debug_message_format = "%(asctime)s: %(message)s"
    if LOG_LEVEL == logging.DEBUG:
        logging.basicConfig(format=debug_message_format, level=LOG_LEVEL, datefmt="%H:%M:%S")
    else:
        logging.basicConfig(format=info_message_format, level=LOG_LEVEL)

    logging.debug(f"main(sys_argv={sys_argv})")
    if len(sys_argv) < 2:
        logging.info("Invalid arguments. Is expected one argument and none was supplied")
        usage(sys_argv)
        result = None
    else:
        euros_amount = sys_argv[1]
        if not euros_amount.replace('.', '', 1).isdigit():
            logging.info("Invalid arguments. Is expected one argument in the format: 2.54")
            usage(sys_argv)
            result = None
        else:
            result = get_euro_coins(euros_amount)

    logging.info(result)
    return result


if __name__ == "__main__":
    main(sys.argv)
