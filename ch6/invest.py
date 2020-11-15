# 6.5 Challenge: Track Your Investments


def invest(amount: float, rate: float, years: int) -> None:
    """
    Tracks the growing amount of an investment over time.
    An initial deposit, called the principal amount, is made. Each year,
    the amount increases by a fixed percentage, called the annual rate of return.
    >>> invest(100, .05, 4)
    year 1: $105.00
    year 2: $110.25
    year 3: $115.76
    year 4: $121.55
    """
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")


if __name__ == "__main__":
    invest(100, 0.05, 4)
