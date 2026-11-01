import numpy as np
from src.profit import profit


def evaluate_policy(Q, demand, **costs):
    """Evaluate a fixed order quantity Q on a set of demand scenarios."""
    demand = np.asarray(demand)
    profits = profit(Q, demand, **costs)
    return {
        "Q": int(Q),
        "profits": profits,
        "avg_profit": float(profits.mean()),
        "se_profit": float(profits.std(ddof=1) / np.sqrt(demand.size)),
        "std_profit": float(profits.std(ddof=1)),
        "p5_profit": float(np.percentile(profits, 5)),
        "median_profit": float(np.median(profits)),
        "p95_profit": float(np.percentile(profits, 95)),
        "avg_unsold": float(np.maximum(Q - demand, 0).mean()),
        "avg_unmet": float(np.maximum(demand - Q, 0).mean()),
        "stockout_freq": float((demand > Q).mean()),
    }


def paired_difference(profits_a, profits_b):
    """Mean and standard error of (profits_a - profits_b), scenario by scenario."""
    diff = np.asarray(profits_a) - np.asarray(profits_b)
    return float(diff.mean()), float(diff.std(ddof=1) / np.sqrt(diff.size))