#This code has been written on existing frame given on lab instruction file
#Code Written,/Upßdated or Modified by Mahmud  Khairi
import rebound
import numpy as np
import matplotlib.pyplot as plt
#'Defining Constants'
au = 1.496e11
gvconstant = 6.67408e-11
solarmass = 1.989e30

sim = rebound.Simulation()
sim.G = gvconstant

# Adding Sun to simulation system
sim.add(m=solarmass)

#Adding Jupiter and Mars to simulation system
# Uw have collected deta from here https://ssd.jpl.nasa.gov/horizons/app.html#/
#$$SOE 2460004.500000000 = A.D. 2023-Mar-01 00:00:00.0000 TDB
#Jupiter
x = 7.045364178498787E+08 *1000
y = 2.238404749861620E+08 *1000
z =-1.669106234685592E+07 *1000
vx=-4.104604962272368E+00 *1000
vy= 1.306483451546579E+01 *1000
vz= 3.753780113731864E-02 *1000
m  = 1e-3*solarmass;
sim.add(m=m, x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)

# mars
#SOE 2460004.500000000 = A.D. 2023-Mar-01 00:00:00.0000 TDB

x = -1.071858196169919E+08*1000
y = 2.188565196665210E+08 *1000
z = 7.216257314635783E+06 *1000
vx=-2.089398062381275E+01 *1000
vy=-8.501862232350478E+00 *1000
vz= 3.347808489897468E-01 *1000
m  = 3.2e-7*solarmass;
sim.add(m=m, x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)

#Adding 10000 particle to the system
N = N_t_particle = 10000
a_ini = np. linspace (2 * au, 4 * au, N_t_particle)
for a in a_ini :
    sim.add(a=a, f=np.random.rand()*2.*np.pi, e=0.5*np.random.rand())
orbit = 2*np.pi*np.sqrt(8 * au * au * au / (gvconstant * solarmass))
#Time steps according to lab manuals to reduce overtime
sim.dt = orbit*1e-2
sim.move_to_com()

#Defining Integrator
sim.integrator = 'leapfrog'
#sim.integrator = "IAS15"
#sim.collision = "direct"
sim.N_active = 3

#Setting Simulation parameters
N_orbits = 10000
end_time = N_orbits*orbit
npr = 1
Nsteps = N_orbits*npr
simtime = np.linspace(0, end_time, Nsteps)

eccntricity = np.zeros(N)
sm_axis = np.zeros(N)
x = np.zeros((sim.N, Nsteps))
y = np.zeros((sim.N, Nsteps))
energy = np.zeros(Nsteps)

#Starting Simulation
for i, t in enumerate(simtime):
    sim.integrate(t)
    for j in range(sim.N):
        x[j,i] = sim.particles[j].x
        y[j,i] = sim.particles[j].y
    energy[i] = sim.energy()

for j in range(0, sim.N-3):
    sm_axis[j] = sim.particles[j + 3].a
    eccntricity[j] = sim.particles[j+3].e

#Plotting the Semimajor Axix Vs Eccentricity
fig, ax = plt.subplots(2)
ax[0].grid()
ax[0].scatter((sm_axis/au), eccntricity,marker='.', s=1, c='g')
#ax[0].set_xlabel("Semi major axis (au)")
ax[0].set_ylabel("Eccentricity")
ax[0].set_xlim(2,4)
ax[0].set_ylim(0,1)

#Plotting the Semimajor Axix Vs Number of Asteroids
sm_axis = sm_axis/au
use_bins = np.arange(2, 4 , .005);
ax[1].hist(sm_axis, bins=use_bins);
ax[1].set_xlabel("Semi-major axis (au)")
ax[1].set_ylabel("Asteroids (per 0.005 au bins)")
ax[1].grid()
fig.savefig("exercise4_10000_orbits")
