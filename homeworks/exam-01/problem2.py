# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

# %%
group1 = [11.4, 11.0, 11.3, 9.5]  # 0.25 tsp
group2 = [27.8, 29.2, 26.8, 26.0]  # 0.5 tsp
group3 = [47.6, 47.0, 47.3, 45.5]  # 0.75 tsp
group4 = [61.6, 62.4, 63.0, 63.9]  # 1 tsp

data = pd.DataFrame({
    'RiseHeight': group1 + group2 + group3 + group4,
    'BakingPowder': ['0.25 tsp']*4 + ['0.5 tsp']*4 + ['0.75 tsp']*4 + ['1 tsp']*4
})
data

# %%
# Fit the model (ANOVA)
model = smf.ols('RiseHeight ~ BakingPowder', data=data).fit()

# Perform ANOVA
anova_results = anova_lm(model)

# Output the ANOVA table
anova_results


# %%
n = 4

# Treatment means
means = np.array([np.array(group1).mean(), np.array(group2).mean(), np.array(group3).mean(), np.array(group4).mean()])

# Contrast coefficients for linear trend
c = np.array([-3, -1, 1, 3])

# Compute contrast value
L = np.sum(c * means)

# Compute sum of squares for the contrast
SS_contrast = (L**2) / (np.sum(c**2) / n)

# Mean square for the contrast (df=1)
MS_contrast = SS_contrast

# Residual sum of squares from previous ANOVA
SS_residual = 13.4875
df_residual = 12

# Mean square error
MSE = SS_residual / df_residual

# F-statistic for the contrast
F = MS_contrast / MSE

# p-value
p_value = 1 - stats.f.cdf(F, 1, df_residual)

print("Linear contrast L =", L)
print("SS_contrast =", SS_contrast)
print("F-statistic =", F)
print("p-value =", p_value)

