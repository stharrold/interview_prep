# -*- coding: utf-8 -*-
"""My iterations of answers to questions on iterviewcake.com.

"""


from __future__ import absolute_import, division, print_function
import copy
import collections


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
    for amt in xrange(1, amount+1):
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
    return len(combos[amount]) if combos.has_key(amount) else 0

        
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
        for amt in xrange(denom+1, amount+1):
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
            space: O(number_of_unique_temperatures)

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
