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


def get_highest_product(ints):
    """Compute the product of the three largest ints in an array.
    
    Args:
        ints: list
            List of `ints` with `len(ints) >= 3`

    Returns:
        highest_product: int
            Product of the 3 largest ints.

    References:
        ..[1] https://www.interviewcake.com/question/highest-product-of-3
    
    """
    # Check input
    # TODO: raise ValueError
    assert len(ints) >= 3
    # Compute top three ints
    # TODO: make top 3 a default arg
    # TODO: use collections.deque?
    tops = sorted(ints[:3])
    for iint in ints[3:]:
        # TODO: math trick?
        for (idx, top) in enumerate(tops):
            if iint > top:
                tops[idx] = iint
                tops = sorted(tops)
                break
            elif iint == top:
                continue
            else:
                break
    # Compute product
    highest_product = 1
    for top in tops:
        highest_product *= top
    return highest_product
    

