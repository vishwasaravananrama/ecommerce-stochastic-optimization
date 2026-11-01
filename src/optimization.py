import numpy as np
from src.profit import profit


def expected_profit_curve(demand, q_values, **costs):
    """
    Expected profit (Monte Carlo mean) and standard error for every Q in q_values.
    Builds a table with one row per Q and one column per demand scenario.
    """
    demand = np.asarray(demand)
    q_values = np.asarray(q_values)
    profits = profit(q_values[:, None], demand[None, :], **costs)
    means = profits.mean(axis=1)
    std_errors = profits.std(axis=1, ddof=1) / np.sqrt(demand.size)
    return means, std_errors


def find_optimal_q(demand, q_max, **costs):
    """Evaluate every integer Q from 0 to q_max and return the best one."""
    q_values = np.arange(0, q_max + 1)
    means, std_errors = expected_profit_curve(demand, q_values, **costs)
    best_index = int(np.argmax(means))      # first maximum if there is a tie
    return {
        "best_q": int(q_values[best_index]),
        "best_profit": float(means[best_index]),
        "best_se": float(std_errors[best_index]),
        "q_values": q_values,
        "means": means,
        "std_errors": std_errors,
    }