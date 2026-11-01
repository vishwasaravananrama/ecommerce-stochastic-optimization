import numpy as np
from src.profit import profit


def expected_profit(Q, demand, **costs):
    """
    Monte Carlo estimate of expected profit for order quantity Q.
    Returns (mean profit, standard error).
    """
    profits = profit(Q, demand, **costs)
    mean = profits.mean()
    std_error = profits.std(ddof=1) / np.sqrt(len(profits))
    return mean, std_error


def running_mean(Q, demand, **costs):
    """Average profit using the first 1, 2, 3, ... N scenarios (for convergence plots)."""
    profits = profit(Q, demand, **costs)
    return np.cumsum(profits) / np.arange(1, len(profits) + 1)