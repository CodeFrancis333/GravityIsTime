import os
import numpy as np
import matplotlib.pyplot as plt

z_points   = np.array([0.15, 0.32, 0.57, 0.80])

res_tau    = np.array([ 0.8,  1.2, -1.0,  0.4])
res_lcdm   = np.array([-1.6,  1.9, -1.4,  1.6])

chi2_tau  = np.sum(res_tau**2)
chi2_lcdm = np.sum(res_lcdm**2)

print(f"χ² (τ-model)   = {chi2_tau:.2f}  for 4 points")
print(f"χ² (ΛCDM)      = {chi2_lcdm:.2f}  for 4 points")

plt.figure(figsize=(6,4))
plt.axhline(0, color="k", lw=0.5)
plt.scatter(z_points, res_tau,  marker="s", color="C3", s=60,
            label=r"$\tau$-model")
plt.scatter(z_points, res_lcdm, marke
