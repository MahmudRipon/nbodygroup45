#Md Mahmud Hassan
#"Framework has been used from N-Body Simulations with REBOUND by Dr. Christoph Schafer"#
import rebound
import numpy as np
import matplotlib.pyplot as plt
# collisions count
def collision_print_only ( sim_pointer , collision ):
	global cnt
	sim = sim_pointer.contents
	print(sim.t)
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
rhill = 1.0*(m2/(3.*m1))**(1./3)
delta = 2.4*(m2/m1 + m3/m1)**(1./3)
sim.add(m=m1)
sim.add(m=m2,a=1.0,e=0.0,r=rhill)
DELTA = 0.1*delta
sim.add(m=m3, a=1.0+DELTA, e=0.0, r=rhill, omega=np.pi)
sim.move_to_com()
Norbits =1000
Nsteps = Norbits
times = np.linspace(0, Norbits*2*np.pi,Nsteps )
x = np.zeros((sim.N,Nsteps))
y = np.zeros_like(x)

for i, time in enumerate(times):
    sim.integrate(time, exact_finish_time = 0)
    for j in range(sim.N):
        x[j, i] = sim.particles[j].x
        y[j, i] = sim.particles[j].y

plt.scatter (x,y, s =2)
plt.set_title ("Orbit with step size %g" % sim.dt)
plt.set_xlabel("x- coordinate")
plt.set_ylabel("y- coordinate")
plt.grid()
plt.savefig("ex2.1 "+str(sim .dt)+".png")