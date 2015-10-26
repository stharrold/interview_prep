#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Tests for interview_prep/interview_cake/interview_cake.py

"""


# Import standard packages.
import collections
import sys
sys.path.insert(0, '.')
# Import installed packages.
# Import local packages.
import interview_prep.interview_cake.interview_cake as ic


def test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,2.,3.], max_profit=7.0):
    """pytest style test for calc_max_profit
    
    """
    assert ic.calc_max_profit(prices) == max_profit
    return None


test_calc_max_profit(prices=[5.0, 4.0, 5.0, 3.0, 6.0, 5.0, 9.0, 8.0, 10.0, -20.0, 3.0], max_profit=23.)


def test_get_products_of_all_ints_except_at_index(ints=[1,7,3,4], prods=[7*3*4, 1*3*4, 1*7*4, 1*7*3]):
    """pytest style test
    
    """
    prod_pairs = list(filter(
        lambda tup: tup[0] == tup[1],
        zip(ic.get_products_of_all_ints_except_at_index(ints), prods)))
    assert len(prod_pairs) == len(ints)
    return None


test_get_products_of_all_ints_except_at_index()
test_get_products_of_all_ints_except_at_index(ints=[0,0,0], prods=[0,0,0])
test_get_products_of_all_ints_except_at_index(ints=[5], prods=[1])
test_get_products_of_all_ints_except_at_index(ints=[], prods=[])


def test_get_highest_product(ints=[-10,-10,-20,1,3,2], highest_product=600):
    """pytest style test for get_highest_product

    """
    assert ic.get_highest_product(ints=ints) == highest_product
    return None


def test_get_highest_product_2(ints=[-10,-10,-20,1,3,2], highest_product=600):
    """pytest style test for get_highest_product_2

    """
    assert ic.get_highest_product_2(ints=ints) == highest_product
    return None


def test_calc_intersection(rect1={'x':0.0, 'y':0.0, 'width':3.0, 'height':3.0},
                           rect2={'x':1.0, 'y':1.0, 'width':3.0, 'height':3.0},
                           recti={'x':1.0, 'y':1.0, 'width':2.0, 'height':2.0}):
    """pytest style test for calc_intersection

    """
    assert ic.calc_intersection(rect1=rect1, rect2=rect2) == recti
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
    assert ic.calc_intersection_2(rect1=rect1, rect2=rect2) == recti
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
    assert ic.condense_meeting_times(times=times) == condensed
    return None


test_condense_meeting_times(times=[(1, 10), (2, 6), (3, 5), (7, 9)], condensed=[(1, 10)])



def test_gen_change_combinations(amount=4, denominations=[1, 2, 3], init_combo=None,
                                 combinations=[[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]):
    """pytest style test for gen_change_denominations

    """
    assert list(ic.gen_change_combinations(
        amount=amount, denominations=denominations, init_combo=init_combo)) == combinations
    return None


def test_count_change_combinations(amount=4, denominations=[1, 2, 3], num=4):
    """pytest style test for count_change_denominations
    
    """
    assert ic.count_change_combinations(
        amount=amount, denominations=denominations) == num
    return None


def test_count_change_combinations_2(amount=4, denominations=[1, 2, 3], num=4):
    """pytest style test for count_change_denominations_2
    
    """
    assert ic.count_change_combinations_2(
        amount=amount, denominations=denominations) == num
    return None


def test_count_change_combinations_3(amount=4, denominations=[1, 2, 3], num=4):
    """pytest style test for count_change_denominations_3

    """
    assert ic.count_change_combinations_3(
        amount=amount, denominations=denominations) == num
    return None


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
