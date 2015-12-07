#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Pytests for interview_prep/interview_prep/probability/probability.py

"""


# Import standard packages.
import os
import sys
# Import installed packages.
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.probability.probability as pr


def test_myfunc() -> None:
    test_myint = pr.myfunc()
    assert test_myint == 5
    return None
