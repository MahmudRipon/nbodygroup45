#This code has been modified based on the code of the following author
#Modified by Mahmud and Khairi
#Reference
# Example for exponential_migration reboundx force
# By: Mohamad Ali-Dib
#     mma9132@nyu.edu
#     See https://arxiv.org/abs/2104.04271
import rebound
import reboundx
import numpy as np
import matplotlib.pyplot as plt

neptune_a_array = []
earth_a_array=[]
time_array1 = []
time_array2 = []
neptune_e_array=[]
earth_e_array=[]
ratio_or_period=[]

sim = rebound.Simulation()  # Initiate rebound simulation
sim.units = ('yr', 'AU', 'Msun')
sim.add(m=1)
sim.add(m=5.1e-5, a=24., e=0.01, hash="neptune")  # Add Neptune (pre-migration) at 24 AU
sim.add(m=5.7e-6, a=10, e=0.01671, hash="planet")  # earth (pre-migration) at 1 AU
sim.move_to_com()

rebx = reboundx.Extras(sim)  # Initiate reboundx
mod_effect = rebx.load_force("exponential_migration")  # Add the migration force
rebx.add_force(mod_effect)  # Add the migration force

sim.particles[1].params["em_aini"] = 24  # parameter 1: Neptune's initial semimajor axis
sim.particles[1].params["em_afin"] = 10  # parameter 2: Neptune's final semimajor axis
sim.particles[1].params["em_tau_a"] =1e5  # parameter 3: the migration e-folding time
sim.particles[2].params["em_aini"] = 10  # parameter 1: Neptune's initial semimajor axis
sim.particles[2].params["em_afin"] = 24  # parameter 2: Neptune's final semimajor axis
#sim.particles[2].params["em_tau_a"] = 1e5  # parameter 3: the migration e-folding time

for time in np.linspace(0, 1e6, 100):  # Integrate the system for 1e6 yr
    sim.integrate(time)
    neptune_a_array.append(sim.particles[1].a)
    neptune_e_array.append(sim.particles[1].e)
    time_array1.append(sim.t)
    earth_a_array.append(sim.particles[2].a)
    earth_e_array.append(sim.particles[2].e)
    time_array2.append(sim.t)
    ratio_or_period.append(sim.particles[1].P / sim.particles[2].P)
    #ratio_or_period.append(sim.particles[1].p/sim.particles[2].p)

plt.plot(time_array1, neptune_e_array)  # Plot
plt.plot(time_array1, earth_e_array)  # Plot
plt.legend(['Neptune', 'Planet'])
plt.xlabel('Time (yrs)')
plt.ylabel('Eccentricity')
plt.grid()
plt.savefig('exercise5.1.png')
plt.clf()

plt.plot(time_array1, neptune_a_array)  # Plot
plt.plot(time_array1, earth_a_array)  # Plot
plt.legend(['Neptune', 'Planet'])
plt.xlabel('Time (yrs)')
plt.grid()
plt.ylabel('Semimajor axis (AU)')
plt.savefig('exercise5.2.png')

plt.clf()

plt.plot(time_array1, ratio_or_period)  # Plot

plt.legend(['e-folding time: 1e5'])
plt.xlabel('Time (yrs)')
plt.ylabel('Period Ratio')#plt.savefig('<exercise5.2')
plt.grid()
plt.savefig('exercise5.3.png')