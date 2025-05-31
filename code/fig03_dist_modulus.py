import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

c_km_s = 299792.458          # speed of light (km/s)
H0     = 70.0                # Hubble const (km/s/Mpc)

# scalar-time parameters
Om_m_st   = 0.31
Om_tau_st = 0.69
Om_r      = 4.2e-5 / 0.7**2  # radiation for h=0.7 

# LCDM parameters
Om_m_LCDM = 0.31
Om_Lam    = 0.69

z = np.linspace(0, 1.4, 600)

def E_scalar_time(z):
    return np.sqrt(Om_r*(1+z)**4 + Om_m_st*(1+z)**3 + Om_tau_st*(1+z)**2)

def E_LCDM(z):
    return np.sqrt(Om_r*(1+z)**4 + Om_m_LCDM*(1+z)**3 + Om_Lam)

def distance_modulus(Hfunc):
    """Return mu(z) using proper integral for the given E(z)."""
    # comoving distance in Mpc
    Dc = cumtrapz(c_km_s / H0 / Hfunc(z), z, initial=0)
    Dl = (1+z) * Dc  # luminosity distance
    return 5*np.log10(Dl*1e6/10)  # 10 pc 

mu_st_int   = distance_modulus(E_scalar_time)
mu_LCDM_int = distance_modulus(E_LCDM)

mu_st_toy   = 43.1 + 5*np.log10((1+z)*(1 - 0.45*z)/(1 + 0.55*z))
mu_LCDM_toy = 43.1 + 5*np.log10((1+z)*(1 + 0.30*z))

rms_st   = np.sqrt(np.mean((mu_st_int   - mu_st_toy  )**2))
rms_LCDM = np.sqrt(np.mean((mu_LCDM_int - mu_LCDM_toy)**2))
print(f"RMS delta-mu  (scalar-time integr. vs toy)  = {rms_st:.4f} mag")
print(f"RMS delta-mu  (CDM       integr. vs toy)  = {rms_LCDM:.4f} mag")

plt.figure(figsize=(6,4))
plt.plot(z, mu_st_toy,   "r--", label="Scalar-time (toy)")
plt.plot(z, mu_LCDM_toy, "C1",  label=r"$\Lambda$CDM (toy)")
plt.plot(z, mu_st_int,   "k:",  alpha=0.4, lw=1,
         label="Scalar-time (integral)")
plt.plot(z, mu_LCDM_int, "k--", alpha=0.4, lw=1,
         label=r"$\Lambda$CDM (integral)")
plt.xlabel("Red-shift $z$")
plt.ylabel(r"Distance modulus $\mu$ (mag)")
plt.legend()
plt.grid(True, ls="--", alpha=0.5)
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure3_Distance_Modulus_Curves.png", dpi=150)
plt.show()
