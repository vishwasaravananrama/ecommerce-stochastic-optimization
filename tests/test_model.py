import os
import sys
import unittest

import numpy as np
from scipy import stats

# Make the project root importable when running this file directly
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.parameters import COSTS, Q_MAX, MEAN_DEMAND, N_SCENARIOS, SEED_TRAIN, SEED_TEST
from src.profit import profit
from src.demand import generate_demand, negbin_params
from src.optimization import find_optimal_q, expected_profit_curve
from src.deterministic import find_deterministic_q
from src.evaluation import evaluate_policy, paired_difference


class TestProfit(unittest.TestCase):
    def test_hand_calculations(self):
        # Q = 120: D=100 -> 52000, D=120 -> 84000, D=130 -> 82000 (worked by hand in Module 07)
        self.assertEqual(profit(120, 100, **COSTS), 52000)
        self.assertEqual(profit(120, 120, **COSTS), 84000)
        self.assertEqual(profit(120, 130, **COSTS), 82000)

    def test_shortage_not_double_counted(self):
        # Q=100, D=130: revenue on 100 units only, minus purchase, minus penalty on 30 unmet units
        # 1500*100 - 800*100 - 200*30 = 150000 - 80000 - 6000 = 64000
        self.assertEqual(profit(100, 130, **COSTS), 64000)

    def test_array_input(self):
        result = profit(120, np.array([100, 120, 130]), **COSTS)
        self.assertEqual(result.tolist(), [52000, 84000, 82000])

    def test_zero_order(self):
        # Q = 0, D = 50: no revenue, no purchase, no holding; penalty 200*50 = 10000
        self.assertEqual(profit(0, 50, **COSTS), -10000)


class TestDemand(unittest.TestCase):
    def test_poisson_valid(self):
        d = generate_demand("poisson", MEAN_DEMAND, N_SCENARIOS, SEED_TRAIN)
        self.assertEqual(len(d), N_SCENARIOS)
        self.assertTrue(np.issubdtype(d.dtype, np.integer))
        self.assertTrue((d >= 0).all())

    def test_reproducible(self):
        a = generate_demand("poisson", MEAN_DEMAND, 1000, 7)
        b = generate_demand("poisson", MEAN_DEMAND, 1000, 7)
        self.assertTrue(np.array_equal(a, b))

    def test_negbin_theory(self):
        # The conversion must keep the mean and give the requested variance
        for variance in (240, 480, 960):
            n, p = negbin_params(120, variance)
            mean, var = stats.nbinom.stats(n, p, moments="mv")
            self.assertAlmostEqual(float(mean), 120.0, places=6)
            self.assertAlmostEqual(float(var), float(variance), places=6)

    def test_negbin_sample(self):
        d = generate_demand("negbin", 120, 100_000, 42, variance=480)
        self.assertLess(abs(d.mean() - 120), 0.5)
        self.assertLess(abs(d.var(ddof=1) - 480) / 480, 0.10)
        self.assertTrue((d >= 0).all())

    def test_negbin_invalid(self):
        with self.assertRaises(ValueError):
            negbin_params(120, 100)          # variance must exceed the mean
        with self.assertRaises(ValueError):
            generate_demand("negbin", 120, 10, 1)   # variance missing


class TestOptimizer(unittest.TestCase):
    def test_bounds(self):
        d = generate_demand("poisson", MEAN_DEMAND, 2000, 3)
        res = find_optimal_q(d, Q_MAX, **COSTS)
        self.assertEqual(len(res["q_values"]), Q_MAX + 1)
        self.assertEqual(int(res["q_values"].min()), 0)
        self.assertEqual(int(res["q_values"].max()), Q_MAX)
        self.assertTrue(0 <= res["best_q"] <= Q_MAX)

    def test_matches_simple_loop(self):
        d = generate_demand("poisson", MEAN_DEMAND, 500, 1)
        res = find_optimal_q(d, 200, **COSTS)
        loop_means = np.array([profit(q, d, **COSTS).mean() for q in range(201)])
        self.assertTrue(np.allclose(res["means"], loop_means))
        self.assertEqual(res["best_q"], int(np.argmax(loop_means)))

    def test_constant_demand(self):
                # Demand is always 50 -> best Q is 50 with profit 1500*50 - 800*50 = 35000
        res = find_optimal_q(np.full(100, 50), Q_MAX, **COSTS)
        self.assertEqual(res["best_q"], 50)
        self.assertAlmostEqual(res["best_profit"], 35000.0)

    def test_exact_poisson_optimum(self):
        # Exact expected profit from the Poisson probabilities (no simulation)
        d_grid = np.arange(0, 401)
        pmf = stats.poisson.pmf(d_grid, MEAN_DEMAND)
        q_values = np.arange(0, Q_MAX + 1)
        exact = profit(q_values[:, None], d_grid[None, :], **COSTS) @ pmf
        self.assertEqual(int(q_values[np.argmax(exact)]), 120)


class TestDeterministic(unittest.TestCase):
    def test_base_case(self):
        res = find_deterministic_q(120, Q_MAX, **COSTS)
        self.assertEqual(res["best_q"], 120)
        self.assertEqual(res["best_profit"], 84000)

    def test_other_demand(self):
        res = find_deterministic_q(80, Q_MAX, **COSTS)
        self.assertEqual(res["best_q"], 80)
        self.assertEqual(res["best_profit"], 56000)


class TestEvaluation(unittest.TestCase):
    def test_hand_metrics(self):
        # Q = 120, demand = 100, 120, 130 -> profits 52000, 84000, 82000
        r = evaluate_policy(120, np.array([100, 120, 130]), **COSTS)
        self.assertAlmostEqual(r["avg_profit"], 218000 / 3)
        self.assertAlmostEqual(r["avg_unsold"], 20 / 3)
        self.assertAlmostEqual(r["avg_unmet"], 10 / 3)
        self.assertAlmostEqual(r["stockout_freq"], 1 / 3)

    def test_paired_difference_zero(self):
        x = np.array([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(paired_difference(x, x), (0.0, 0.0))


class TestIndependence(unittest.TestCase):
    def test_train_and_test_differ(self):
        self.assertNotEqual(SEED_TRAIN, SEED_TEST)
        train = generate_demand("poisson", MEAN_DEMAND, N_SCENARIOS, SEED_TRAIN)
        test = generate_demand("poisson", MEAN_DEMAND, N_SCENARIOS, SEED_TEST)
        self.assertFalse(np.array_equal(train, test))

    def test_saved_training_csv_matches(self):
        import pandas as pd
        path = os.path.join(ROOT, "data", "processed", "synthetic_demand_clean.csv")
        if not os.path.isfile(path):
            self.skipTest("training CSV not found")
        saved = pd.read_csv(path)["poisson"].to_numpy()
        regenerated = generate_demand("poisson", MEAN_DEMAND, N_SCENARIOS, SEED_TRAIN)
        self.assertTrue(np.array_equal(saved, regenerated))


if __name__ == "__main__":
    unittest.main(verbosity=2)