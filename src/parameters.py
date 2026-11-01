# All model assumptions in one place. ILLUSTRATIVE values, not real company data.

# Business parameters
P = 1500          # selling price per unit (Rs)
C = 800           # purchasing cost per unit (Rs)
H = 100           # holding cost per unsold unit (Rs)
S = 200           # shortage penalty per unmet unit (Rs), an extra penalty, not lost revenue
Q_MAX = 500       # maximum inventory capacity (units)

COSTS = dict(p=P, c=C, h=H, s=S)

# Demand parameters
MEAN_DEMAND = 120
NB_VARIANCES = {"negbin_var240": 240, "negbin_var480": 480}

# Simulation settings
N_SCENARIOS = 10_000
SEED_TRAIN = 42
SEED_TEST = 2026

# Sensitivity experiment A
MEAN_LEVELS = [80, 100, 120, 150, 180]
