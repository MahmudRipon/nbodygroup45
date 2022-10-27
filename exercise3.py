import numpy as np
import rebound
import matplotlib.pyplot as plt
sim = rebound.Simulation()
sim.integrator = "leapfrog"
#https://rebound.readthedocs.io/en/latest/ipython_examples/Units/
sim.units = ('AU', 'yr', 'Msun')
Msat = 2.85716656e-4
n = 100
m = 1.1e-8
r = 1
m_critical = (2.3*Msat/(n**3))
print(m_critical)

#calculating In
In = 0.0
for k in range(1, n):
    In =In+ 0.25 * 1. / np.sin(np.pi*k/(1.0 * n))
##Calculating the Omega
omega = np.sqrt(sim.G * Msat / (r**3 ) + sim.G * m * In / (r**3))
v = omega * r
sim.dt = 2 * np.pi / (omega * 1e-5)
sim.add(m=Msat)
dphi = 2 * np.pi / (n)
phi = 0

#adding n mass
for i in range(0, n):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    vlx = -v * np.sin(phi)
    vly = v * np.cos(phi)
    sim.add(m=m, x=x, y=y, vx=vlx, vy=vly)
    phi += dphi
sim.move_to_com()
Norbits = 100
Nsteps = Norbits
#time = 2 * np.pi / omega * Norbits
energy=np.zeros(Nsteps)
x = np.zeros((sim.N, Norbits))
y = np.zeros_like(x)

times = np.linspace (0, Norbits *2* np.pi , Nsteps )
for i, t in enumerate(times):
    sim.integrate(t, exact_finish_time=0)
    energy[i]=sim.calculate_energy()
    for j in range(sim.N):
        x[j, 1] = sim.particles[j].x
        y[j, 1] = sim.particles[j].y

fig, ax = plt.subplots()
ax.scatter(x, y, s=2)
ax.set_aspect ("equal")
ax. set_xlabel ("X- coordinate ")
ax. set_ylabel ("Y- coordinate ")
plt.grid()
fig.savefig(" ex3_n=100 "".png")
