import os
import numpy as np
import matplotlib.pyplot as plt

h      = 0.7
Omega_r0 = 4.2e-5 / h**2         # ≈ 8.6 × 10⁻⁵
# fiducial ΛCDM
Om_m_LCDM = 0.31
Om_Lam    = 0.69
# scalar-time best-fit
Om_m_st   = 0.50
Om_tau_st = 0.62

z = np.logspace(-1, np.log10(1100), 800)

def E_LCDM(z):
    return np.sqrt(Omega_r0*(1+z)**4 + Om_m_LCDM*(1+z)**3 + Om_Lam)

def E_scalar(z):
    return np.sqrt(Omega_r0*(1+z)**4 + Om_m_st*(1+z)**3 + Om_tau_st*(1+z)**2)

E_lcdm = E_LCDM(z)
E_st   = E_scalar(z)

mask      = (z >= 2) & (z <= 1100)
frac_diff = (E_st[mask] - E_lcdm[mask]) / E_lcdm[mask]
max_dev   = np.max(np.abs(frac_diff)) * 100   # %
print(f"Max |ΔE/E| over 2<z<1100  = {max_dev:.2f} %")

plt.figure(figsize=(6,4))

plt.fill_between(z, 0.97*E_lcdm, 1.03*E_lcdm,
                 color="gray", alpha=0.2, label=r"$\pm3\%$ BAO+CMB")

plt.loglog(z, E_lcdm, lw=2, color="gray", label=r"$\Lambda$CDM fiducial")
plt.loglog(z, E_st,   lw=2, ls="--", color="C0", label="Scalar-time")

plt.xlabel("Red-shift $z$")
plt.ylabel("$E(z)=H(z)/H_0$")
plt.xlim(0.1, 1100); plt.ylim(0.3, 300)
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.legend()
plt.tight_layout()


os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure7_BAO_CMB_Comparison.png", dpi=150)
plt.show()
