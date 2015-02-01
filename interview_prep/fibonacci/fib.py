import logging

logger = logging.getLogger(__name__)

# Global variable to lookup computed Fibonnaci numbers.
# Using a class requires extra code maintenance.
fibs = []

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
    From [1]_: 
    F_n = F_n-1 + F_n-2
    Time complexity is O(1) for in-memory lookup.
    Space complexity is O(phi^n), where phi is golden ratio, ~1.6.
    
    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Fibonacci_number

    """
    # Check input.
    if not isinstance(idx, int):
        idx = int(idx)
    if idx < 0:
        raise ValueError(("`idx` must be an ``int`` >= 0:\n" +
                          "idx = {idx}").format(idx=idx))
    # Initialize fibs array and compute Fibonacci number.
    if len(fibs) < 2:
        fibs = [0, 1]
    if len(fibs) - 1 < idx:
        if idx > 1:
            # Note: Lookup F_n-1 before F_n-2 for easier trace.
            # Computations and memory access is equivalent.
            fn = fib_lookup(idx-1) + fib_lookup(idx-2)
            fibs.append(fn)
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
    From [1]_: 
    F_n = F_n-1 + F_n-2
    Time complexity is O(phi^n), where phi is golden ratio, ~1.6.
    Space complexity is O(2), for 2 ints.
    
    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Fibonacci_number

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
        # Note: Lookup F_n-1 before F_n-2 for easier trace.
        # Computations and memory access is equivalent.
        fn = fib_recur(idx-1) + fib_recur(idx-2)
    else:
        raise AssertionError(("Program error. `idx` must be an ``int`` >= 0:\n" +
                              "idx = {idx}").format(idx=idx))
    logger.debug(("F{idx} = {fn}").format(idx=idx, fn=fn))
    return fn
