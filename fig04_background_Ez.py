import os
import numpy as np
import matplotlib.pyplot as plt

h = 0.7
Omega_r0 = 4.2e-5 / h**2   # 8.57 x 1e-5
Omega_m0 = 0.50
Omega_tau0 = 0.62

print(f"Sum of Omega's today = {Omega_r0 + Omega_m0 + Omega_tau0:.3f}")

z = np.logspace(-2, 3.6, 500)   #  z = 0.01 ... 4000

Ez = np.sqrt(Omega_r0*(1+z)**4 +
             Omega_m0*(1+z)**3 +
             Omega_tau0*(1+z)**2)

def dominant(z_val):
    r = Omega_r0*(1+z_val)**4
    m = Omega_m0*(1+z_val)**3
    t = Omega_tau0*(1+z_val)**2
    winner = max((r,"radiation"), (m,"matter"), (t,"tau-field"),
                 key=lambda pair: pair[0])[1]
    return winner, r/(r+m+t), m/(r+m+t), t/(r+m+t)

for test_z in [0, 1, 10, 100, 2000]:
    dom, f_r, f_m, f_t = dominant(test_z)
    print(f"z={test_z:>4} : {dom:9s} dominates "
          f"(fractions  r={f_r:.2%}, m={f_m:.2%}, tau={f_t:.2%})")

plt.figure(figsize=(6,4))
plt.loglog(z, Ez, lw=2, color="C0")
plt.xlabel("Red-shift $z$")
plt.ylabel("$E(z)=H(z)/H_0$")
plt.title("Scalar-time background expansion")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure4_Background_Expansion.png", dpi=150)
plt.show()
