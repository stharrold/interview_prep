#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""My answers to questions on interviewcake.com.

"""


# Import standard packages.
import copy
import collections
import functools
import itertools
import operator
import os
import pdb
import sys
# Import installed packages.
# Import local packages.
import interview_prep.utils as utils


def q1_calc_max_profit(prices:list) -> float:
    r"""Compute maximum profit from stock prices.
    
    Args:
        prices (list): List of prices as `float`. Index is number of minutes
            since beginning of trading day.
    
    Returns:
        max_profit (float): Maximum profit possible from buying then selling.
    
    Notes:
        * interviewcake.com question #1, "Apple Stocks".
        * Complexity:
            * n = len(prices)
            * Ideal: Time=O(n), Space=O(1)
            * Realized: Time=O(n), Space=O(1)
    
    References:
        .. [1] https://www.interviewcake.com/question/stock-price
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q1_calc_max_profit.__annotations__,
        lcls=locals())
    # Calculate max_profit sequentially with min_price since the fund must be
    # bought before being sold.
    (min_price, max_profit) = (prices[0], 0.0)
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def q2_get_products_of_all_ints_except_at_index(ints:list) -> list:
    r"""Calculate the products of all integers except for the one each index.

    Args:
        ints (list): `list` of `int` factors.

    Returns:
        prods (list): `list` of `int` products
    
    Notes:
        * interviewcake.com question #2, "Product of All Other Numbers".
        * Complexity:
            * n = len(prices)
            * Ideal: Time=O(n), Space=O(n)
            * Realized: Time=O(n), Space=O(n)

    References:
        ..[1] https://www.interviewcake.com/question/product-of-other-numbers
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q2_get_products_of_all_ints_except_at_index.__annotations__,
        lcls=locals())
    # Allocate a list of ones for `prods`. Multiply products at indexes by
    # cumulative product then update cumulative product. Repeat iterating in
    # opposite direction through `ints`.
    idxs = range(len(ints))
    prods = [1]*len(ints)
    prod_cuml = 1
    for idx in idxs:
        prods[idx] = prod_cuml
        prod_cuml *= ints[idx]
    prod_cuml = 1
    for idx in reversed(idxs):
        prods[idx] *= prod_cuml
        prod_cuml *= ints[idx]
    return prods


def q3_calc_highest_product_of_3(ints:list) -> int:
    r"""Calculate the highest product from integers.
    
    Args:
        ints (list): List of `ints` with `len(ints) >= 3`

    Returns:
        prod (int): Highest product from 3 `int`s.

    Raises:
        ValueError: Raised if `len(ints) < 3`.
    
    Notes:
        * interviewcake.com question #3, "Highest Product of 3".
        * Complexity:
            * n = len(ints)
            * Ideal: Time=O(n), Space=O(1)
            * Realized: Time=O(n), Space=O(1)

    References:
        ..[1] https://www.interviewcake.com/question/highest-product-of-3
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q3_calc_highest_product_of_3.__annotations__,
        lcls=locals())
    if len(ints) < 3:
        raise ValueError(
            ("`ints` must have at least 3 items:\n" +
             "ints =\n{ints}").format(ints=ints))
    # #########################################
    # # With collections, itertools; Python 3.5.
    # max_3 = collections.deque(iterable=[1]*3, maxlen=3)
    # min_2 = collections.deque(iterable=[1]*2, maxlen=2)
    # for item in ints:
    #     # Find the 3 most positive integers.
    #     for idx in range(len(max_3)):
    #         if item > max_3[idx]:
    #             max_3.insert(item, index=idx)
    #             break
    #     # Find the 2 most negative integers.
    #     for idx in range(len(min_2)):
    #         if item < min_2[idx]:
    #             min_2.insert(item, index=idx)
    #             break
    # prod_max_3 = functools.reduce(operator.mul, max_3, 1)
    # prod_min_2 = functools.reduce(operator.mul, min_2, 1)
    # prod_minmax_3 = prod_min_2 * max_3[0]
    # prod = max(prod_max_3, prod_minmax_3)
    # #########################################
    # # With extreme integers ranked.
    # (max_1st, max_2nd, max_3rd) = (1, 1, 1)
    # (min_1st, min_2nd) = (1, 1)
    # for item in ints:
    #     # Find the 3 most positive integers.
    #     if item > max_3rd:
    #         if item > max_2nd:
    #             if item > max_1st:
    #                 max_3rd = max_2nd
    #                 max_2nd = max_1st
    #                 max_1st = item
    #             else:
    #                 max_3rd = max_2nd
    #                 max_2nd = item
    #         else:
    #             max_3rd = item
    #     # Find the 2 most negative integers.
    #     if item < min_2nd:
    #         if item < min_1st:
    #             min_2nd = min_1st
    #             min_1st = item
    #         else:
    #             min_2nd = item
    # prod = max(max_1st*max_2nd*max_3rd, max_1st*min_1st*min_2nd)
    #########################################
    # With bottom-up approach.
    (prod_1_pos, prod_2_pos, prod_3_pos) = (0, 0, 0)
    (prod_1_neg, prod_2_neg) = (0, 0)
    for item in ints:
        # Find the 3 most positive integers.
        if item >= 0:
            prod_3_pos = max(item*prod_2_pos, prod_3_pos)
            prod_2_pos = max(item*prod_1_pos, prod_2_pos)
            prod_1_pos = max(item, prod_1_pos)
        # Find the 2 most negative integers.
        else:
            item *= -1
            prod_2_neg = max(item*prod_1_neg, prod_2_neg)
            prod_1_neg = max(item, prod_1_neg)
    prod = max(prod_3_pos, prod_1_pos*prod_2_neg)
    return prod


def q4_condense_meeting_times(times:list) -> list:
    r"""Condense meeting times into contiguous blocks.
    
    Args:
        times (list): `list` of `tuple`s of `int`s as meeting times. `int`s are
            number of 30-minute blocks since 9:00am. Does not need to be sorted.
            Example: `times = [(0, 1), (3, 5), (2, 4)]`

    Returns:
        condensed (list): `list` of combined meeting times as `tuple`s.
            Example: `condensed = [(0, 1), (2, 5)]`

    Notes:
        * interviewcake.com question #4, "Merging Meeting Times".
        * Complexity:
            * n = len(times)
            * Ideal: Time=O(n*lg(n)), Space=O(n)
            * Realized: Time=O(n*lg(n)), Space=O(n)

    References:
        .. [1] https://www.interviewcake.com/question/merging-ranges

    """
    # Check arguments.
    utils.check_arguments(
        antns=q4_condense_meeting_times.__annotations__,
        lcls=locals())
    # #########################################
    # # Without sorting: Time: O(n**2); Space: O(n)
    # # Iterate through `times` comparing current time to:
    # # * condensed times in `condensed`, iterating forwards
    # # * uncondensed times in `times`, iterating forwards
    # # * uncondensed times in `times`, iterating backwards
    # # * condensed times in `condensed`, iterating backwards
    # # Backwards and forwards iteration is necessary for unsorted `times`.
    # def do_overlap(time1:tuple, time2:tuple) -> bool:
    #     # Check arguments.
    #     utils.check_arguments(
    #         antns=do_overlap.__annotations__,
    #         lcls=locals())
    #     # Order meeting times by start time.
    #     # Overlap if first stop time >= second start time.
    #     if time1[0] < time2[0]:
    #         (time1st, time2nd) = (time1, time2)
    #     else:
    #         (time1st, time2nd) = (time2, time1)
    #     if time1st[1] >= time2nd[0]:
    #         overlap = True
    #     else:
    #         overlap = False
    #     return overlap
    # # Compare current time to seen condensed times.
    # condensed = [times[0]]
    # for (idx, time) in enumerate(times):
    #     idx_olap = None
    #     # Compare current time with condensed times, forward.
    #     for idx_cmp in range(len(condensed)):
    #         time_cmp = condensed[idx_cmp]
    #         overlap = do_overlap(time1=time, time2=time_cmp)
    #         if overlap:
    #             time = (min(time[0], time_cmp[0]), max(time[1], time_cmp[1]))
    #             if idx_olap is None:
    #                 idx_olap = idx_cmp
    #     # Compare current time with uncondensed times, forward and backward.
    #     for idx_cmp in itertools.chain(
    #         range(idx+1, len(times)), reversed(range(idx+1, len(times)-1))):
    #         time_cmp = times[idx_cmp]
    #         overlap = do_overlap(time1=time, time2=time_cmp)
    #         if overlap:
    #             time = (min(time[0], time_cmp[0]), max(time[1], time_cmp[1]))
    #     # Compare current time with condensed times, backward.
    #     for idx_cmp in reversed(range(len(condensed))):
    #         time_cmp = condensed[idx_cmp]
    #         overlap = do_overlap(time1=time, time2=time_cmp)
    #         if overlap:
    #             time = (min(time[0], time_cmp[0]), max(time[1], time_cmp[1]))
    #             if idx_olap is None:
    #                 idx_olap = idx_cmp
    #     # Update condensed times if overlap, else append.
    #     if idx_olap is not None:
    #         condensed[idx_olap] = time
    #     else:
    #         condensed.append(time)
    ########################################
    # With sorting: Time: O(n*lg(n)); Space: O(n)
    # Sort times first by meeting start then by meeting end
    # to avoid needing to compare all meeting times to each other.
    times = sorted(times, key=operator.itemgetter(0, 1))
    condensed = [times[0]]
    for time in times:
        cond = condensed[-1]
        # If time is disjoint, append as new meeting.
        # Else change condensed meeting time.
        if cond[1] < time[0]:
            condensed.append(time)
        else:
            condensed[-1] = (cond[0], max(cond[1], time[1]))
    return condensed


def q5_count_combinations(amount:int, denoms:list) -> int:
    r"""Count the number of combinations of `denomiations` that sum to `amount`.
    
    Args:
        amount (int): Amount of money to partition.
        denoms (list): `list` of demoninations to partition `amount`
    
    Returns:
        ncombos (int): Number of combinations.
    
    Raises:
        ValueError:
            * Raised if not amount >= 1.
            * Raised if not len(denoms) >= 1.
            * Raised if any denoms are not `int`.
            * Raised if any denoms are not >= 1.
        
    Notes:
        * interviewcake.com question #5, "Making Change".
        * Complexity:
            * n = amount; k = len(denoms)
            * Complexity:
                * Ideal: Time: O(n*k); Space: O(n)
                * Realized:
    
    References:
        .. [1] https://www.interviewcake.com/question/python/coin
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q5_count_combinations.__annotations__,
        lcls=locals())
    if not amount >= 1:
        raise ValueError(
            ("`amount` must be >= 1\n" +
             "amount = {amt}").format(amt=amount))
    if not len(denoms) >= 1:
        raise ValueError(
            ("`len(denoms)` must be >= 1\n" +
             "len(denoms) = {nden}").format(nden=len(denoms)))
    for denom in denoms:
        if not isinstance(denom, int):
            raise ValueError(
                ("All `denoms` must be type `int`\n" +
                 "denom = {den}\n" +
                 "type(denom) = {tden}").format(den=denom, tden=type(denom)))
        if not denom >= 1:
            raise ValueError(
                ("All `denoms` must be >= 1\n" +
                 "denom = {den}").format(den=denom))
    # For each denomination, iterate through the amounts to find the number of
    # combinations per amount.
    # Note: For each amount, iterating through denominations will instead find
    # the number of permutations per amount.
    amt_ncombos = [0]*(amount+1)
    amt_ncombos[0] = 1
    for den in denoms:
        for amt in range(den, amount+1):
            amt_ncombos[amt] += amt_ncombos[amt-den]
    ncombos = amt_ncombos[amount]
    return ncombos


def q6_calc_intersection(rect1:dict, rect2:dict) -> dict:
    r"""Calculate the intersection of two rectangles.
    
    Args:
        rect1 (dict):
        rect2 (dict):
            Rectangles are `dicts` with keys `x`, `y`, `width`, `height`.
            `x`, `y` are the coordinates of the bottom-left corner.
    
    Returns:
        recti (dict):
            Rectangle intersection as `dict`. Same format at `rect1`, `rect2`.
    
    Raises:
        ValueError: Raised if missing keys.

    Notes:
        * interviewcake.com question #6, "Rectangular Love".
        * Complexity:
            * TODO
    
    References:
        .. [1] https://www.interviewcake.com/question/rectangular-love

    """
    # Check arguments.
    utils.check_arguments(
        antns=q6_calc_intersection.__annotations__,
        lcls=locals())
    # TODO: resume here 20151107
    ##########
    # Check input
    if not (isinstance(rect1, dict) and isinstance(rect2, dict)):
        raise ValueError("`rect1` and `rect2` must both be type `dict`")
    for rect in [rect1, rect2]:
        for key in ['x', 'y', 'width', 'height']:
            if not key in rect:
                raise ValueError("All `rect`s must have the key {key}".format(key=key))
    ##########
    # Strictly order the rectangles in a well-defined way: left-to-right, up-to-down
    # Assigning by references, so no extra mem usage.
    (rect_lhs, rect_rhs) = (rect1, rect2) if rect1['x'] <= rect2['x'] else (rect2, rect1)
    (rect_lwr, rect_upr) = (rect1, rect2) if rect1['y'] <= rect2['y'] else (rect2, rect1)
    assert rect_lhs != rect_rhs
    assert rect_lwr != rect_upr
    ##########
    # Cases:
    # Overlapping case:
    # |
    # |           xr,yu+hu------------------------xr+wr,yu+hu
    # |             |                                 |
    # | xl,yl+hl----|------xl+wl,yl+hl                |
    # |   |         |        |                        |
    # |   |       xr,yu------|--------------------xr+wr,yu
    # |   |                  |
    # | xl,yl--------------xl+wl,yl
    # |
    # 0,0 ------------------------------------------------
    # xl+wl - xl = (xr - xl) + (xl+wl - xr) ==> wi = xl+wl - xr; xi = xl + (xr - xl) = xr
    # yl+hl - yl = (yu - yl) + (yl+hl - yu) ==> hi = yl+hl - yu; yi = yl + (yu - yl) = yu
    #
    # Overlapping case:
    # |
    # |  xl,yu+hu-----------xl+wl,yu+hu
    # |   |                    |
    # |   |       xr,yl+hl-----|------------------xr+wr,yl+hl
    # |   |         |          |                      |
    # |  xl,yu------|-------xl+wl,yu                  |
    # |             |                                 |
    # |          xr,yl----------------------------xr+wr,yl
    # |
    # 0,0 ------------------------------------------------
    # xl+wl - xl = (xr - xl) + (xl+wl - xr) ==> wi = xl+wl - xr; xi = xl + (xr - xl) = xr
    # yl+hl - yl = (yu - yl) + (yl+hl - yu) ==> hi = yl+hl - yu; yi = yl + (yu - yl) = yu
    #
    # Nested case:
    # |
    # |  xl,yl+hl-----------------------------------------xl+wl,yl+hl
    # |     |                                               |
    # |     |       xr,yu+hu--------------xr+wr,yu+hu       |
    # |     |          |                      |             |
    # |     |       xr,yu-----------------xr+wr,yu          |
    # |     |                                               |
    # |   xl,yl-------------------------------------------xl+wl,yl
    # |
    # 0,0 ------------------------------------------------
    # xl+wl - xl = (xr - xl) + (xr+wr - xr) + (xl+wl - xr+wr) ==> wi = xr+wr - xr = wr; xi = xl + (xr - xl) = xr
    # yl+hl - yl = (yu - yl) + (yu+hu - yu) + (yl+hl - yu+hu) ==> hi = yu+hu - yu = hu; yi = yl + (yu - yl) = yu
    widths_nested = True if rect_lhs['x'] + rect_lhs['width'] > rect_rhs['x'] + rect_rhs['width'] else False
    heights_nested = True if rect_lwr['y'] + rect_lwr['height'] > rect_upr['y'] + rect_upr['height'] else False
    #
    # Disjoint case:
    # |
    # |  xl,yl+hl----xl+xw,yl+hl      
    # |     |          |              xr,yu+hu---------------xr+wr,yu+hu
    # |     |          |                |                         |
    # |     |          |                |                         |
    # |     |          |              xr,yu------------------xr+wr,yu   
    # |     |          |     
    # |   xl,yl------xl+xw,yl
    # |
    # 0,0 ------------------------------------------------
    # wi = None, xi = None
    # hi = None, yi = None
    if (rect_lhs['x'] + rect_lhs['width'] < rect_rhs['x'] or
        rect_lwr['y'] + rect_lwr['height'] < rect_upr['y']):
        disjoint = True
    else:
        disjoint = False
    ##########
    # Calculate and return rectangle intersection
    if disjoint:
        recti = \
            {'x': None,
             'y': None,
             'width': None,
             'height': None}
    else:
        recti = \
            {'x': rect_rhs['x'],
             'y': rect_upr['y'],
             'width': rect_rhs['width'] if widths_nested else rect_lhs['x'] + rect_lhs['width'] - rect_rhs['x'],
             'height': rech_upr['height'] if heights_nested else rect_lwr['y'] + rect_lwr['height'] - rect_upr['y']}
    return recti


def calc_overlap(pt1, len1, pt2, len2):
    """Calculate the overlap of two line segments.

    Args:
        pt1: float
            Min coordinate of line segment 1.
        len1: float
            Length of line segment 1.
        pt2: float
            Min coordinate of line segment 2.
        len2: float
            Length of line segment 2.

    Return:
        pti: float
            Min coordiante of intersecting line segment.
        leni: float
            Length of intersecting line coordinate.

    TODO:
       Rename calc_overlap, calc_intersection_2 to reflect dimensions.
    """
    # TODO: Check input
    # Order coordinates.
    if pt1 <= pt2:
        ((pt_lhs, len_lhs), (pt_rhs, len_rhs)) = ((pt1, len1), (pt2, len2))
    else:
        ((pt_lhs, len_lhs), (pt_rhs, len_rhs)) = ((pt2, len2), (pt1, len1))
    # If segments are nested...
    if pt_lhs + len_lhs > pt_rhs + len_rhs:
        (pti, leni) = (pt_rhs, len_rhs)
    else:
        leni = pt_lhs + len_lhs - pt_rhs
        if leni >= 0:
            # If segments overlap...
            pti = pt_rhs - pt_lhs
        else:
            # ...otherwise segments are disjoint.
            (pti, leni) = (None, None)
    return (pti, leni)


def calc_intersection_2(rect1, rect2):
    """Calculate the intersection of two rectangles but with the
    dementionsality of the problem reduced.

    Args:
        rect1: dict
        rect2: dict
            Rectangles are `dicts` with keys `x`, `y`, `width`, `height`.
            `x`, `y` are the coordinates of the bottom-left corner.
    
    Returns:
        recti: dict
            Rectangle of intersection as `dict`. Same format at `rect1`, `rect2`.
    
    Raises:
        ValueError:
            TODO: raise if wrong type or missing keys.
    
    References:
        ..[1] https://www.interviewcake.com/question/rectangular-love

    """
    ##########
    # Check input
    if not (isinstance(rect1, dict) and isinstance(rect2, dict)):
        raise ValueError("`rect1` and `rect2` must both be type `dict`")
    for rect in [rect1, rect2]:
        for key in ['x', 'y', 'width', 'height']:
            if not key in rect:
                raise ValueError("All `rect`s must have the key {key}".format(key=key))
    ##########
    # Compute overlap.
    recti = {}
    (recti['x'], recti['width']) = calc_overlap(pt1=rect1['x'], len1=rect1['width'],
                                                pt2=rect2['x'], len2=rect2['width'])
    (recti['y'], recti['height']) = calc_overlap(pt1=rect1['y'], len1=rect1['height'],
                                                 pt2=rect2['y'], len2=rect2['height'])
    # Check if rectangles are disjoint.
    if (recti['width'] is None or
        recti['height'] is None):
        recti = {'x': None,
                 'y': None,
                 'width': None,
                 'height': None}
    return recti


class TempTracker(object):
    """Manage temperatures to check consistency with guarantee.
    Units are degrees Fahrenheit. Assumes 0 deg F <= temp <= 110 deg F.

    Attrs:
        ctr: collections.Counter
            Number of temperatures grouped by temperature.

    Notes:
        - interviewcake.com question #6
        - Complexity:
            time for get methods: O(1)
            time for insert: O(number_of_temperatures)
            space: O(number_of_unique_temperatures) ~ O(1)

    References:
        ..[1] https://www.interviewcake.com/question/temperature-tracker
    
    """


    def insert(self, temps):
        """Insert a new temperature into the record.
        
        Args:
            temps: {list, int}
            List of `int` temperatures or a single `int` temperature.

        Returns:
            None
        
        """
        # TODO: check temp value 0-110
        # Cast to type `list` in case `temps` is only an `int`
        if temps is None:
            temps = []
        elif not isinstance(temps, collections.Iterable):
            temps = [temps]
        if not hasattr(self, 'ctr'):
            self.ctr = collections.Counter(temps)
        else:
            self.ctr.update(temps)
        self._max = max(self.ctr)
        self._min = min(self.ctr)
        self._total = sum(self.ctr.elements())
        self._num = sum(self.ctr.values())
        self._mean = self._total / self._num
        self._mode = self.ctr.most_common(1)
        return None


    def __init__(self, temps=None):
        """Initialize TempTracker.
        
        Args:
            temps: {None}, {list, int}, optional
                List of `int` temperatures or a single `int` temperature.
                If `None` (default), initialized to empty `list`.

        Returns:
            None
        
        """
        # TODO: check temp value 0-110
        self.insert(temps)
        return None


    def get_max(self):
        """Compute the maximum temperature.

       Returns:
           temp: int
               Maximum temperature.
        
        """
        return self._max


    def get_min(self):
        """Compute the minimum temperature.
        
        Returns:
            temp: int
                Minimum temperature.

        """
        return self._min


    def get_mean(self):
        """Compute the mean temperature.
        
        Returns:
            temp: float
                Mean temperature.

        """
        return self._mean


    def get_mode(self):
        """Compute the temperature mode.
        
        Returns:
            temp: int
                Temperature mode.
        
        """
        return self._mode


def is_leaf_node(node):
    """Determine if the current node is a leaf node.

    Args:
        node: list
            Each node is itself a k-ary tree, represented as a `list` with at most k elements.
            Examples: [value, lhs, rhs], [value, lhs], [value]
    
    Returns:
        is_leaf: bool
            `True` if `len(node) == 1`
            `False` if otherwise.
            Examples (from `node` examples): False, False, True

    See Also:
        is_super_balanced

    Notes:
        - interviewcake.com question #8
        - Complexity:
            Time: O(1)
            Space: O(1)

    References:
        ..[1] https://www.interviewcake.com/question/balanced-binary-tree
    
    """
    return len(node) == 1


def get_younger_sibling_or_parent(tree, path):
    """Determine if the node at the path has a sibling node with an index one larger than its own,
        i.e. a "younger" sibling. Return if so, otherwise return the node's parent.
    
    Args:
        tree: list
            A k-ary tree represented as a `list` with at most k elements.
            Each node of the k-ary tree is itself a k-ary tree.
            Example: [value, [value, [value], [value]], [value]]
        path: list
            Sequence of indexes leading to node to evaluate.
            Example: [1, 1]

    Returns:
        node_sp: {None}, list
            The node in `tree` identified by `path[-1] += 1`, i.e. the younger sibling of the node
            identified by `path`, if there there is a younger sibling.
            Otherwise, the parent of the node is returned. If the node has no parent, then `None`.
        path_sp: {[]}, list
            Sequences of indexes leading to `node_sp` within `tree`.
            If `node_sp` is the root of `tree`, then `[]`.
        rel_sp: {'younger_sibling', 'parent'}, string
            Relationship of returned `node_sp` to the node identified by input `path`.

    Raises:
        ValueError: Raised if `path` does not identify a valid node within `tree`.
    
    See Also:
        is_super_balanced

    Notes:
        - interviewcake.com question #8
        - Complexity:
            Time: O(max_depth) ~ O(logk(num_nodes))
            Space: O(1)

    References:
        ..[1] https://www.interviewcake.com/question/balanced-binary-tree

    """
    # Check input
    # The root node is its own parent.
    if len(path) < 1:
        raise ValueError("`path` must identify a valid node within `tree`.")
    # Initialize values to track
    node_sp = tree
    path_sp = copy.copy(path)
    path_sp[-1] += 1
    # Find younger sibling or parent.
    for (iidx, idx) in enumerate(path_sp):
        try:
            node_sp = node_sp[idx]
            rel_sp = 'younger_sibling'
        except IndexError:
            # node_sp was previously assigned to the parent of the node identified by input `path`
            if iidx != len(path) - 1:
                raise ValueError("`path` must identify a valid node within `tree`.")
            path_sp.pop()
            rel_sp = 'parent'
    return (node_sp, path_sp, rel_sp)
    

def is_super_balanced(tree):
    """Evaluate whether a k-ary tree is super balanced,
    i.e. the maximum difference in depths between leaf nodes is <= 1.

    Args:
        tree: list
            A k-ary tree represented as a list of lists.
            Each element of `tree` is a `list`. The first element of each `list` within
            `tree` is the value of that node.
            Example: [val, [val, [val], [val]], [val, [val, [val]]]]
    
    Returns:
        is_super: bool
            `True` if the maximum difference in depths between leaf nodes is <= 1.
            `False` if otherwise.
            Example (from Args:`tree` example): True

    Notes:
        - interviewcake.com question #8
        - Complexity:
            Time: O(num_nodes*logk(num_nodes))
            Space: O(max_depth) ~ O(logk(num_nodes))

    References:
        ..[1] https://www.interviewcake.com/question/balanced-binary-tree
    
    """
    # TODO: Check input.
    # Initialize values to track.
    min_depth = None
    max_depth = None
    # TODO: remove current_path to reduce space
    current_path = None
    is_super = None
    current_node = tree
    # Iterate through the tree.
    while ((current_path is None) or (len(current_path) > 0)) and ((is_super is None) or is_super):
        # Depth-first search of first child to find a leaf node.
        while not is_leaf_node(node=current_node):
            current_node = current_node[1]
            if current_path is not None: current_path.append(1)
            else: current_path = [1]
        # Current node is a leaf node. Evaluate its depth.
        if min_depth is not None: min_depth = min(min_depth, len(current_path))
        else: min_depth = len(current_path)
        if max_depth is not None: max_depth = max(max_depth, len(current_path))
        else: max_depth = len(current_path)
        is_super = (max_depth - min_depth <= 1)
        # Break if find one example of violating super-balanced.
        if not is_super:
            break
        # Set the current node to the leaf node's sibling if it exists, or the sibling of its parent.
        # TODO: finding the next node is not optimal.
        relationship = None
        while ((relationship is None) or (relationship == 'parent')) and (len(current_path) > 0):
            (current_node, current_path, relationship) = get_younger_sibling_or_parent(tree=tree, path=current_path)
    return is_super


def _get_next_path(current_path):
    """Semi-private method to get next path in a breadth-first search of a binary tree.

    Args:
        current_path: list
            Path to current node of within a binary tree.
            Example: [1, 2, 2]; [2, 2, 2]

    Returns:
        next_path: list
            Path of `next_node` of a full binary tree following breadth-first search.
            Example from Args: current_path: [2, 1, 1]; [1, 1, 1, 1]

    See Also:
        is_valid_bin_search, _get_next_node_path

    Notes:
        - Assumes that binary tree is full. Calling scope must check that path is valid.
        - Complexity:
            Time: O(len_path) ~ O(lg(num_nodes_of_bin_tree))
            Space: O(len_path) ~ O(lg(num_nodes_of_bin_tree))

    """
    # Find a cousin node at the same depth otherwise descend to next depth of binary tree.
    next_path = copy.copy(current_path)
    found_cousin_node_at_same_depth = None
    for rev_path_idx, bin_tree_idx in enumerate(reversed(current_path), start=1):
        if bin_tree_idx == 2:
            next_path[-rev_path_idx] = 1
        else:
            next_path[-rev_path_idx] = 2
            found_cousin_node_at_same_depth = True
            break
    if not found_cousin_node_at_same_depth:
        next_path.append(1)
    return next_path


def _get_next_node_path_values(bin_tree, current_path):
    """Get the next node, path, and node values in a breadth-first search of a binary tree.

    Args:
        bin_tree: list
            Binary tree represented as a `list` with 3 elements.
            Leaf nodes have format [value, `None`, `None`]
            Example: [50, [30, None, [40, None, None]], [70, [60, None, None], None]]
        current_path: list
            Path to current node of `bin_tree`.
            Example: [1, 2]

    Returns:
        next_node: list
            Next node of `bin_tree` following breadth-first search.
            `None` if at maximum depth, far rhs of binary tree.
            Example: [60, None, None]
        next_path: list
            Path of `next_node` of `bin_tree` following breadth-first search.
            `None` if at maximum depth, far rhs of binary tree.
            Example: [2, 1]
        next_values: list
            Node values of nodes along `next_path`.
            `None` if at maximum depth, far rhs of binary tree.
            Example: [50, 70, 60]

    See Also:
        is_valid_bin_search, _get_next_path

    Notes:
        - Complexity:
            Time: O(num_nodes*lg(num_nodes)^2)
            Space: O(lg(num_nodes_of_bin_tree))

    """
    # TODO: memoize which nodes we’ve seen to reduce time
    orig_path_len = len(current_path)
    next_path = _get_next_path(current_path=current_path)
    next_node = bin_tree
    next_values = [next_node[0]]
    next_path_is_valid = None
    while not next_path_is_valid:
        try:
            for idx in next_path:
                next_node = next_node[idx]
                if next_node is not None: next_values.append(next_node[0])
                else: next_values.append(None)
            next_path_is_valid = True
        except IndexError:
            next_path_is_valid = False
            next_path_len = len(next_path)
            if next_path_len - orig_path_len > 1:
                break
            next_path = _get_next_path(current_path=next_path)
            next_node = bin_tree
            next_values = []
    if not next_path_is_valid:
        (next_node, next_path, next_values) = (None, None, None)
    return (next_node, next_path, next_values)


def is_valid_bin_search_tree(bin_tree):
    """Determine if a binary tree is a valid binary search tree,
    i.e. where every node is less than its rhs child and greater than
    the lhs child.

    Args:
        bin_tree: list
        Binary tree represented as a `list` with 3 elements.
        Leaf nodes have format [value, `None`, `None`]
        Example: [value, lhs, rhs], where lhs and rhs are each binary trees.

    Returns:
        is_bst: bool
        `True` if `bin_tree` is a valid binary search tree.
        `False` otherwise.

    See Also:
        _get_next_node_path_values
  
    Notes:
        - interviewcake.com question #9
        - Complexity:
            Ideal:
                Time: O(num_nodes)
                Space: O(lg(num_nodes))
            Realized:
                Time: O(num_nodes*lg(num_nodes)^2)
                Space: O(lg(num_nodes))

    TODO:
        - Redo with depth-first search
        - Memoize bounds of ancestor nodes rather than all ancestor nodes.
        - Use array rather than list of lists.
    
    References:
        .. [1] https://www.interviewcake.com/question/bst-checker

    """
    # TODO: check that `bin_tree` is valid binary tree
    (current_node, current_path, current_values) = (bin_tree, [], [bin_tree[0]])
    is_bst = None
    while ((current_node is not None) and
           (is_bst is None or is_bst is True)):
        if current_node[1] is not None: lhs_value = current_node[1][0]
        else: lhs_value = None
        if current_node[2] is not None: rhs_value = current_node[2][0]
        else: rhs_value = None
        for (rev_idx, current_value) in enumerate(reversed(current_values), start=1):
            # Compare the value of a parent node with its lhs, rhs child nodes.
            if rev_idx == 1:
                if lhs_value is not None: is_bst_lhs = lhs_value < current_value
                else: is_bst_lhs = True
                if rhs_value is not None: is_bst_rhs = current_value < rhs_value
                else: is_bst_rhs = True
            # Compare the value of a grandparent+ node with its lhs, rhs grandchild+ nodes.
            # If the grandparent node's child is lhs, then its granchildren must also be lhs.
            else:
                if current_path[-rev_idx+1] == 1:
                    if lhs_value is not None: is_bst_lhs = lhs_value < current_value
                    else: is_bst_lhs = True
                    if rhs_value is not None: is_bst_rhs = rhs_value < current_value
                    else: is_bst_rhs = True
                else:
                    if lhs_value is not None: is_bst_lhs = current_value < lhs_value
                    else: is_bst_lhs = True
                    if rhs_value is not None: is_bst_rhs = current_value < rhs_value
                    else: is_bst_rhs = True
            is_bst = (is_bst_lhs and is_bst_rhs)
            if not is_bst:
                break
        if not is_bst:
            break
        (current_node, current_path, current_values) = _get_next_node_path_values(bin_tree=bin_tree,
                                                                                  current_path=current_path)
    return is_bst


def q13_find_rotation_index(lst: list) -> int:
    r"""Find the rotation index.
    
    Args:
        lst (list): List of sorted words but rotated.
        
    Returns:
    	idx_rot (int): Rotation index.
    
    Notes:
        * interviewcake.com question #13, "Find Rotation Point".
        * Complexity:
            * Ideal:
                * Time: lg(len(lst))
                * Space: O(1)
            * Realized:
                * Time: lg(len(lst))
                * Space: O(1)
    
    References:
        .. [1] https://www.interviewcake.com/question/python/find-rotation-point
    
    """
    # Check input.
    for (arg, cls) in q13_find_rotation_index.__annotations__.items():
        if arg != 'return':
            if not isinstance(locals()[arg], cls):
                raise TypeError(
                    ("{arg} must be an instance of {cls}").format(
                        arg=arg, cls=cls))
    # Initialize indexes
    idx_ceil = len(lst) - 1
    idx_ceil_prev = idx_ceil
    idx_floor = 0
    idx_rot = None
    # Check if list is sorted.
    if lst[idx_floor] < lst[idx_ceil]:
        idx_rot = idx_floor
    else:
        # Deterministic stopping criteria to avoid infinite loops.
        # No recursion to avoid building call stack.
        # lg x bounded by x.
        for inum in range(len(lst)):
            if idx_floor == idx_ceil - 1:
                idx_rot = idx_ceil
                break
            else:
                # If 1st half of list is sorted,
                # check 2nd half on next iteration.
                idx_ceil = int(idx_floor + (idx_ceil - idx_floor)/2)
                if lst[idx_floor] < lst[idx_ceil]:
                    idx_floor = idx_ceil
                    idx_ceil = idx_ceil_prev
                else:
                    idx_ceil_prev = idx_ceil
    return idx_rot


def q14_movies_match_flight(flight_length: int, movie_lengths: list) -> bool:
    r"""Check if the sum of two movie lengths exactly equals the flight length.
    
    Args:
        flight_length (int): Length (duration) of the flight. Units: minutes.
        movie_lengths (list): List of `int` as the lengths (durations) of
            movies. Units: minutes.
        
    Returns:
        found_match (bool):
            True: There are two movies whose sum lengths exactly matches the
                length of the flight.
            False: There are not two movies...
        
    Notes:
        * interviewcake.com question #14, "Inflight Entertainment" [1]_.
        * Complexity:
            * Ideal:
                * Time: O(n)
                * Space: O(n)
            * Realized:
                * Time: O(n)
                * Space: O(n)
    
    References:
        .. [1] https://www.interviewcake.com/question/python/
            inflight-entertainment
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q14_movies_match_flight.__annotations__,
        lcls=locals())
    # Memoize movie lengths seen.
    # Without `collections.defaultdict`:
    # `in` calls `dict.__contains__`, which is O(1) lookup for Python 3x.
    #found_match = False
    #movie_lengths_seen = dict()
    #for movie_length1 in movie_lengths:
    #    movie_length2 = flight_length - movie_length1
    #    if movie_length2 in movie_lengths_seen:
    #        found_match = True
    #        break
    #    # Add movie_length1 after testing for movie_length2 to avoid watching
    #    # movie1 twice.
    #    movie_lengths_seen[movie_length1] = True
    # With `collections.defaultdict`:
    movie_lengths_seen = collections.defaultdict(lambda: False)
    for movie_length1 in movie_lengths:
        movie_length2 = flight_length - movie_length1
        found_match = movie_lengths_seen[movie_length2]
        if found_match:
            break
        # Add movie_length1 after testing for movie_length2 to avoid watching
        # movie1 twice.
        movie_lengths_seen[movie_length1] = True
    return found_match


def q15_fib(idx: int) -> int:
    r"""Compute the nth Fibonacci number.
    
    Args:
        idx (int): Nth Fibonacci number to compute.
            `idx` >= 0.
    
    Returns:
        fnum (int): Nth Fibonacci number.
        
    Raises:
        ValueError: Raised if `idx` < 0 or is not `int`.
    
    Notes:
        * interviewcake.com question #15, "Compute Nth Fibonacci Number" [1]_.
        * fib(n) = fib(n-1) + fib(n-2), fib(0) = 0, fib(1) = 1.
        * Complexity:
            * Ideal:
                * Time: O(lg(n))
                * Space: O(1)
            * Realized:
                * Time: O(n)
                * Space: O(1)
    
    References:
        .. [1] https://www.interviewcake.com/question/python/nth-fibonacci

    """
    # Check arguments.
    utils.check_arguments(
        antns=q15_fib.__annotations__,
        lcls=locals())
    if idx < 0:
        raise ValueError(
            ("`idx` must be >= 0:\n" +
             "idx = {idx}").format(idx=idx))
    # Compute nth Fibonacci number.
    for inum in range(idx+1):
        if inum == 0:
            fnum = 0
            fnum_prev2 = 0
        elif inum == 1:
            fnum = 1
            fnum_prev1 = 1
        else:
            fnum = fnum_prev1 + fnum_prev2
            fnum_prev2 = fnum_prev1
            fnum_prev1 = fnum
    return fnum


def q16_max_duffel_bag_value(cake_tuples:list, bag_capacity:int) -> int:
    r"""Compute max value that the duffel bag can hold.
    
    Args:
        cake_tuples (list): `list` of `tuple`s (cake_weight, cake_value)
            cake_weight, cake_value > 0
        bag_capacity (int): Max weight that the duffel bag can hold.
    
    Returns:
        bag_value (int): Max value that the duffel bag can hold.
            Returns `numpy.inf` if there is a cake with weight = 0.
        
    Notes:
        * interviewcake.com question #16, "The Cake Thief"
        * Complexity:
            * (n, k) = (len(cake_tuples), bag_capacity)
            * Ideal:
                * Time: O(n*k)
                * Space: O(k)
            * Realized:
                * Time: O(n*k)
                * Space: O(k)
                
    References:
        .. [1] https://www.interviewcake.com/question/python/cake-thief
    
    """
    # Check arguments.
    utils.check_arguments(
        antns=q16_max_duffel_bag_value.__annotations__,
        lcls=locals())
    for tup in cake_tuples:
        for item in tup:
            if item < 0:
                raise ValueError(
                    ("All items in `cake_tuples` must be >= 0:\n" +
                     "cake_tuples =\n" +
                     "{ct}").format(ct=cake_tuples))
            elif not isinstance(item, int):
                raise ValueError(
                    ("All items in `cake_tuples` must be type `int`:\n" +
                     "cake_tuples =\n" +
                     "{ct}").format(ct=cake_tuples))
    if bag_capacity < 0:
        raise ValueError(
            ("`bag_capacity` must be >= 0\n" +
             "bag_capacity = {bc}").format(bc=bag_capacity))
    # With dynamic programming:
    bag_value = 0
    for (cake_weight, cake_value) in cake_tuples:
        if cake_weight == 0 and cake_value > 0:
            bag_value = sys.maxsize
    if bag_value != sys.maxsize:
        bag_values_max = [0]*(bag_capacity + 1)
        for bag_capacity_current in range(len(bag_values_max)):
            for (cake_weight, cake_value) in cake_tuples:
                if cake_weight <= bag_capacity_current:
                    bag_values_max[bag_capacity_current] = max(
                        bag_values_max[bag_capacity_current],
                        cake_value + bag_values_max[
                            bag_capacity_current - cake_weight])
        bag_value = bag_values_max[bag_capacity]
    return bag_value
