#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for interview_prep/phone_screen/phone_screen.py

"""


from __future__ import absolute_import, division, print_function
import sys
sys.path.insert(0, '.')
import interview_prep as ip


def test_reverse_string(string=’asdfjkl;’, revd=’;lkjfdsa’):
    """pytest style test for reverse_string.

    """
    assert ip.phone_screen.phone_screen.reverse_string(string=string) == revd
    return None
