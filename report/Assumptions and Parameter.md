# 3. Assumptions and Parameter Identification

## 3.1 Introduction

The proposed project focuses on optimizing inventory decisions for a hypothetical e-commerce business selling wireless headphones under uncertain customer demand. Since the actual demand is unknown before purchasing inventory, the model requires a set of assumptions and input parameters to represent the business environment.

The parameters used in this project are hypothetical values selected for academic modelling and simulation. They do not represent actual sales or financial records from a real company.

## 3.2 Identification of Model Parameters

The following parameters are considered in the initial stochastic inventory optimization model.

| Parameter | Symbol | Assumed Value |
|---|---|---:|
| Selling price per unit | p | ₹1,500 |
| Purchasing cost per unit | c | ₹800 |
| Holding cost per unsold unit | h | ₹100 |
| Shortage penalty per unmet unit | s | ₹200 |
| Maximum inventory capacity | Qmax | 500 units |
| Average customer demand | μ | 120 units |
| Number of simulation scenarios | N | 10,000 |

### 3.2.1 Selling Price

The selling price represents the amount received by the company for each headphone sold. It is assumed to be ₹1,500 per unit and remains constant throughout the planning period.

### 3.2.2 Purchasing Cost

The purchasing cost represents the amount paid by the company to its supplier for each unit purchased. It is assumed to be ₹800 per unit. The total purchasing cost depends on the inventory quantity selected.

### 3.2.3 Holding Cost

Holding cost represents the additional expense associated with storing unsold inventory. It includes assumed storage, handling and inventory management expenses. A holding cost of ₹100 is considered for each unsold unit.

### 3.2.4 Shortage Penalty

The shortage penalty represents the additional cost associated with unmet customer demand, such as customer dissatisfaction and service-related consequences. It is assumed to be ₹200 per unmet unit. This is an additional penalty and is not treated as the full selling price of a lost sale.

### 3.2.5 Inventory Capacity

The maximum inventory capacity is restricted to 500 units. This assumption limits the purchasing decision to a practical search range and prevents the model from selecting an unlimited inventory quantity.

### 3.2.6 Average Demand

The average customer demand is assumed to be 120 units per planning period. Actual demand may be lower or higher than this value because of customer behaviour and market uncertainty.

## 3.3 Modelling Assumptions

The following assumptions are used to simplify the inventory optimization problem:

1. The business sells only one product, wireless headphones.
2. The model considers a single inventory planning period.
3. Customer demand is uncertain and is not known when the inventory decision is made.
4. Selling price and purchasing cost remain constant during the planning period.
5. Purchasing cost is incurred for every unit ordered.
6. Unsold products incur an additional holding cost.
7. Unsold products have no salvage or recovery value within the modelled planning period.
8. Each unit of unmet demand incurs an additional shortage penalty.
9. Inventory quantity must be a non-negative integer.
10. The maximum permitted inventory quantity is 500 units.

## 3.4 Demand Data and Probability Distribution

Since actual company sales data are unavailable, the project initially uses synthetic demand data generated through a probability distribution.

Customer demand is initially represented using a Poisson distribution:

\[
D \sim \operatorname{Poisson}(120)
\]

where:

- \(D\) represents actual customer demand.
- \(\lambda=120\) represents the assumed average demand.

The Poisson distribution is selected as an initial model for representing non-negative integer demand. However, its assumption that the mean and variance are equal may not represent every real-world demand pattern. Therefore, alternative demand variability assumptions will be examined during sensitivity analysis.

## 3.5 Justification for Synthetic Data

Synthetic data allow the proposed optimization model to be tested without requiring confidential or unavailable company sales records. By generating multiple possible demand scenarios, the project can evaluate inventory decisions under different market conditions.

The generated data are used for simulation and comparison rather than being presented as actual business observations.

## 3.6 Summary

This module establishes the initial business parameters, modelling assumptions and demand-generation approach for the proposed stochastic inventory optimization system. These inputs form the foundation for the mathematical formulation, Monte Carlo simulation and optimization procedures developed in the following modules.