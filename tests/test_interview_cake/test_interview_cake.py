"""Tests for interview_prep/interview_cake/interview_cake.py
"""

def test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,2.,3.], max_profit=7.0):
    """pytest style test for calc_max_profit
    """
    assert calc_max_profit(prices) == max_profit
    return None

test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,-20.,3.], max_profit=23.)

def test_get_products_of_all_ints_except_at_index(ints=[1,7,3,4], prods=[7*3*4, 1*3*4, 1*7*4, 1*7*3]):
    """pytest style test
    """
    prod_pairs = filter(lambda tup: tup[0] == tup[1], zip(get_products_of_all_ints_except_at_index(ints), prods))
    assert len(prod_pairs) == len(ints)
    return None

test_get_products_of_all_ints_except_at_index()
test_get_products_of_all_ints_except_at_index(ints=[0,0,0], prods=[0,0,0])
test_get_products_of_all_ints_except_at_index(ints=[5], prods=[1])
test_get_products_of_all_ints_except_at_index(ints=[], prods=[])
