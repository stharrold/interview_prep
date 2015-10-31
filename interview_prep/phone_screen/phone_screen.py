#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""My interations of answers to common phone screen questions.

"""


# Import standard packages.
import collections
import math
import sys
# Import installed packages.
# Import local packages.
import interview_prep.utils as utils


def reverse_string(string:str) -> str:
    """Reverse a string.
    
    Args:
        string (str): String with __getslice__ method.

    Returns:
        string_rev (str): Reversed `string`.

    Notes:
        * Example 1 from [1]_.
        * Complexity:
            * n = len(string)
            * Time: O(n)
            * Space: O(n)

    References:
        .. [1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

    """
    utils.check_arguments(
        antns=reverse_string.__annotations__,
        lcls=locals())
    string_rev = string[::-1]
    return string_rev


def calc_nth_fib(nth:int) -> int:
    """Calculate the nth Fibonacci number (0-indexed).

    Args:
        nth (int): The index number of the Fibonacci number to calculate.
            `nth` >= 0

    Returns:
        fib_nth (int): The `nth` Fibonacci number in sequence.
    
    Raises:
        ValueError: Raised if `nth` < 0. 

    Notes:
        * fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).
        * Complexity:
            * n = `nth`
            * Time: O(n)
            * Space: O(1)

    """
    # # Check arguments.
    # utils.check_arguments(
    #     antns=calc_nth_fib.__annotations__,
    #     lcls=locals())
    # if nth < 0:
    #     raise ValueError(
    #         ("`nth` must be >= 0\n" +
    #          "nth = {nth}").format(nth=nth))
    # Initialize Fibonacci sequence to reach nth Fibonacci number.
    # fib_prevs = collections.deque()
    # for idx in range(nth):
    #     if idx == 0:
    #         fib_idx = 0
    #     elif idx == 1:
    #         fib_idx = 1
    #     elif idx > 1:
    #         fib_idx = fib_prev1 + fib_prev2
    #         fib_prev2 = fib
    #         fib_prev1 = fib_idx
    #     else:
    #         raise AssertionError(
    #             ("Program error. `idx` must be >= `nth`\n" +
    #              "idx = {idx}\nnth = {nth}").format(idx=idx, nth=nth))
        
    fibs = [0, 1]
    while len(fibs) < nth:
        fibs.append(fibs[-2] + fibs[-1])
    # Check computation.
    if nth == 0:
        assert fibs[nth-1] == fibs[0]
    else:
        assert fibs[nth-1] == fibs[-1]
    return fibs[nth-1]


def print_mult_table(max_fac=12):
    """Print to stdout a multiplication table.
    
    Args:
        max_fac: {12}, int, optional
            Maximum factor up to which to make table.`max_fac` >= 0.
            Example: max_fac=12 (default) makes multiplication table
            0x0, 0x1, ... 12x11, 12x12.

    Returns:
        None
            Prints table to `stdout`.

    Raises:
        ValueError:
            Raised if `max_fac` < 0.

    Notes:
        - Example 3 from [1].
        - Complexity:
            Time: O(n^2)
            Space: O(1)

    References:
        ..[1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

    """
    # Check input
    if max_fac < 0:
        raise ValueError(("`max_fac` must be >= 0\n" +
                          "max_fac = {max_fac}").format(max_fac=max_fac))
    # Define custom print function for rows of multiplication table.
    max_prod = max_fac*max_fac
    max_digits = int(math.log10(max_prod)) + 1
    fmt = "{elt:>" + str(max_digits) + "d}"
    print_elt = lambda elt: print(fmt.format(elt=elt), end=' ')
    # Print multiplication table.
    for row_fac in range(max_fac+1):
        # Print header row
        if row_fac == 0:
            print(' '*(max_digits-1) + 'x', end=' ')
            [print_elt(elt) for elt in range(max_fac+1)]
            print()
        # Print header column element for every row.
        print_elt(elt=row_fac)
        # Print products
        [print_elt(row_fac*col_fac) for col_fac in range(max_fac+1)]
        print()
    return None


def sum_ints(fname):
    """Sum the ints from a text file, one per line

    Args:
        fname: string
            Path to file. File contains one `int` per line.

    Returns:
        total: int
            Sum of all `int`s in file `fname`.

    Notes:
        * Example 4 from [1]
        * Complexity:
            Time: O(n), n is number of lines in `fname` file.
            Space: O(1)

    References:
        .. [1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions
    
    """
    # TODO: check input
    total = 0
    with open(fname, 'rb') as fobj:
        for line in fobj:
            total += int(line.strip())
    return total
