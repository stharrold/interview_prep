#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""My answers to example probability questions from Society of Actuaries Exam P.

See Also:
    * 20151206_edu-exam-p-sample-quest.pdf from [1]_.
    * 20151206_edu-exam-p-sample-sol.pdf from [2]_.

References:
    .. [1] http://www.soa.org/Files/Edu/edu-exam-p-sample-quest.pdf
    .. [2] http://www.soa.org/Files/Edu/edu-exam-p-sample-sol.pdf
    
"""


# Import standard packages.
# Import installed packages.
# Import local packages.
import interview_prep.utils as utils


def q1(
    pr_a:float=0.28, pr_b:float=0.29, pr_c:float=0.19,
    pr_aib:float=0.14, pr_aic:float=0.12, pr_bic:float=0.10,
    pr_aibic:float=0.08) -> float:
    r"""Calculate P(not(A union B union C)).
    
    Args:
        pr_[a,b,c] (float): [P(A), P(B), P(C)]
        pr_[aib,aic,bic] (float): [P(A intr B), P(A intr C), P(B intr C)]
        pr_aibic (float): P(A intr B intr C)
    
    Returns:
        pr_naubuc (float): P(not(A union B union C))
    
    Notes:
        * P(not(A union B union C)) = (1 - (
            P(A) + P(B) + P(C) - P(A intr B) - P(A intr C)
            - P(B intr C) + P(A intr B intr C)))

    """
    # Check arguments.
    utils.check_arguments(
        antns=q1.__annotations__,
        lcls=locals())
    # Calculate union complement.
    pr_naubuc = 1.0 - (pr_a + pr_b + pr_c - pr_aib - pr_aic - pr_bic + pr_aibic)
    return pr_naubuc
