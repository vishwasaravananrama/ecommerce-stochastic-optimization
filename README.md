# Stochastic Optimization for E-commerce Inventory Management Under Uncertain Customer Demand

Course: 21AIE321T Stochastic Decision Making, Assignment IV (Mini Project)
Student: [your name, roll number]

## Overview
An e-commerce seller must choose how many wireless headphones (Q) to buy before demand (D) is known.
Expected profit is maximized with Monte Carlo simulation and an exhaustive search over Q = 0 to 500,
and compared with a deterministic model that assumes demand is exactly 120.

All costs and demand data are illustrative assumptions and synthetic data, not real company data.

## Model
Profit(Q, D) = p*min(Q,D) - c*Q - h*max(Q-D,0) - s*max(D-Q,0)
p = 1500, c = 800, h = 100, s = 200, Qmax = 500, demand ~ Poisson(120)
(negative binomial with variance 240, 480, 960 for variability experiments)

## Folder structure
- notebooks/  step-by-step analysis (02 to 09)
- src/        reusable code (profit, demand, simulation, optimization, deterministic, evaluation, sensitivity)
- tests/      unit tests
- data/       synthetic demand (raw, processed)
- results/    graphs, tables, experiment outputs
- report/     figures and Final_Report.pdf

## How to run
1. Create and activate a virtual environment, then: pip install -r requirements.txt
2. Run the notebooks in order: 03, 04, 05, 06, 07, 08, 09 (select the venv kernel, Run All).
3. Run the tests from the project root: python tests/test_model.py

## Key results (seed 42 for training, seed 2026 for testing)
- Stochastic-optimal Q* = 120 and deterministic Q = 120, so the policies tie in the base case.
- Test profit at Q = 120 is about Rs 76,151, versus the deterministic prediction of Rs 84,000.
- Higher demand variability lowers profit and raises risk, but moves Q* only from 120 to 117.
- Cost changes move Q* by a few units; stochastic gains are small (at most 0.65% of profit).

## Limitations
[2 to 3 sentences in your own words]