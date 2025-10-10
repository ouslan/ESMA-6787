import numpy as np
from scipy.stats import f, ncf
import matplotlib.pyplot as plt
import seaborn as sns

k = 5
mus = np.array([1.5, 2, 1, -1.5, -3])
sigma = 5
alpha = 0.05

mu_bar = np.mean(mus)
ssd = np.sum((mus - mu_bar) ** 2)
df1 = k - 1


def power_calc(n):
    df2 = k * (n - 1)
    lambda2 = n * ssd / sigma**2
    F_crit = f.ppf(1 - alpha, df1, df2)
    power = 1 - ncf.cdf(F_crit, df1, df2, lambda2)
    return power, df2, lambda2, F_crit


n_values = np.arange(2, 101)
powers = []

for n in n_values:
    power, _, _, _ = power_calc(n)
    powers.append(power)

powers = np.array(powers)
n_min = n_values[np.where(powers >= 0.95)[0][0]]
print(f"Minimal sample size per group for power >= 0.95 is: {n_min}")

# Plot power curve
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(n_values, powers, label="Power")
plt.axhline(0.95, color="red", linestyle="--", label="Power = 0.95")
plt.axvline(n_min, color="blue", linestyle=":", label=f"Min n = {n_min}")
plt.xlabel("Sample Size per Group (n)")
plt.ylabel("Power")
plt.title("Power of ANOVA F-test vs Sample Size per Group")
plt.legend()
plt.tight_layout()
plt.show()

# Plot F distributions for n_min
_, df2_min, lambda2_min, F_crit_min = power_calc(n_min)
x = np.linspace(0, 14, 1000)
f_central = f.pdf(x, df1, df2_min)
f_noncentral = ncf.pdf(x, df1, df2_min, lambda2_min)

plt.figure(figsize=(10, 6))
plt.plot(
    x,
    f_central,
    color="red",
    linestyle="-",
    label=f"Central F (lambda2=0), df=({df1},{df2_min})",
)
plt.plot(
    x,
    f_noncentral,
    color="blue",
    linestyle="--",
    label=f"Non-central F (labda2={lambda2_min:.2f}), df=({df1},{df2_min})",
)
plt.axvline(
    F_crit_min,
    color="black",
    linestyle="dashed",
    label=f"Critical value = {F_crit_min:.4f}",
)
plt.xlabel("F statistic")
plt.ylabel("Density")
plt.title(f"Central vs Non-central F-distributions for n = {n_min}")
plt.legend()
plt.tight_layout()
plt.show()
