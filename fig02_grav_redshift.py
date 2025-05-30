import numpy as np
import matplotlib.pyplot as plt

G       = 6.67430e-11          # m^3 kg^-1 s^-2
c       = 2.99792458e8         # m s^-1
M_sun   = 1.98847e30           # kg

M_BH    = 1e9 * M_sun          # 10^9 solar masses
r_s     = 2 * G * M_BH / c**2  # Schwarzschild radius 

print(f"Schwarzschild radius r_s = {r_s/1e3:.2f} km")

r_over_rs = np.logspace(np.log10(3), 4, 400)
r         = r_over_rs * r_s

z_exact = 1.0 / np.sqrt(1.0 - r_s/r) - 1.0

z_approx = 0.5 * r_s / r * (1 + 0.75 * r_s / r)  

for test_r in [20, 100, 1e3]:
    idx = np.abs(r_over_rs - test_r).argmin()
    rel_err = (z_exact[idx] - z_approx[idx]) / z_exact[idx]
    print(f"r = {test_r:>5.0f} r_s :  exact z = {z_exact[idx]:.3e} "
          f"| 1/r approx rel. error = {rel_err:.2%}")


plt.figure(figsize=(6,4))
plt.loglog(r_over_rs, z_exact,  label="Exact GR",       lw=2)
plt.loglog(r_over_rs, z_approx, label="1/r weak field", lw=1.4, ls="--")
plt.gca().invert_yaxis()
plt.xlabel(r"Distance $r/r_s$")
plt.ylabel("Red-shift $z$")
plt.title(r"Red-shift vs. radius for $10^9\,M_\odot$ SMBH")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.savefig("images/Figure2_Gravitational_Redshift.png", dpi=150)
plt.show()