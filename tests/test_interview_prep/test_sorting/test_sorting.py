#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for interview_prep/sorting/sorting.py

"""


from __future__ import absolute_import, division, print_function
import sys
sys.path.insert(0, '.')
import interview_prep as ip


def test_median_pivot(vals=[0, 1, 2, 3, 4], pivot_val=2, pivot_idx=2):
    """pytest style test for _median_pivot.

    """
    assert ip.sorting.sorting._median_pivot(vals=vals) == (pivot_val, pivot_idx)
    return None


def test_quicksort(vals=[5, 0, 2, 5, 4, 6, 5, 6], sorted_vals=[0, 2, 4, 5, 5, 5, 6, 6]):
    """pytest style test for quicksort

    """
    assert ip.sorting.sorting.quicksort(vals=vals) == sorted_vals
    return None
