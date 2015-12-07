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


def myfunc(myint:int=5) -> None:
    # Check arguments.
    utils.check_arguments(
        antns=myfunc.__annotations__,
        lcls=locals())
    return myint


