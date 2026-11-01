import numpy as np
from scipy import stats

from src.demand import generate_demand, negbin_params
from src.optimization import find_optimal_q
from src.deterministic import find_deterministic_q
from src.evaluation import evaluate_policy, paired_difference


def theory_q(dist, mean, variance, costs):
    """Newsvendor quantity: smallest Q with P(D <= Q) >= Cu / (Cu + Co)."""
    cu = costs["p"] - costs["c"] + costs["s"]     # gain from one more unit that sells
    co = costs["c"] + costs["h"]                  # loss from one more unit that stays unsold
    ratio = cu / (cu + co)
    if dist == "poisson":
        q = stats.poisson.ppf(ratio, mean)
    else:
        n, p = negbin_params(mean, variance)
        q = stats.nbinom.ppf(ratio, n, p)
    return int(q), ratio


def run_case(label, dist, mean, variance, costs, q_max, size, seed_train, seed_test):
    """Solve one scenario: choose Q on training data, compare policies on test data."""
    train = generate_demand(dist, mean, size, seed_train, variance=variance)
    test = generate_demand(dist, mean, size, seed_test, variance=variance)

    opt = find_optimal_q(train, q_max, **costs)
    q_star = opt["best_q"]
    det = find_deterministic_q(mean, q_max, **costs)
    q_det = det["best_q"]

    r_star = evaluate_policy(q_star, test, **costs)
    r_det = evaluate_policy(q_det, test, **costs)
    diff, se = paired_difference(r_star["profits"], r_det["profits"])
    q_theory, ratio = theory_q(dist, mean, variance, costs)

    return {
        "case": label,
        "mean_demand": mean,
        "demand_variance": mean if dist == "poisson" else variance,
        "critical_ratio": ratio,
        "Q_star": q_star,
        "Q_theory": q_theory,
        "Q_det": q_det,
        "exp_profit_train": opt["best_profit"],
        "det_predicted_profit": det["best_profit"],
        "test_profit_stoch": r_star["avg_profit"],
        "test_profit_det": r_det["avg_profit"],
        "diff_stoch_minus_det": diff,
        "diff_ci95_half_width": 1.96 * se,
        "stockout_freq_stoch": r_star["stockout_freq"],
        "p5_profit_stoch": r_star["p5_profit"],
        "max_demand_train": int(train.max()),
    }