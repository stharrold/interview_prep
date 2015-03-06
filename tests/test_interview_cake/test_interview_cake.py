"""Tests for interview_prep/interview_cake/interview_cake.py
"""

def test_calc_max_profit(prices=[5.,4.,5.,3.,6.,5.,9.,8.,10.,2.,3.], max_profit=7.0):
    """pytest style test for calc_max_profit
    """
    assert calc_max_profit(prices) == max_profit
    return None
