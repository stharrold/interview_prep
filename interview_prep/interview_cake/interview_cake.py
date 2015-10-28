#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""My answers to questions on iterviewcake.com.

"""


# Import standard packages.
import copy
import collections
import operator
import pdb
# Import installed packages.
import numpy as np
# Import local packages.


def check_arguments(antns, lcls) -> None:
    r"""Check types of a function's arguments. Call from within the function.
    
    Args:
        antns: Annotations of enclosing function.
        lcls: Local variables.
    
    Returns:
        None
        
    Raises:
        ValueError: Raised if arguments do not match annotated arguments.
    
    Notes:
        * Example usage:
            ```
            def myfunc(arg0: int, arg1: str) -> float:
               check_arguments(antns=myfunc.__annotations__, lcls=locals())
            ```
    
    """
    for (arg, cls) in antns.items():
        if arg != 'return':
            if not isinstance(lcls[arg], cls):
                raise ValueError(
                    ("type({arg}) must be {cls}\n" +
                     "type({arg}) = {typ}").format(
                        arg=arg, cls=cls, typ=type(lcls[arg])))
    return None


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
    idxs = range(len(ints))
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

    Raises:
        ValueError:
            Raised if `len(ints) < 3`.

    References:
        ..[1] https://www.interviewcake.com/question/highest-product-of-3
    
    """
    # Check input
    if len(ints) < 3:
        raise ValueError("`ints` must have at least 3 elements")
    # Compute top three ints
    # TODO: make top 3 a default arg
    # TODO: use collections.deque?
    tops_pos = []
    tops_neg = []
    for iint in ints:
        if iint >= 0:
            if len(tops_pos) < 3:
                tops_pos.append(iint)
                tops_pos = sorted(tops_pos) # TODO: optimize
            else:
                for (idx, top) in enumerate(tops_pos):
                    if iint > top:
                        tops_pos[idx] = iint
                        break
                    else:
                        break
        else:
            if len(tops_neg) < 2:
                tops_neg.append(iint)
                tops_neg = sorted(tops_neg, key=abs) # TODO; optimize
            else:
                for (idx, top) in enumerate(tops_neg):
                    if abs(iint) > abs(top):
                        tops_neg[idx] = iint
                        break
                    else:
                        break
    # Compute product
    prod_pos = 1
    for top in tops_pos:
        prod_pos *= top
    prod_neg = 1
    for top in tops_neg:
        prod_neg *= top
    prod_pos_neg = prod_neg * max(tops_pos)
    highest_product = max(prod_pos, prod_pos_neg)
    return highest_product    


def get_highest_product_2(ints):
    """Compute the highest product of 3 integers.
    
    Args:
        ints: list
            List of `int` with at least 3 items.
    
    Returns:
        highest_product:
            Greatest product from multiplying 3 ints.

    Raises:
        ValueError:
            Raised if `len(ints) < 3`.

    References:
        ..[1] https://www.interviewcake.com/question/highest-product-of-3

    """
    # Check input.
    if len(ints) < 3:
        raise ValueError("`ints` must have at least 3 items.")
    # Initialize variables to track.
    # TODO: optimize by reducing loops. keep it programmatic.
    highest_product = 1
    for iint in ints[:3]:
        highest_product *= iint
    highest_product_top_2 = 1
    highest_product_bot_2 = 1
    for iint in ints[:2]:
        highest_product_top_2 *= iint
        highest_product_bot_2 *= iint
    highest = ints[0]
    lowest = ints[0]
    # Iteratively update tracked variables.
    for iint in ints:
        highest_product = max(highest_product, iint*highest_product_top_2, iint*highest_product_bot_2)
        highest_product_top_2 = max(highest_product_top_2, iint*highest)
        highest_product_bot_2 = max(highest_product_bot_2, iint*lowest)
        highest = max(highest, iint)
        lowest = min(lowest, iint)
    return highest_product


def calc_intersection(rect1, rect2):
    """Calculate the intersection of two rectangles.
    
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


def condense_meeting_times(times):
    """Condense meeting times into contiguous blocks.
    
    Args:
        times: list
            List of meeting times as tuples.
            List does not need to be sorted.
            Example: [(0, 1), (3, 5), (2, 4)]

    Returns:
        condensed: list
            Sorted list of combined meeting times as tuples.
            Example: [(0, 1), (2, 5)]

    Notes:
        - Interviewcake.com problem #4
        - Complexity: time: O(nlgn), space: O(n)
    
    References:
        ..[1] https://www.interviewcake.com/question/merging-ranges
        ..[2] https://wiki.python.org/moin/TimeComplexity
        
    """
    # TODO: check input
    # Sort times first by meeting start then by meeting end
    # to avoid needing to compare all meeting times to each other.
    # Sorting eliminates need to test if meetings occur before each other
    # or if they are nested.
    times = sorted(times, key=lambda tup: (tup[0], tup[1]))
    condensed = [times[0]]
    for time in times:
        cond = condensed[-1]
        # If meetings are disjoint, append as new meeting.
        if time[0] > cond[1]:
            condensed.append(time)
        # Else if meetings overlap, join.
        elif cond[0] <= time[0] and time[0] <= cond[1] and cond[1] <= time[1]:
            condensed[-1] = (cond[0], time[1]) # set item takes O(1)
    return condensed


def gen_change_combinations(amount, denominations, init_combo=None):
    """Create a combination of coins that sum to amount.
    
    Args:
        amount: int
            Value of change to partition into denominations.
            Example: 4
        denominations: list
            Sorted list of unique denominations into which `amount` of change is partitioned.
            Example: [1, 2, 3]
        init_combo: {None}, list, optional
            Initialize a portion of combination. If `None` (default), then builds
            combination of `denominations` without prior values.
            Example: None
    
    Yields:
        combo: list
            Generates a combination of `denominations` that sum to `amount`.
            Example: ([1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2])
    
    See Also:
        count_change_combinations

    Notes:
        - Because recursive, can cause large call stack.
    
    """
    # TODO: check input
    if init_combo is None:
        combo = [denominations[0]]
    else:
        combo = copy.deepcopy(init_combo)
        combo.append(denominations[0])
    for (idx, denom) in enumerate(denominations):
        combo[-1] = denom
        remainder = amount - sum(combo)
        if remainder > 0:
            for gen_combo in gen_change_combinations(amount=amount,
                                                 denominations=denominations[idx:],
                                                 init_combo=combo):
                yield gen_combo
        elif remainder == 0:
            yield combo
            break
        else:
            break


def count_change_combinations(amount, denominations):
    """Count the number of possible combinations for a given amount of change
    from the given denominations.
    
    Args:
        amount: int
            Value of change to partition into denominations.
            Example: 4
        denominations: list
            List of denominations into which `amount` of change is partitioned.
            Example: [1, 2, 3]

    Returns:
        num: int
            Number of possible combinations of denominations to total `amount` of change.
            Example: 4

    See Also:
        gen_change_combinations
    
    Notes:
        - interviewcake.com question #5.
        - Because uses a recursive helper function, can cause a large call stack.
        - Complexity:
            time: O(amount*len(denominations))
            space: O(amount*len(denominations)) in call stack

    References:
        ..[1] https://www.interviewcake.com/question/coin

    """
    # TODO: check input
    num = 0
    denominations = sorted(set(denominations))
    for _ in gen_change_combinations(amount=amount, denominations=denominations, init_combo=None):
           num += 1
    return num


def count_change_combinations_2(amount, denominations):
    """Count the number of possible combinations for a given amount of change
    from the given denominations.

    Args:
        amount: int
            Value of change to partition into denominations.
            Example: 4
        denominations: list
            List of denominations into which `amount` of change is partitioned.
            Example: [1, 2, 3]

    Returns:
        num: int
            Number of possible combinations of denominations to total `amount` of change.
            Example: 4

    Notes:
        - interviewcake.com question #5.
        - Non-recursive, but iterates through denominations for each amount and
            requires saving combinations in order to avoid double-counting unique solutions.
        - Complexity:
            time: O(amount*len(denominations))
            space: O(amount*len(denominations))

    References:
        ..[1] https://www.interviewcake.com/question/coin
    
    """
    # TODO: check input
    combos = {}
    # Build all possible combinations of denominations by memorizing.
    for amt in range(1, amount+1):
        combos[amt] = []
        if amt in denominations:
            combos[amt].append(tuple([amt]))
        # Collect combinations from amounts and their complements.
        amts_gt = [key for key in combos.keys() if key >= round(max(combos)/2)]
        for amt_gt in amts_gt:
            amt_lt = amt - amt_gt
            if amt_lt in combos:
                for comb_gt in combos[amt_gt]:
                    for comb_lt in combos[amt_lt]:
                        comb = []
                        comb.extend(list(comb_gt))
                        comb.extend(list(comb_lt))
                        combos[amt].append(tuple(sorted(comb)))
        # Remove duplicates.
        combos[amt] = set(combos[amt])
    return len(combos[amount]) if amount in combos else 0

        
def count_change_combinations_3(amount, denominations):
    """Count the number of possible combinations for a given amount of change
    from the given denominations.

    Args:
        amount: int
            Value of change to partition into denominations.
            Example: 4
        denominations: list
            List of denominations into which `amount` of change is partitioned.
            Example: [1, 2, 3]

    Returns:
        num: int
            Number of possible combinations of denominations to total `amount` of change.
            Example: 4

    Notes:
        - interviewcake.com question #5.
        - Non-recursive and iterates through amounts for each denomination to eliminate
            saving combinations in order to avoid double-counting unique solutions.
        - Complexity:
            time: O(amount*len(denominations))
            space: O(amount)

    References:
        ..[1] https://www.interviewcake.com/question/coin
    
    """
    # TODO: check input
    num_combos = collections.Counter()
    # Iterate through amount for each denomination to avoid double-counting.
    # TODO: make self-referencing dict comprehension for 2x speedup
    for denom in denominations:
        num_combos[denom] += 1
        for amt in range(denom+1, amount+1):
            num_combos[amt] += num_combos[amt-denom]
    return num_combos[amount]


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
            Time: O(len_path) ~ O(log2(num_nodes_of_bin_tree))
            Space: O(len_path) ~ O(log2(num_nodes_of_bin_tree))

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
            Time: O(num_nodes*log2(num_nodes)^2)
            Space: O(log2(num_nodes_of_bin_tree))

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
                Space: O(log2(num_nodes))
            Realized:
                Time: O(num_nodes*log2(num_nodes)^2)
                Space: O(log2(num_nodes))

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
                * Time: log2(len(lst))
                * Space: O(1)
            * Realized:
                * Time: log2(len(lst))
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
        # log2 x bounded by x.
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
    check_arguments(
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
        * fib(n) = fib(n-1) + fib(n-2)
            where fib(0) = 0, fib(1) = 1.
        * Complexity:
            * Ideal:
                * Time: O(log2(n))
                * Space: O(1)
            * Realized:
                * Time: O(n)
                * Space: O(1)
    
    References:
        .. [1] https://www.interviewcake.com/question/python/nth-fibonacci

    """
    # Check arguments.
    check_arguments(
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


def q16_max_duffel_bag_value(cake_tuples:list, capacity:int) -> int:
    r"""Compute max value that the duffel bag can hold.
    
    Args:
        cake_tuples (list): `list` of `tuple`s (cake_weight, cake_value)
            cake_weight, cake_value > 0
        capacity (int): Max weight that the duffel bag can hold.
    
    Returns:
        bag_value (int): Max value that the duffel bag can hold.
            Returns `numpy.inf` if there is a cake with weight = 0.
        
        
    Notes:
        * interviewcake.com question #16, "The Cake Thief"
        * Complexity:
            * n = len(cake_tuples)
            * Ideal:
                * Time: 
                * Space: 
            * Realized:
                * Time: O(n*log2(n))
                * Space: O(1)
                
    References:
        .. [1] https://www.interviewcake.com/question/python/cake-thief
    
    """
    check_arguments(
        antns=q16_max_duffel_bag_value.__annotations__,
        lcls=locals())
    for tup in cake_tuples:
        for item in tup:
            if item < 0:
                raise ValueError(
                    ("All elements in `cake_tuples` must be >= 0:\n" +
                     "cake_tuples =\n" +
                     "{ct}").format(ct=cake_tuples))
    if capacity < 0:
        raise ValueError(
            ("`capacity` must be >= 0\n" +
             "capacity = {cap}").format(cap=capacity))
    # Optimize value-to-weight ratio.
    (cake_weights, cake_values) = zip(*cake_tuples)
    if 0 in cake_weights:
        bag_value = np.inf
    else:
        cake_triples = sorted(
            [(cake_weight, cake_value, cake_value/cake_weight)
             for (cake_weight, cake_value) in cake_tuples],
            key=operator.itemgetter(2),
            reverse=True)
        bag_value = 0
        res = capacity
        for (cake_weight, cake_value, _) in cake_triples:
            if res >= cake_weight:
                num_cakes = int(res/cake_weight)
                bag_value += num_cakes*cake_value
                res -= num_cakes*cake_weight
    return bag_value
