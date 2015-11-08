#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Pytests for interview_prep/interview_prep/interview_cake.py

"""


# Import standard packages.
import collections
import os
import sys
# Import installed packages.
import pytest
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.interview_cake as ic


def test_q1_calc_max_profit(
    prices:list=[5.0, 4.0, 5.0, 3.0, 6.0, 5.0, 9.0, 8.0, 10.0, 2.0, 3.0],
    ref_max_profit:float=7.0) -> None:
    r"""Pytest for q1_calc_max_profit.
    
    """
    test_max_profit = ic.q1_calc_max_profit(prices)
    assert ref_max_profit == test_max_profit
    return None


def test_q1_calc_max_profit_suppl() -> None:
    r"""Supplemental pytests for q1_calc_max_profit.
    
    """
    with pytest.raises(ValueError):
        ic.q1_calc_max_profit(prices='123')
    test_q1_calc_max_profit(
        prices=[5.0, 4.0, 5.0, 3.0, 6.0, 5.0, 9.0, 8.0, 10.0, -20.0, 3.0],
        ref_max_profit=23.0)
    return None


def test_q2_get_products_of_all_ints_except_at_index(
    ints:list=[1, 7, 3, 4],
    ref_prods:list=[7*3*4, 1*3*4, 1*7*4, 1*7*3]) -> None:
    """Pytest for q2_get_products_of_all_ints_except_at_index.
    
    """
    test_prods = ic.q2_get_products_of_all_ints_except_at_index(ints)
    assert ref_prods == test_prods
    return None


def test_q2_get_products_of_all_ints_except_at_index_suppl() -> None:
    r"""Supplemental tests for q2_get_products_of_all_ints_except_at_index.
    
    """
    with pytest.raises(ValueError):
        ic.q2_get_products_of_all_ints_except_at_index(ints='123')
    test_q2_get_products_of_all_ints_except_at_index(
        ints=[0, 0, 0], ref_prods=[0, 0, 0])
    test_q2_get_products_of_all_ints_except_at_index(
        ints=[5], ref_prods=[1])
    test_q2_get_products_of_all_ints_except_at_index(
        ints=[], ref_prods=[])
    return None


def test_q3_calc_highest_product_of_3(
    ints:list=[-10, -10, 1, 3, 2],
    ref_prod:int=300) -> None:
    r"""Pytest for q3_calc_highest_product_of_3.

    """
    test_prod = ic.q3_calc_highest_product_of_3(ints=ints)
    assert ref_prod == test_prod
    return None


def test_q3_calc_highest_product_of_3_suppl() -> None:
    r"""Supplemental pytests for q3_calc_highest_product_of_3.
    
    """
    with pytest.raises(ValueError):
        ic.q3_calc_highest_product_of_3(ints=[1, 2])
        ic.q3_calc_highest_product_of_3(ints='123')
    test_q3_calc_highest_product_of_3(ints=[1, 10, -5, 1, -100], ref_prod=5000)
    test_q3_calc_highest_product_of_3(ints=[0, 0, 0], ref_prod=0)
    test_q3_calc_highest_product_of_3(ints=[0, 0, 0, 1], ref_prod=0)
    return None


def test_q4_condense_meeting_times(
    times:list=[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)],
    ref_condensed:list=[(0, 1), (3, 8), (9, 12)]) -> None:
    r"""Pytest for q4_condense_meeting_times.

    """
    test_condensed = ic.q4_condense_meeting_times(times=times)
    assert ref_condensed == test_condensed
    return None


def test_q4_condense_meeting_times_suppl() -> None:
    r"""Supplemental pytests for q4_condense_meeting_times.
    
    """
    with pytest.raises(ValueError):
        ic.q4_condense_meeting_times(times='[(1, 10), (2, 6)]')
    test_q4_condense_meeting_times(
        times=[(1, 2), (2, 3)],
        ref_condensed=[(1, 3)])
    test_q4_condense_meeting_times(
        times=[(1, 5), (2, 3)],
        ref_condensed=[(1, 5)])
    test_q4_condense_meeting_times(
        times=[(1, 10), (2, 6), (3, 5), (7, 9)],
        ref_condensed=[(1, 10)])
    test_q4_condense_meeting_times(
        times=[(0, 1), (0, 1), (0, 1)],
        ref_condensed=[(0, 1)])
    test_q4_condense_meeting_times(
        times=[(0, 1), (1, 2), (2, 3)],
        ref_condensed=[(0, 3)])
    test_q4_condense_meeting_times(
        times=[(2, 3), (1, 2), (0, 1)],
        ref_condensed=[(0, 3)])
    test_q4_condense_meeting_times(
        times=[(9, 11), (5, 7), (1, 3), (2, 10)],
        ref_condensed=[(1, 11)])
    return None


def test_q5_count_combinations(
    amount:int=4,
    denoms:list=[1, 2, 3],
    ref_ncombos:int=4) -> None:
    r"""Pytest for q5_count_combinations.
    
    """
    test_ncombos = ic.q5_count_combinations(amount=amount, denoms=denoms)
    assert ref_ncombos == test_ncombos
    return None


def test_q5_count_combinations_suppl() -> None:
    r"""Supplemental pytests for q5_count_combinations.
    
    """
    with pytest.raises(ValueError):
        ic.q5_count_combinations(amount=4.0, denoms=[1, 2, 3])
        ic.q5_count_combinations(amount=4.0, denoms='[1, 2, 3]')
        ic.q5_count_combinations(amount=0, denoms=[1, 2, 3])
        ic.q5_count_combinations(amount=4, denoms=[])
        ic.q5_count_combinations(amount=0, denoms=[1, 2.0, 3])
        ic.q5_count_combinations(amount=0, denoms=[1, 0, 3])
    test_q5_count_combinations(amount=5, denoms=[1, 3, 5], ref_ncombos=3)
    return None


def test_q6_calc_intersection(
    rect1:dict={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
    rect2:dict={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0},
    ref_recti:dict={'x':1.0, 'y':1.0, 'width':2.0, 'height':2.0}) -> None:
    r"""Pytest for q6_calc_intersection.

    """
    test_recti = ic.q6_calc_intersection(rect1=rect1, rect2=rect2)
    assert ref_recti == test_recti
    return None


def test_q6_calc_intersection_suppl() -> None:
    r"""Supplemental pytests for q6_test_calc_intersection.
    
    """
    with pytest.raises(ValueError):
        ic.q6_calc_intersection(
            rect1="{'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0}",
            rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0})
        ic.q6_calc_intersection(
            rect1=[0.0, 0.0, 3.0, 3.0],
            rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0})
    test_q6_calc_intersection(
        rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
        rect2={'x':3.0, 'y':3.0, 'width':3.0, 'height':3.0},
        ref_recti={'x':3.0, 'y':3.0, 'width':0.0, 'height':0.0})
    test_q6_calc_intersection(
        rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
        rect2={'x':4.0, 'y':0.0, 'width':3.0, 'height':3.0},
        ref_recti={'x':None, 'y':None, 'width':None, 'height':None})
    return None


def test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                             rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0},
                             recti={'x':1.0, 'y':1.0, 'width':2.0, 'height':2.0}):
    """pytest style test for calc_intersection_2

    """
    assert ic.calc_intersection_2(rect1=rect1, rect2=rect2) == recti
    return None


test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         rect2={'x':3.0, 'y':3.0, 'width':3.0, 'height':3.0},
                         recti={'x':3.0, 'y':3.0, 'width':0.0, 'height':0.0})
test_calc_intersection_2(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         rect2={'x':4.0, 'y':0.0, 'width':3.0, 'height':3.0},
                         recti={'x':None, 'y':None, 'width':None, 'height':None})


def test_TempTracker(temps=[1, 2, 3, 3], temps2=4, ctr=collections.Counter([1, 2, 3, 3])):
    """pytest style test for class TempTracker

    """
    temptracker = ic.TempTracker(temps=temps)
    assert temptracker.ctr == ctr
    temptracker.insert(temps=temps2)
    ctr.update([temps2])
    assert temptracker.ctr == ctr
    assert temptracker.get_max() == max(ctr)
    assert temptracker.get_min() == min(ctr)
    assert temptracker.get_mean() == sum(ctr.elements()) / sum(ctr.values())
    assert temptracker.get_mode() == ctr.most_common(1)
    return None


def test_is_leaf_node(node=['a'], is_leaf=True):
    """pytest style test for is_leaf

    """
    assert ic.is_leaf_node(node=node) == is_leaf
    return None


test_is_leaf_node(node=['a', 'b'], is_leaf=False)


def test_get_younger_sibling_or_parent(tree=['a', ['b', ['c'], ['d']], ['e']], path=[1, 1],
                                       node_sp=['d'], path_sp=[1, 2], rel_sp='younger_sibling'):
    """pytest style test for get_younger_sibling_or_parent
    
    """
    assert ic.get_younger_sibling_or_parent(tree=tree, path=path) == \
        (node_sp, path_sp, rel_sp)
    try: ic.get_younger_sibling_or_parent(tree=tree, path=[])
    except ValueError: pass
    return None


test_get_younger_sibling_or_parent(tree=['a', ['b', ['c'], ['d']], ['e']], path=[1, 2],
                                   node_sp=['b', ['c'], ['d']], path_sp=[1], rel_sp='parent')
test_get_younger_sibling_or_parent(tree=['a', ['b', ['c'], ['d']], ['e']], path=[1],
                                   node_sp=['e'], path_sp=[2], rel_sp='younger_sibling')
test_get_younger_sibling_or_parent(tree=['a', ['b', ['c'], ['d']], ['e']], path=[2],
                                   node_sp=['a', ['b', ['c'], ['d']], ['e']], path_sp=[], rel_sp='parent')


def test_is_super_balanced(tree=['a', ['b', ['c'], ['d']], ['e', ['f', ['g']]]], is_super=True):
    """pytest style test for is_super_balanced

    """
    assert ic.is_super_balanced(tree=tree) == is_super
    return None


test_is_super_balanced(tree=['a', ['b', ['c'], ['d']], ['e', ['f', ['g', ['h']]]]], is_super=False)


def test_get_next_path(current_path=[1, 2, 2], next_path=[2, 1, 1]):
    """pytest style test for _get_next_path.

    """
    assert ic._get_next_path(current_path=current_path) == next_path
    return None


test_get_next_path(current_path=[2, 2, 2], next_path=[1, 1, 1, 1])


def test_get_next_node_path_values(
    bin_tree=[50, [30, [10, None, None], [40, None, None]], [70, [60, None, None], [80, None, None]]],
    current_path=[1, 2], next_node=[60, None, None], next_path=[2, 1], next_values=[50, 70, 60]):
    """pytest style test for _get_next_node_path.

    """
    for (test, ref) in zip(
        ic._get_next_node_path_values(
            bin_tree=bin_tree,
            current_path=current_path),
        (next_node, next_path, next_values)):
        assert test == ref
    return None


def test_is_valid_bin_search_tree(
    bin_tree=[50, [30, [10, None, None], [40, None, None]], [70, [60, None, None], [80, None, None]]],
    is_bst=True):
    """pytest style test for is_valid_bin_search_tree.

    """
    assert ic.is_valid_bin_search_tree(bin_tree=bin_tree) == is_bst
    return None


test_is_valid_bin_search_tree(
    bin_tree=[50, [30, [10, None, None], [60, None, None]], [70, [60, None, None], [80, None, None]]],
    is_bst=False)
test_is_valid_bin_search_tree(
    bin_tree=[50, [30, [10, None, None], [40, None, None]], [70, [40, None, None], [80, None, None]]],
    is_bst=False)


def test_q13_find_rotation_index(
    lst=['c', 'd', 'a','b'],
    ref_idx_rot=2):
    r"""Pytest for q13_find_rotation_index.
    
    """
    test_idx_rot = ic.q13_find_rotation_index(lst=lst)
    assert ref_idx_rot == test_idx_rot
    return None
    

lsts = [
    ['a','b','c','d'],
    ['b','c','d','a'],
    ['c','d','a','b'],
    ['d','a','b','c'],
    ['a','b','c','d','e'],
    ['b','c','d','e','a'],
    ['c','d','e','a','b'],
    ['d','e','a','b','c'],
    ['e','a','b','c','d']]
ref_idxs_rot = [0, 3, 2, 1, 0, 4, 3, 2, 1]
for (lst, ref_idx_rot) in zip(lsts, ref_idxs_rot):
	test_q13_find_rotation_index(lst=lst, ref_idx_rot=ref_idx_rot)


def test_q14_movies_match_flight(
    flight_length=200, movie_lengths=[100, 90, 100], ref_found_match=True):
    r"""Pytest for q14_movies_match_flight.
    
    """
    test_found_match = ic.q14_movies_match_flight(
        flight_length=flight_length, movie_lengths=movie_lengths)
    assert ref_found_match == test_found_match
    return None


def test_q14_movies_match_flight_suppl() -> None:
    r"""Supplemental pytests for q14_movies_match_flight.
    
    """
    flight_lengths = [200, 200]
    movie_lengths_list = [
        [100, 50, 50],
        [200, 30, 30]]
    ref_found_matches = [False, False]
    for (flight_length, movie_lengths, ref_found_match) in \
        zip(flight_lengths, movie_lengths_list, ref_found_matches):
        test_q14_movies_match_flight(
            flight_length=flight_length,
            movie_lengths=movie_lengths,
            ref_found_match=ref_found_match)
    return None


def test_q15_fib(idx:int=4, ref_fnum:int=3) -> None:
    r"""Pytest for q15_fib.
    
    """
    test_fnum = ic.q15_fib(idx=idx)
    assert ref_fnum == test_fnum
    return None


def test_q15_fib_suppl() -> None:
    r"""Supplemental pytests for q15_fib.
    
    """
    with pytest.raises(ValueError):
        ic.q15_fib(idx=1.0)
        ic.q15_fib(idx=-1)
    return None


def test_q16_max_duffel_bag_value(
    cake_tuples:list=[(7, 160), (3, 90), (2, 15)],
    bag_capacity:int=20,
    ref_bag_value:int=555) -> None:
    r"""Pytest for q16_max_duffel_bag_value.
    
    """
    test_bag_value = ic.q16_max_duffel_bag_value(
        cake_tuples=cake_tuples, bag_capacity=bag_capacity)
    assert ref_bag_value == test_bag_value
    return None
    
    
def test_q16_max_duffel_bag_value_suppl() -> None:
    r"""Supplemental pytests for q16_max_duffel_bag_value.
    
    """
    with pytest.raises(ValueError):
        ic.q16_max_duffel_bag_value(
            cake_tuples=[(7, 160), (3, 90), (2, 15)], bag_capacity=-1)
        ic.q16_max_duffel_bag_value(
            cake_tuples=[(7, 160), (-1, 90), (2, 15)], bag_capacity=20)
        ic.q16_max_duffel_bag_value(
            cake_tuples=[(7, 160), (3, -1), (2, 15)], bag_capacity=20)
        ic.q16_max_duffel_bag_value(
            cake_tuples=[(7, 160), (3, 90.0), (2, 15)], bag_capacity=20)
    test_q16_max_duffel_bag_value(
        cake_tuples=[(0, 160), (3, 90), (2, 15)],
        bag_capacity=20, ref_bag_value=sys.maxsize)
    test_q16_max_duffel_bag_value(
        cake_tuples=[(0, 0), (3, 90), (2, 15)], bag_capacity=20, ref_bag_value=555)
    test_q16_max_duffel_bag_value(
        cake_tuples=[(1, 30), (50, 200)], bag_capacity=100, ref_bag_value=3000)
    test_q16_max_duffel_bag_value(
        cake_tuples=[(3, 40), (5, 70)], bag_capacity=8, ref_bag_value=110)
    test_q16_max_duffel_bag_value(
        cake_tuples=[(3, 40), (5, 70)], bag_capacity=9, ref_bag_value=120)
    return None