#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My interations of answers to
https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

"""


from __future__ import absolute_import, division, print_function


def reverse_string(string):
    """Reverse a string.
    
    Args:
        string: str
            String with __getslice__ method.

    Returns:
        revd: str
            Reversed `string`.

    Notes:
        - Example 1 from [1]
        - Complexity:
            Time: O(n)
            Space: O(1)

    References:
        ..[1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions
        ..[2] http://stackoverflow.com/questions/931092/reverse-a-string-in-python

    """
    return string[::-1]


def calc_nth_fib(nth):
    """Calculate the nth Fibonacci number.

    Args:
        nth: int
            The sequence number of the Fibonaci number to calculate.
            `nth` >= 1

    Returns:
        nth_fib: int
            The `nth` Fibonacci number in sequence.

    Notes:
        - Complexity:
            Time: O(n), n = `nth`
            Space: O(n), n = `nth`

    """
    # TODO: check input
    # TODO: save state information between calls with global or class.
    # TODO: use array.array for efficient storage.
    # Check input
    if nth < 1:
        raise ValueError(("`nth` must be >= 1\n" +
                          "nth = {nth}").format(nth=nth))
    # Initialize Fibonacci sequence and append to reach nth Fibonacci number.
    fibs = [0, 1]
    while len(fibs) < nth:
        fibs.append(fibs[-2] + fibs[-1])
    # Check computation.
    if nth = 0:
        assert fibs[nth-1] == fibs[0]
    else:
        assert fibs[nth-1] == fibs[-1]
    return fibs[nth-1]
