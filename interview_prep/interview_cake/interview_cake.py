"""My iterations of answers to questions on Interview Cake.
"""

def calc_max_profit(prices):
    """Compute maximum profit.
    
    Args:
        prices: array_like
            Iterable with prices. Index is number of minutes since beginning of trading day.
    
    Returns:
        max_profit: float
            Maximum profit possible from buying then selling during `prices`.
            
    References:
        .. [1] https://www.interviewcake.com/question/stock-price
    
    """
    # TODO: use indices as internal check that program is working.
    (min_price, max_profit) = (prices[0], 0.0)
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def get_products_of_all_ints_except_at_index(ints):
    """Get product of all ints save one for each idx.

    Args:
        ints: list of int
        List of `int` factors.

    Returns:
        prods: list of int
        List of `int` products.

    References:
        ..[1] https://www.interviewcake.com/question/product-of-other-numbers
    
    """
    idxs = xrange(len(ints))
    prods = [1]*len(ints)
    prod = 1
    for idx in idxs:
        prods[idx] = prod
        prod *= ints[idx]
    prod = 1
    for idx in reversed(idxs):
        prods[idx] *= prod
        prod *= ints[idx]
    return prods

