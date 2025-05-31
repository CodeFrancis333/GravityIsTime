import numpy as np
import matplotlib.pyplot as plt

tau_inf = 1.0     
k       = 0.6     

x = np.linspace(0, 6, 400)

tau   = tau_inf * (1 - np.exp(-k * x))
dtau  = np.gradient(tau, x)  
   
print(f"dtau/dx at x = 0  : {dtau[0]:.3f}")
print(f"dtau/dx at x = 1/k: {dtau[np.searchsorted(x,1/k)]:.3f}")
print(f"tau(x->infinity): {tau[-1]:.3f} (should -> tau_inf = 1.0)")

plt.figure(figsize=(6,4))
plt.plot(x, tau, label=r"$\tau(x)$", lw=2)
plt.xlabel("x  (units of $k^{-1}$)")
plt.ylabel(r"Clock field $\tau$")
plt.title("Clock-field gradient along 1-D cut")
plt.grid(True, ls="--", alpha=0.5)
plt.tight_layout()
plt.savefig("images/Figure1_Clock_Gradient.png", dpi=150)
plt.show()