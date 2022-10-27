#Md Mahmud Hassan
import rebound
import numpy as np
import matplotlib.pyplot as plt
# count number of collisions
def collision_print_only ( sim_pointer , collision ):
	global cnt
	sim = sim_pointer . contents # get simulation object from pointer
	print ( sim.t) # print time
	cnt += 1
	return 0

cnt = 0

sim = rebound.Simulation()
sim.integrator = "IAS15"
sim.collision = "direct"
sim.collision_resolve = collision_print_only

m1 = 1.0
m2 = m3= 1e-5
#m3=1e-7
delta = 2.4 * (m2/m1 + m3/m1)**(1./3)
rhill = 1.0*(m2/(3.*m1))**(1./3)
sim.add(m=m1)
sim.add(m=m2, a=1.0, e=0.0, r=rhill)
DELTA = .1 * delta
sim.add(m=m3, a=1.0+DELTA, e=0.0, r=rhill, omega=np.pi)
sim.move_to_com()
Norbits =10000
Nsteps = Norbits
times = np.linspace (0, Norbits *2* np.pi , Nsteps )
x = np.zeros((sim.N, Nsteps)) # coordinates for both particles
y = np.zeros_like(x)

for i, t in enumerate(times):
    sim.integrate(t, exact_finish_time = 0)
    for j in range(sim.N):
        x[j, i] = sim.particles[j].x
        y[j, i] = sim.particles[j].y

fig,ax = plt.subplots()
ax.scatter (x,y, s =2)
ax.set_title ("Orbit with step size %g" % sim.dt)
ax.set_xlabel ("x- coordinate")
ax.set_ylabel ("y- coordinate")
plt.grid ()
fig.savefig (" ex2 "+str (sim .dt)+".png")

