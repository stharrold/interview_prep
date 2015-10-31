#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Pytests for interview_prep/phone_screen/phone_screen.py

"""


# Import standard packages.
import io
import os
import sys
import tempfile
# Import installed packages.
import pytest
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.phone_screen.phone_screen as ps


def test_reverse_string(
    string:str='asdfjkl;',
    string_rev:str=';lkjfdsa') -> None:
    """Pytest for reverse_string.

    """
    assert ps.reverse_string(string=string) == string_rev
    return None


def test_calc_nth_fib(
    nth:int=4,
    fib:int=3) -> None:
    """Pytest for calc_nth_fib.

    """
    assert ps.calc_nth_fib(nth=nth) == fib
    return None


def test_calc_nth_fib_suppl() -> None:
    r"""Supplemental pytests for calc_nth_fib.
    
    """
    with pytest.raises(ValueError):
        ps.calc_nth_fib(nth=1.0)
        ps.calc_nth_fib(nth=-1)
    return None


def test_print_mult_table(
    max_fac:int=2,
    ref_stdout:str=\
"""x 0 1 2 
0 0 0 0 
1 0 1 2 
2 0 2 4 
""") -> None:
    """Pytest for print_mult_table.

    """
    # Create a string buffer to capture print statements and
    # assign to the `sys.stdout` pointer. Capture the output then
    # reassign `sys.stdout` to original stream. 
    test_stdout = io.StringIO()
    sys.stdout = test_stdout
    ps.print_mult_table(max_fac=max_fac)
    sys.stdout = sys.__stdout__
    assert test_stdout.getvalue() == ref_stdout
    return None


def test_print_mult_table_suppl() -> None:
    r"""Supplemental pytests for print_mult_table.
    
    """
    with pytest.raises(ValueError):
        ps.print_mult_table(max_fac=1.0)
        ps.print_mult_table(max_fac=-1)
    return None


def test_sum_ints(contents=\
"""1
2
3
""",
ref_total=6):
    """Pytest for sum_ints.

    """
    (_, fname) = tempfile.mkstemp()
    with open(fname, 'w') as fobj:
        fobj.write(contents)
    test_total = ps.sum_ints(fname=fname)
    assert ref_total == test_total
    os.remove(fname)
    return None
