"""Tests for interview_prep/fibonacci/fib.py

"""

from __future__ import absolute_import, division, print_function
import sys
sys.path.insert(0, '.')
import interview_prep as ip


def test__init_fibs(fibs=[0, 1]):
    ip.fibonacci.fib._init_fibs()
    assert ip.fibonacci.fib.fibs == fibs


def test_fib_lookup(idx=5, fn=5, fibs=[0, 1, 1, 2, 3, 5]):
    del(ip.fibonacci.fib.fibs)
    assert (ip.fibonacci.fib.fib_lookup(idx=5) == fn
            and ip.fibonacci.fib.fibs == fibs)

    
def test_fib_recur(idx=5, fn=5):
    assert ip.fibonacci.fib.fib_recur(idx=5) == fn
