def get_max_profit(stock_prices_yesterday):
    """ Return the best profit one could have made from 1 purchase and 1 sale of 1 stock yesterday.
        List index represents time of day.

        Example::

        >>> get_max_profit([10, 7, 5, 8, 11, 9])
        6

    """

    min_price = stock_prices_yesterday[0]
    max_profit = 0

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** TEST PASSED! ***\n"

