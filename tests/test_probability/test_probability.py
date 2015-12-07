#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Pytests for interview_prep/interview_prep/probability/probability.py

"""


# Import standard packages.
import os
import sys
# Import installed packages.
import numpy as np
# Import local packages.
sys.path.insert(0, os.path.curdir)
import interview_prep.probability.probability as pr


def test_q1(
    pr_a:float=0.28, pr_b:float=0.29, pr_c:float=0.19,
    pr_aib:float=0.14, pr_aic:float=0.12, pr_bic:float=0.10,
    pr_aibic:float=0.08, ref_pr_naubuc=0.52) -> None:
    r"""Pytest for q1.
    
    """
    test_pr_naubuc = pr.q1(
        pr_a=pr_a, pr_b=pr_b, pr_c=pr_c,
        pr_aib=pr_aib, pr_aic=pr_aic, pr_bic=pr_bic,
        pr_aibic=pr_aibic)
    assert np.isclose(ref_pr_naubuc, test_pr_naubuc)
    return None
