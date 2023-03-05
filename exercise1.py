#Md Mahmud Hassan
#"Framework has been used from N-Body Simulations with REBOUND by Dr. Christoph Schafer"#
import numpy as np
import matplotlib . pyplot as plt
import rebound
# create a sim object
sim = rebound . Simulation ()
sim.integrator = "leapfrog"
#sim.integrator = "JANUS"
# and use a fixed time step
sim .dt = 1e-2
# here add your particles ....
sim . add (m =1.0)
sim . add (m=1e-3, a=1.0 , e =0.3)

sim . move_to_com ()
Norbits = 1000
Nsteps = Norbits*200
times = np. linspace (0, Norbits *2* np.pi , Nsteps )
x = np. zeros (( sim .N, Nsteps )) # coordinates for both particles
y = np. zeros_like (x)
energy = np.zeros ( Nsteps ) # energy of the system
# now integrating
for i, t in enumerate ( times ):
	#print (t, end="\r")
	sim. integrate (t,exact_finish_time =0)
	energy [i] = sim.calculate_energy ()
	for j in range (sim .N):
		x[j,i] = sim. particles [j].x
		y[j,i] = sim. particles [j].y

# plotting the orbit
fig, ax = plt.subplots (1,2)
ax[0]. scatter (x,y)
ax[0]. set_title ("Orbit with step size %g" % sim .dt)
ax[0].set_aspect ("equal")
ax[0]. set_xlabel ("X- coordinate ")
ax[0]. set_ylabel ("Y- coordinate ")

# plotting Time Vs Energy

ax[1]. scatter (times , np. abs( energy - energy[0]) /np.abs(energy[0]),marker='.')
ax[1]. set_title ("Energy with step size %g" % sim .dt)
ax[1]. set_xlabel ("time")
ax[1].set_yscale("log")
ax[1]. set_ylabel ("Energy(Log)")
plt .grid ()
#fig.savefig("ex1.1_orbit and energy_JANUS" +str(sim.dt) + ".png")
fig.savefig("ex1.1_orbit and energy_leapfrog" +str(sim.dt) + ".png")
