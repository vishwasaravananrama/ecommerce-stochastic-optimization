# 4. Mathematical Model Formulation

## 4.1 Problem Description

The objective of the proposed project is to determine the optimal inventory quantity for a hypothetical e-commerce business selling wireless headphones under uncertain customer demand.

The company must decide how many units to purchase before actual demand is known. Purchasing insufficient inventory may result in unmet demand, while purchasing excess inventory may lead to additional holding costs.

Therefore, a stochastic optimization model is formulated to maximize expected profit while satisfying inventory constraints.

## 4.2 Decision Variable

The decision variable represents the quantity of headphones purchased by the company.

\[
Q=\text{Number of headphones purchased}
\]

The decision variable must be a non-negative integer.

## 4.3 Uncertain Variable

Customer demand is represented by the random variable:

\[
D=\text{Actual customer demand}
\]

For the initial model, demand is assumed to follow a Poisson distribution with an average demand of 120 units.

\[
D\sim Poisson(120)
\]

## 4.4 Profit Function

The total profit depends on revenue, purchasing cost, holding cost and shortage penalty.

The number of units sold is:

\[
Sales=\min(Q,D)
\]

The unsold inventory is:

\[
Unsold=\max(Q-D,0)
\]

The unmet demand is:

\[
Shortage=\max(D-Q,0)
\]

Therefore, the profit function is formulated as:

\[
\begin{aligned}
\Pi(Q,D)={}&p\min(Q,D)-cQ\\
&-h\max(Q-D,0)\\
&-s\max(D-Q,0)
\end{aligned}
\]

Substituting the assumed parameters:

\[
\begin{aligned}
\Pi(Q,D)={}&1500\min(Q,D)-800Q\\
&-100\max(Q-D,0)\\
&-200\max(D-Q,0)
\end{aligned}
\]

Here, the shortage penalty represents an additional cost associated with unmet customer demand and does not represent the full value of lost sales.

## 4.5 Objective Function

Since actual customer demand is uncertain, maximizing profit for only one demand scenario is insufficient.

The model aims to maximize expected profit across possible demand outcomes.

\[
\boxed{\max_Q E[\Pi(Q,D)]}
\]

This objective considers the probability of different demand outcomes and identifies the inventory quantity that provides the highest expected profit.

## 4.6 Constraints

The inventory decision must satisfy the following constraints:

**Non-negativity constraint:**

\[
Q\geq0
\]

**Maximum inventory capacity:**

\[
Q\leq500
\]

**Integer constraint:**

\[
Q\in\mathbb Z
\]

Combining these constraints:

\[
Q\in\{0,1,2,\ldots,500\}
\]

## 4.7 Complete Mathematical Model

The proposed stochastic optimization model is:

\[
\max_Q E[\Pi(Q,D)]
\]

Subject to:

\[
0\leq Q\leq500
\]

\[
Q\in\mathbb Z
\]

where:

\[
D\sim Poisson(120)
\]

and:

\[
\begin{aligned}
\Pi(Q,D)={}&1500\min(Q,D)-800Q\\
&-100\max(Q-D,0)\\
&-200\max(D-Q,0)
\end{aligned}
\]

## 4.8 Summary

The mathematical formulation defines the inventory decision variable, uncertain customer demand, profit calculation, expected-profit objective and inventory constraints. This formulation provides the foundation for implementing Monte Carlo simulation and stochastic optimization in Python.