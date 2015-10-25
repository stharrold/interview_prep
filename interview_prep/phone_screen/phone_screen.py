#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My interations of answers to
https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

"""


# Import standard packages
import pdb
import math


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
        - Example 4 from [1]
        - Complexity:
            Time: O(n), n is number of lines in `fname` file.
            Space: O(1)

    References:
        ..[1] https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions
    
    """
    # TODO: check input
    total = 0
    with open(fname, 'rb') as fobj:
        for line in fobj:
            total += int(line.strip())
    return total
