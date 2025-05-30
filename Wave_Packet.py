import numpy as np
import matplotlib.pyplot as plt

ħ = 1.054571817e-34  # J·s
m_e = 9.10938356e-31 # kg
sigma0 = 1e-10       # initial sigma 0.1 nm
t = np.linspace(0, 1e-14, 500)  # 0 to 10 fs

def sigma_free(t):
    return np.sqrt(sigma0**2 + (ħ * t / (m_e * sigma0))**2)

# slowed time region: tau_factor < 1 (e.g., 0.2)
tau_factor = 0.2
sigma_slow = sigma_free(t * tau_factor)

plt.figure(figsize=(6,4))
plt.plot(t*1e15, sigma_free(t)*1e10, label="Normal time")
plt.plot(t*1e15, sigma_slow*1e10, label="Slowed time (τ factor = 0.2)")
plt.xlabel("Coordinate time (fs)")
plt.ylabel(r"$\sigma$ (Å)")
plt.title("Wave-packet width vs. time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
