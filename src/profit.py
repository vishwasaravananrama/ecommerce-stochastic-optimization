import numpy as np


def profit(Q, D, p=1500, c=800, h=100, s=200):
    """
    Profit for order quantity Q and demand D (works for single numbers or arrays).

    p: selling price, c: purchase cost, h: holding cost per unsold unit,
    s: shortage penalty per unmet unit (an extra penalty, NOT lost revenue).
    """
    Q = np.asarray(Q)
    D = np.asarray(D)
    units_sold = np.minimum(Q, D)
    unsold = np.maximum(Q - D, 0)
    unmet = np.maximum(D - Q, 0)
    return p * units_sold - c * Q - h * unsold - s * unmet