#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Pytests for interview_prep/interview_prep/sorting.py

"""


# Import standard packages.
import os
import sys
# Import intalled packages.
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.sorting as sort


def test_median_pivot(vals=[0, 1, 2, 3, 4], pivot_val=2, pivot_idx=2):
    r"""Pytest for _median_pivot.

    """
    assert sort._median_pivot(vals=vals) == (pivot_val, pivot_idx)
    return None


def test_quicksort(vals=[5, 0, 2, 5, 4, 6, 5, 6], sorted_vals=[0, 2, 4, 5, 5, 5, 6, 6]):
    r"""Pytest for quicksort.

    """
    assert sort.quicksort(vals=vals) == sorted_vals
    return None
