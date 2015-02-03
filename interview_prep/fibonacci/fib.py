"""Utilities for computing Fibonacci sequence.

"""
# Import standard packages.
from __future__ import absolute_import, division, print_function
import sys
import logging
# Import installed packages
import numpy as np


# Globals
logger = logging.getLogger(__name__)
fibs = []


def _init_fibs():
    """Semi-private function to initialize Fibonacci sequence for lookup.
    Resets a global variable: fibs = [0, 1]

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    global fibs
    fibs = [0, 1]
    return None


def fib_lookup(idx):
    """Compute Fibonacci number, looked up from an array.

    Parameters
    ----------
    idx : int
        Index of Fibonacci number, >= 0.

    Returns
    -------
    fn : int
        Fibonacci number at given index.

    Notes
    -----
    * Fibonacci sequence [1]_:
        F_n = F_n-1 + F_n-2
    * Complexities [2]_:
        Time complexity is O(1) to O(n) for dynamic array.
        Space complexity is O(n) for dynamic array.

    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Fibonacci_number
    .. [2] http://bigocheatsheet.com/

    """
    # Check input.
    if not isinstance(idx, int):
        idx = int(idx)
    if idx < 0:
        raise ValueError(("`idx` must be an ``int`` >= 0:\n" +
                          "idx = {idx}").format(idx=idx))
    # Initialize fibs array and compute Fibonacci number.
    if 'fibs' not in globals():
        _init_fibs()
    if len(fibs) < 2:
        _init_fibs()
    if len(fibs) - 1 < idx:
        if idx > 1:
            # Note: Lookup F_n-1 before F_n-2 for clearer trace.
            try:
                logger.debug(
                    ("Recursive call: fib_lookup(idx={idxn1}) + fib_lookup(idx={idxn2})").format(
                        idxn1=idx-1, idxn2=idx-2))
                fn = fib_lookup(idx=idx-1) + fib_lookup(idx=idx-2)
                fibs.append(fn)
            except RuntimeError as err:
                fn = np.NaN
                print(("RuntimeError: {err}\n" +
                       "F{idx} is set to {fn}").format(err=err, idx=idx, fn=fn),
                      file=sys.stderr)

        else:
            raise AssertionError(("Program error. `fibs` must be initialized with [0,1]:\n" +
                                  "fibs = {fibs}").format(fibs=fibs))
    else:
        fn = fibs[idx]
    logger.debug(("F{idx} = {fn}").format(idx=idx, fn=fn))
    logger.debug(("fibs = {fibs}").format(fibs=fibs))
    return fn


def fib_recur(idx):
    """Compute Fibonacci number, recursively.

    Parameters
    ----------
    idx : int
         Index of Fibonacci number, >= 0.

    Returns
    -------
    fn : int
        Fibonacci number at given index.

    Notes
    -----
    * Fibonacci sequence [1_]:
        F_n = F_n-1 + F_n-2
    * Complexities [2]_, [3]_:
        Time complexity is O(phi^n), where phi is golden ratio, ~1.6.
        Space complexity is O(n), for storing 1 ``int`` for each of n stack frames.

    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Fibonacci_number
    .. [2] http://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence
    .. [3] http://www.quora.com/What-is-the-space-complexity-of-a-recursive-fibonacci-function

    """
    # Check input.
    if not isinstance(idx, int):
        idx = int(idx)
    if idx < 0:
        raise ValueError(("`idx` must be an ``int`` >= 0:\n" +
                          "idx = {idx}").format(idx=idx))
    # Compute Fibonacci number.
    if idx == 0:
        fn = 0
    elif idx == 1:
        fn = 1
    elif idx > 1:
        # Note: Lookup F_n-1 before F_n-2 for clearer trace.
        try:
            logger.debug(
                ("Recursive call: fib_lookup(idx={idxn1}) + fib_lookup(idx={idxn2})").format(
                    idxn1=idx-1, idxn2=idx-2))
            fn = fib_recur(idx=idx-1) + fib_recur(idx=idx-2)
        except RuntimeError as err:
            print(err, file=sys.stderr)
    else:
        raise AssertionError(("Program error. `idx` must be an ``int`` >= 0:\n" +
                              "idx = {idx}").format(idx=idx))
    logger.debug(("F{idx} = {fn}").format(idx=idx, fn=fn))
    return fn
