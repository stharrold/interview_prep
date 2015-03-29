#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for interview_prep/phone_screen/phone_screen.py

"""


from __future__ import absolute_import, division, print_function
import sys
sys.path.insert(0, '.')
import cStringIO
import interview_prep as ip


def test_reverse_string(string='asdfjkl;', revd=';lkjfdsa'):
    """pytest style test for reverse_string.

    """
    assert ip.phone_screen.phone_screen.reverse_string(string=string) == revd
    return None


def test_calc_nth_fib(nth=5, nth_fib=3):
    """pytest style test for calc_nth_fib.

    """
    assert ip.phone_screen.phone_screen.calc_nth_fib(nth=nth) == nth_fib
    return None


def test_print_mult_table(
    max_fac=2,
    ref_stdout=\
"""  x   0   1   2
  0   0   0   0
  1   0   1   2
  2   0   2   4
"""):
    """pytest style test for print_mult_table
    """
    stdout_orig = sys.stdout
    captured_stdout = cStingIO.StringIO()
    sys.stdout = captured_output
    print_mult_table(max_fac=max_fac)
    sys.stdout = stdout_orig
    assert captured_stdout.getvalue() == ref_stdout
    return None
