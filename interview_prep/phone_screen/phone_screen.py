#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""My interations of answers to common phone screen questions.

"""


# Import standard packages.
import collections
import os
import sys
# Import installed packages.
# Import local packages.
import interview_prep.utils as utils


def reverse_string(string:str) -> str:
    r"""Reverse a string.
    
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
    r"""Calculate the nth Fibonacci number (0-indexed).

    Args:
        nth (int): The index number of the Fibonacci number to calculate.
            `nth` >= 0

    Returns:
        fib (int): The `nth` Fibonacci number in sequence.
    
    Raises:
        ValueError: Raised if `nth` < 0. 

    Notes:
        * fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).
        * Complexity:
            * n = `nth`
            * Time: O(n)
            * Space: O(1)

    """
    # Check arguments.
    utils.check_arguments(
        antns=calc_nth_fib.__annotations__,
        lcls=locals())
    if nth < 0:
        raise ValueError(
            ("`nth` must be >= 0\n" +
             "nth = {nth}").format(nth=nth))
    # Initialize Fibonacci sequence to reach nth Fibonacci number.
    maxlen = 2
    fibs_prev = collections.deque(maxlen=maxlen)
    fibs_prev.extend(range(maxlen))
    if nth < maxlen:
        fib = fibs_prev[nth]
    else:
        idxs_res = range((nth - maxlen) + 1)
        [fibs_prev.append(sum(fibs_prev)) for idx in idxs_res]
        fib = fibs_prev[-1]
    return fib


def print_mult_table(max_fac:int=12) -> None:
    r"""Print a multiplication table to stdout.
    
    Args:
        max_fac (int, optional, default=12):  Factor up to which to make table.
            `max_fac` >= 0.
            Example: max_fac=12 (default) makes multiplication table
            0x0,  0x1,  ..., 0x12
            1x0,  1x1,  ..., 1x12
            ...,  ...,  ..., ...
            12x0, 12x1, ..., 12x12

    Returns:
        None: Prints table to `stdout`.

    Raises:
        ValueError: Raised if `max_fac` < 0.

    Notes:
        * Example 3 from [1].
        * Complexity:
            * n = max_fac
            * Time: O(n^2)
            * Space: O(1)

    References:
        .. [1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

    """
    # Check input
    utils.check_arguments(
        antns=print_mult_table.__annotations__,
        lcls=locals())
    if max_fac < 0:
        raise ValueError(
            ("`max_fac` must be >= 0\n" +
             "max_fac = {max_fac}").format(max_fac=max_fac))
    # Define custom print function for factors and products (elements)
    # of multiplication table,
    max_prod = max_fac*max_fac
    max_digits = len(str(max_prod))
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


def sum_ints(path:str) -> int:
    r"""Sum the integers from a text file, one integer per line.

    Args:
        path(str): Path to file. File contains one `int` per line.

    Returns:
        total(int): Total sum of all `int`s in the file.

    Notes:
        * Example 4 from [1]_.
        * Complexity:
            * n = number of lines in `path` file.
            * Time: O(n)
            * Space: O(1)

    References:
        .. [1] https://sites.google.com/site/steveyegge2/
               five-essential-phone-screen-questions
    
    """
    # Check input.
    utils.check_arguments(
        antns=sum_ints.__annotations__,
        lcls=locals())
    if not os.path.exists(path):
        raise ValueError(
            ("`path` does not exist:\n" +
             "path =\n{path}").format(path=path))
    # Sum the lines in the file.
    total = 0
    with open(path, 'rt') as fobj:
        for line in fobj:
            total += int(line.strip())
    return total
