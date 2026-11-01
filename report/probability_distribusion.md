# 5. Probability Distribution and Uncertainty Modelling

## 5.1 Introduction

Customer demand is uncertain and cannot be determined exactly before the inventory purchasing decision is made. Therefore, a probability distribution is required to represent different possible demand outcomes.

This project initially uses the Poisson distribution to model customer demand for wireless headphones.

## 5.2 Selection of Poisson Distribution

The Poisson distribution is a discrete probability distribution used to represent the number of occurrences of an event within a fixed interval under specified assumptions.

It is suitable as an initial academic model for representing the number of product units demanded during a planning period.

The demand variable is defined as:

\[
D\sim Poisson(\lambda)
\]

For this project:

\[
\lambda=120
\]

Therefore:

\[
D\sim Poisson(120)
\]

The assumed average customer demand is 120 units per planning period.

## 5.3 Probability Mass Function

The probability mass function of the Poisson distribution is:

\[
P(D=k)=\frac{e^{-\lambda}\lambda^k}{k!}
\]

where:

- \(D\) represents customer demand.
- \(k\) represents a particular demand value.
- \(\lambda\) represents the average demand.
- \(e\) is the mathematical constant.
- \(k!\) represents the factorial of k.

This function determines the probability of observing a particular demand value.

## 5.4 Statistical Properties

The Poisson distribution has the following properties:

**Mean:**

\[
E[D]=\lambda=120
\]

**Variance:**

\[
Var(D)=\lambda=120
\]

**Standard deviation:**

\[
SD(D)=\sqrt{\lambda}=\sqrt{120}\approx10.95
\]

These properties describe the expected demand and its variability.

## 5.5 Limitation of the Poisson Distribution

One important limitation of the Poisson distribution is that its theoretical mean and variance are equal.

In real-world e-commerce environments, demand may exhibit greater variability because of seasonal changes, promotional activities, customer preferences and other market conditions.

Therefore, the Poisson distribution may not fully represent every possible demand pattern.

## 5.6 Alternative Distribution: Negative Binomial

To examine the effect of greater demand variability, the Negative Binomial distribution is considered as an alternative model.

Using the mean-dispersion parameterization:

\[
E[D]=\mu
\]

\[
Var(D)=\mu+\frac{\mu^2}{r}
\]

where \(\mu\) represents mean demand and \(r\) is the dispersion parameter.

For an illustrative alternative scenario:

\[
\mu=120,\quad r=120
\]

The variance becomes:

\[
Var(D)=120+\frac{120^2}{120}=240
\]

Thus, the Poisson and Negative Binomial distributions can represent the same average demand while having different levels of variability.

## 5.7 Application in the Project

The Poisson distribution will be used as the initial demand-generation model. Multiple demand scenarios will be generated through Monte Carlo simulation to estimate expected profit for different inventory decisions.

The Negative Binomial distribution will be considered in sensitivity analysis to investigate how higher demand variability affects the optimal inventory decision and business performance.

## 5.8 Summary

This module establishes the probability distribution used to represent uncertain customer demand. The Poisson distribution provides the initial demand model, while the Negative Binomial distribution provides an alternative for examining higher demand variability. These distributions form the foundation for synthetic demand generation and Monte Carlo simulation.