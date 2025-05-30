import os
import numpy as np
import matplotlib.pyplot as plt

kappa_0   = 0.01     # amplitude at pivot
ell_pivot = 300.0    # pivot multipole
alpha     = 0.3      # power-law slope

ell = np.logspace(np.log10(30), np.log10(3000), 500)  
kappa_tau = kappa_0 * (ell / ell_pivot)**(-alpha)

for ell_test in [100, 300, 1000]:
    idx = np.abs(ell - ell_test).argmin()
    print(f"κ_τ(ℓ={ell_test:4.0f}) = {kappa_tau[idx]:.4f}")

plt.figure(figsize=(6,4))
plt.loglog(ell, kappa_tau, lw=2, color="C0", label=r"$\kappa_{\tau}(\ell)$")
plt.axhline(0.01, color="gray", ls="--", label="LSST 1 %")
plt.xlabel(r"Multipole $\ell$")
plt.ylabel(r"Residual convergence $\kappa_{\tau}$")
plt.title("Weak-lensing signature of the scalar-time model")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/Figure10_Weak_Lensing_Signature.png", dpi=150)
plt.show()
