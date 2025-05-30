import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

nx = 400
x = np.linspace(-500, 500, nx)
y = np.linspace(-500, 500, nx)
X, Y = np.meshgrid(x, y)

def gaussian_2d(x0, y0, sigma, amp=1.0):
    return amp * np.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / (2 * sigma ** 2))

sigma = 120

gas1 = gaussian_2d(-150, 0, sigma, 1.0)
gas2 = gaussian_2d(150, 0, sigma, 0.7)
baryon = gas1 + gas2

# scalar-time halos: assume range ~200 kpc, create two collisionless halos originally centred with gas
# After collision, halos move ahead by 200 kpc relative to gas (idealised)
halo_offset = 200
tau_halo1 = gaussian_2d(-150 - halo_offset, 0, sigma, 1.0)  # moves leftward
tau_halo2 = gaussian_2d(150 + halo_offset, 0, sigma, 0.8)   # moves rightward

# Effective lensing convergence in modified tau-model: baryon + scalar halos
lensing_tau_halo = baryon + tau_halo1 + tau_halo2
lensing_tau_halo /= lensing_tau_halo.max()

fig, ax = plt.subplots(1, 1, figsize=(5,4))
im = ax.imshow(lensing_tau_halo, extent=(-500,500,-500,500), origin='lower', cmap=cm.viridis)
ax.contour(X, Y, baryon / baryon.max(), levels=[0.3,0.5,0.7], colors='white', linewidths=0.8)
ax.set_title('τ-model with self-gravitating halos')
ax.set_xlabel('kpc'); ax.set_ylabel('kpc')
ax.set_aspect('equal')
fig.colorbar(im, ax=ax, shrink=0.8, label='Norm. convergence')
plt.tight_layout()
plt.show()
