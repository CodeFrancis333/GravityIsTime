import os
import numpy as np
import matplotlib.pyplot as plt

Omega_m0   = 0.50
Omega_tau0 = 0.62
z_cross = Omega_tau0 / Omega_m0 - 1
print(f"Analytic cross-over  z* = Ωτ0/Ωm0 − 1  = {z_cross:.2f}")

z = np.logspace(-2, 1, 400)      # 0.01 → 10

Omega_m   = Omega_m0   * (1+z)**3
Omega_tau = Omega_tau0 * (1+z)**2

def fractions(zval):
    m = Omega_m0   * (1+zval)**3
    t = Omega_tau0 * (1+zval)**2
    s = m + t
    return m/s, t/s

for z_test in [0, 0.8, 2]:
    f_m, f_tau = fractions(z_test)
    print(f"z={z_test:>4.1f} : matter {f_m:.2%} | τ-field {f_tau:.2%}")

plt.figure(figsize=(6,4))
plt.loglog(z, Omega_m/Omega_m0,   lw=2, color="C0", label=r"$\Omega_m(z)$")
plt.loglog(z, Omega_tau/Omega_tau0, lw=2, ls="--", color="C3",
           label=r"$\Omega_\tau(z)$")

plt.axvline(z_cross, color="gray", ls=":", lw=1)
plt.text(z_cross*1.08, 0.3, f"z* ≈ {z_cross:.2f}", color="gray")

plt.xlabel("Red-shift z")
plt.ylabel(r"$\Omega(z)\ /\ \Omega_0$")
plt.title("Matter vs. clock-field energy density")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure5_Matter_Energy_Densities.png", dpi=150)
plt.show()
