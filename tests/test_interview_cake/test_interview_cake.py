"""Tests for interview_prep/interview_cake/interview_cake.py
"""


from __future__ import absolute_import, division, print_function
import sys
sys.path.insert(0, '.')
import interview_prep as ip


def test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,2.,3.], max_profit=7.0):
    """pytest style test for calc_max_profit
    
    """
    assert ip.interview_cake.interview_cake.calc_max_profit(prices) == max_profit
    return None


test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,-20.,3.], max_profit=23.)


def test_get_products_of_all_ints_except_at_index(ints=[1,7,3,4], prods=[7*3*4, 1*3*4, 1*7*4, 1*7*3]):
    """pytest style test
    
    """
    prod_pairs = filter(lambda tup: tup[0] == tup[1],
                        zip(ip.interview_cake.interview_cake.get_products_of_all_ints_except_at_index(ints), prods))
    assert len(prod_pairs) == len(ints)
    return None


test_get_products_of_all_ints_except_at_index()
test_get_products_of_all_ints_except_at_index(ints=[0,0,0], prods=[0,0,0])
test_get_products_of_all_ints_except_at_index(ints=[5], prods=[1])
test_get_products_of_all_ints_except_at_index(ints=[], prods=[])


def test_get_highest_product(ints=[-10,-10,-20,1,3,2], highest_product=600):
    """pytest style test for get_highest_product

    """
    assert ip.interview_cake.interview_cake.get_highest_product(ints=ints) == highest_product
    return None


def test_get_highest_product_2(ints=[-10,-10,-20,1,3,2], highest_product=600):
    """pytest style test for get_highest_product_2

    """
    assert ip.interview_cake.interview_cake.get_highest_product_2(ints=ints) == highest_product
    return None


def test_calc_intersection(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                           rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0},
                           recti={'x':1.0, 'y':1.0, 'width':2.0, 'height':2.0}):
    """pytest style test for calc_intersection

    """
    assert ip.interview_cake.interview_cake.calc_intersection(rect1=rect1, rect2=rect2) == recti
    return None


test_calc_intersection(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                       rect2={'x':3.0, 'y':3.0, 'width':3.0, 'height':3.0},
                       recti={'x':3.0, 'y':3.0, 'width':0.0, 'height':0.0})
test_calc_intersection(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                       rect2={'x':4.0, 'y':0.0, 'width':3.0, 'height':3.0},
                       recti={'x':None, 'y':None, 'width':None, 'height':None})


def test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                             rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0},
                             recti={'x':1.0, 'y':1.0, 'width':2.0, 'height':2.0}):
    """pytest style test for calc_intersection_2

    """
    assert ip.interview_cake.interview_cake.calc_intersection_2(rect1=rect1, rect2=rect2) == recti
    return None


test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         rect2={'x':3.0, 'y':3.0, 'width':3.0, 'height':3.0},
                         recti={'x':3.0, 'y':3.0, 'width':0.0, 'height':0.0})
test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         rect2={'x':4.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         recti={'x':None, 'y':None, 'width':None, 'height':None})


def test_condense_meeting_times(times=[(0, 1), (3, 9), (4, 5), (8, 10), (2, 4)],
                                condensed=[(0, 1), (2, 10)]):
    """pytest style test for condense_meeting_times

    Notes:
        - interviewcake.com problem #4

    """
    assert ip.interview_cake.interview_cake.condense_meeting_times(times=times) == condensed
    return None


test_condense_meeting_times(times=[(1, 10), (2, 6), (3, 5), (7, 9)], condensed=[(1, 10)])
