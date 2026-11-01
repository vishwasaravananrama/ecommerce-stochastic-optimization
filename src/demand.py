import numpy as np


def negbin_params(mean, variance):
    """Convert a target mean and variance into NumPy's (n, p) for the negative binomial."""
    if variance <= mean:
        raise ValueError("Negative binomial needs variance > mean.")
    p = mean / variance
    n = mean**2 / (variance - mean)
    return n, p


def generate_demand(distribution, mean, size, seed, variance=None):
    """Generate integer demand scenarios ("poisson" or "negbin")."""
    rng = np.random.default_rng(seed)
    if distribution == "poisson":
        return rng.poisson(lam=mean, size=size)
    if distribution == "negbin":
        if variance is None:
            raise ValueError("Provide a variance for the negative binomial.")
        n, p = negbin_params(mean, variance)
        return rng.negative_binomial(n, p, size=size)
    raise ValueError("distribution must be 'poisson' or 'negbin'")
