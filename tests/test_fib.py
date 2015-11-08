#!/usr/bin/env python
# -*- coding=utf-8 -*-
r"""Pytests for interview_prep/interview_prep/fib.py

"""


# Import standard packages.
import os
import sys
# Import installed packages.
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.fib as fib


def test__init_fibs(fibs=[0, 1]):
    fib._init_fibs()
    assert fib.fibs == fibs
    return None


def test_fib_lookup(idx=5, fn=5, fibs=[0, 1, 1, 2, 3, 5]):
    del(fib.fibs)
    assert (fib.fib_lookup(idx=5) == fn
            and fib.fibs == fibs)
    return None

    
def test_fib_recur(idx=5, fn=5):
    assert fib.fib_recur(idx=5) == fn
    return None
