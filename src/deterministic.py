import numpy as np
from src.profit import profit


def deterministic_profit_curve(fixed_demand, q_values, **costs):
    """Profit for every Q when demand is known and fixed."""
    q_values = np.asarray(q_values)
    return profit(q_values, fixed_demand, **costs)


def find_deterministic_q(fixed_demand, q_max, **costs):
    """Evaluate every integer Q from 0 to q_max for a fixed demand and return the best."""
    q_values = np.arange(0, q_max + 1)
    profits = deterministic_profit_curve(fixed_demand, q_values, **costs)
    best_index = int(np.argmax(profits))
    return {
        "best_q": int(q_values[best_index]),
        "best_profit": float(profits[best_index]),
        "q_values": q_values,
        "profits": profits,
    }