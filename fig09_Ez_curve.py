import os
import numpy as np
import matplotlib.pyplot as plt

h          = 0.7
Omega_r0   = 4.2e-5 / h**2        # photons + neutrinos 

# Fiducial ΛCDM
Om_m_LCDM  = 0.31
Om_Lam     = 0.69

# Scalar-time
Om_m_ST    = 0.50
Om_tau_ST  = 0.62
z = np.logspace(-2, 1, 500)     #redshift

def E_LCDM(z):
    return np.sqrt(Omega_r0*(1+z)**4 +
                   Om_m_LCDM*(1+z)**3 +
                   Om_Lam)

def E_scalar(z):
    return np.sqrt(Omega_r0*(1+z)**4 +
                   Om_m_ST*(1+z)**3 +
                   Om_tau_ST*(1+z)**2)

E_LCDM_vals = E_LCDM(z)
E_ST_vals   = E_scalar(z)


frac_diff = (E_ST_vals - E_LCDM_vals) / E_LCDM_vals
max_dev   = np.max(np.abs(frac_diff))*100
print(f"Max |ΔE/E| over 0.01<z<10  = {max_dev:.2f} %")

for z_test in [0.1, 1, 3]:
    idx = np.abs(z - z_test).argmin()
    print(f"z={z_test:<3}  :  E_ST = {E_ST_vals[idx]:.3f}, "
          f"E_LCDM = {E_LCDM_vals[idx]:.3f},  "
          f"Δ = {frac_diff[idx]*100:+.2f} %")

plt.figure(figsize=(6,4))
plt.loglog(z, E_LCDM_vals, lw=2, color="gray", label=r"$\Lambda$CDM")
plt.loglog(z, E_ST_vals,   lw=2, ls="--", color="C0", label="Scalar-time")

plt.xlabel("Red-shift $z$")
plt.ylabel("$E(z)=H(z)/H_0$")
plt.xlim(0.01, 10)
plt.ylim(0.5, 20)
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.legend()
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure9_Ez_Curve.png", dpi=150)
plt.show()
