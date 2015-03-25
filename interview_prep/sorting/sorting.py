#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My iterations of sorting algorithms.

"""


from __future__ import absolute_import, division, print_function
import copy
import pdb


def _median_pivot(vals):
    """Compute the pivot value for quicksort and the index of the pivot value.
    
    Args:
        vals: list
            Values to be sorted. Sequence must be indexed for random access.

    Returns:
        pivot_val: hashable
            Value to be used as the pivot value.
        pivot_idx: int
            Index of `pivot_val` in `vals`.

    See Also:
        quicksort

    Notes:
        - Chooses the median of the first, middle, and last elements
        as the pivot value.
        - May not preserve stable sorting.
    
    """
    # Evaluate only three potential pivot values per (sub)sequence.
    pivot_idxs = [0, int(len(vals)/2), -1]
    pivot_vals = [vals[idx] for idx in pivot_idxs]
    if (pivot_vals[0] <= pivot_vals[1] <= pivot_vals[2] or
        pivot_vals[2] <= pivot_vals[1] <= pivot_vals[0]):
        (pivot_val, pivot_idx) = (pivot_vals[1], pivot_idxs[1])
    elif (pivot_vals[1] <= pivot_vals[0] <= pivot_vals[2] or
          pivot_vals[2] <= pivot_vals[0] <= pivot_vals[1]):
        (pivot_val, pivot_idx) = (pivot_vals[0], pivot_idxs[0])
    else:
        (pivot_val, pivot_idx) = (pivot_vals[2], pivot_idxs[2])
    return (pivot_val, pivot_idx)


def quicksort(vals):
    """Sort using an implementation of quicksort.
   
    Args:
        vals: list
            Values to be sorted must be indexed for random access.

    Returns:
        sorted_vals: list
            Values sorted by quicksort.

    Notes:
        - Input list is copied to avoid modifying list in caller’s scope.
        - May not preserve stable sorting.
        - Complexity:
            Ideal:
                Time: O(n*lg(n))
                Space: O(1)
            Realized:
                Time: O(n*lg(n))
                Space: O(n)

    """
    # FILO stack of subsequences from `vals` which need to be sorted.
    subseqs_to_sort = []
    orig_len_vals = len(vals)
    # Don’t modify list in caller’s scope.
    tmp_vals = copy.deepcopy(vals)
    sorted_vals = []
    # TODO: check while cond wrt subseqs_to_sort
    while len(sorted_vals) < orig_len_vals:
        # TODO: look for runs as atomic elements to save comparisons
        # TODO: use pop and reversed to sort in place and save memory
        # TODO: restructure to avoid needing singleton [pivot_val]
        (pivot_val, pivot_idx) = _median_pivot(tmp_vals)
        tmp_vals = tmp_vals[:pivot_idx] + tmp_vals[pivot_idx+1:]
        tmp_vals_lt = []
        tmp_vals_gteq = []
        while len(tmp_vals) > 0:
            val = tmp_vals.pop()
            if val < pivot_val:
                tmp_vals_lt.append(val)
            else:
                tmp_vals_gteq.append(val)
        if len(tmp_vals_lt) <= 1: lt_sorted = True
        else: lt_sorted = False
        if len(tmp_vals_gteq) <= 1: gteq_sorted = True
        else: gteq_sorted = False
        # Order of appending in sorted list is from least to greatest.
        if lt_sorted:
            sorted_vals.extend(tmp_vals_lt)
            sorted_vals.append(pivot_val)
            if gteq_sorted:
                sorted_vals.extend(tmp_vals_gteq)
        # Order of stack to sort is from greatest to least.
        if not lt_sorted and len(tmp_vals_lt) > 1:
            subseqs_to_sort.append(tmp_vals_gteq)
            subseqs_to_sort.append([pivot_val])
            subseqs_to_sort.append(tmp_vals_lt)
        else:
            if not gteq_sorted and len(tmp_vals_gteq) > 1:
                subseqs_to_sort.append(tmp_vals_gteq)
        if len(subseqs_to_sort) > 0:
            tmp_vals = subseqs_to_sort.pop()
    return sorted_vals
