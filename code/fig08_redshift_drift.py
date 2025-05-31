import os
import numpy as np
import matplotlib.pyplot as plt

H0 = 70.0                 # km/s/Mpc
Omega_r0 = 4.2e-5 / 0.7**2  # radiation (photons + v) for h=0.7
Om_m_st   = 0.50
Om_tau_st = 0.62
Om_m_LCDM = 0.31
Om_Lam    = 0.69


def H_scalar(z):
    return H0 * np.sqrt(Omega_r0*(1+z)**4
                        + Om_m_st*(1+z)**3
                        + Om_tau_st*(1+z)**2)

def H_LCDM(z):
    return H0 * np.sqrt(Omega_r0*(1+z)**4
                        + Om_m_LCDM*(1+z)**3
                        + Om_Lam)


z = np.linspace(0, 5, 800)
dzdt_scalar = -H_scalar(z)                      # scalar-time formula
dzdt_LCDM   = (1+z)*H0 - H_LCDM(z)              # LCDM formula

z_target = 2.0
idx = np.abs(z - z_target).argmin()
diff = dzdt_scalar[idx] - dzdt_LCDM[idx]
print(f"dz/dt0  at z=2  :  scalar-time = {dzdt_scalar[idx]:.2f}  "
      f" vs LCDM = {dzdt_LCDM[idx]:.2f}   "
      f"(Delta = {diff:.2f} km/s/Mpc/yr)")

# Convert km/s/Mpc to cm/s/yr
km_per_Mpc = 3.0856776e19  # cm
yr         = 3.15576e7     # s
conv = km_per_Mpc / yr     # km/s/Mpc -> cm/s/yr
print(f"Delta at z=2 \approx {diff * conv*1e5:.2f} cm/s/yr")  # x1e5 km -> cm

plt.figure(figsize=(6,4))
plt.plot(z, dzdt_scalar,  lw=2, color="C0", label="Scalar-time")
plt.plot(z, dzdt_LCDM,    lw=2, ls="--", color="C1", label=r"$\Lambda$CDM")
plt.xlabel("Red-shift $z$")
plt.ylabel(r"$\mathrm{d}z/\mathrm{d}t_0$  (km s$^{-1}$ Mpc$^{-1}$)")
plt.ylim(-500, 500); plt.xlim(0, 5)
plt.grid(True, ls="--", alpha=0.5)
plt.legend()
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure8_Redshift_Drift.png", dpi=150)
plt.show()
