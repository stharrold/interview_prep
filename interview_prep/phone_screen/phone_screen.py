#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My interations of answers to
https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

"""


from __future__ import absolute_import, division, print_function


def reverse_string(string):
    """Reverse a string.
    
    Args:
        string: str
            String with __getslice__ method.

    Returns:
        revd: str
            Reversed `string`.

    Notes:
        - Complexity:
            Time: O(n)
            Space: O(1)

    References:
        ..[1] http://stackoverflow.com/questions/931092/reverse-a-string-in-python

    """
    return string[::-1]
