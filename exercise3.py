
#Written by Mahud and khairi based on existing framework
import numpy as np
import rebound
import reboundx
import matplotlib.pyplot as plt

#Defining Constant
sim = rebound.Simulation()
sim.units = ('AU','yr','Msun')
sim.integrator = "leapfrog"
Msaturn = 2.85716656e-4
sim.G=1

#analytical section for finding critical mass
n = 100
gamma=2.3999 #2.412, 2.375, 2.306 , 2.300, # Analytical value
            #2.4121, 2.3753, 2.3066, 2.2999 #Simulated
disfsat = 1 #Distance from saturn
#m =1.345993e-06,6.785771e-07,1.412171e-08,6.571483e-10 #Analytic
#m= 6.891771e-07, 6.786628e-07,1.412539e-08, 6.856914e-10                                            #simulated
l= 0 #+1.34e-6 #adding extram mass to check instability
m=(Msaturn*gamma)/(n*n*n)
m=m+l
print("%e"%m)

#Analytcal section
In = 0
for i in range(1, n):
    In = In+0.25/np.sin(np.pi*i*1./n)
omega = np.sqrt(sim.G * Msaturn / (disfsat * disfsat * disfsat) + sim.G * m * In / (disfsat * disfsat * disfsat))
v = omega * disfsat

sim.add(m=Msaturn)
deltap = 2*np.pi / n
phi = 0
for i in range(0, n):
    x = disfsat * np.cos(phi)
    y = disfsat * np.sin(phi)
    vx = -v * np.sin(phi)
    vy = v * np.cos(phi)
    sim.add(m=m, x=x, y=y, vx=vx, vy=vy)
    phi += deltap
sim.dt = 2*np.pi/omega*1e-5
sim.move_to_com()

Norbits = 100
t = 2*np.pi/omega*Norbits
x = np.zeros((sim.N))
y = np.zeros_like(x)
sim.integrate(t, exact_finish_time = 0)
for k in range(sim.N):
    x[k] = sim.particles[k].x
    y[k] = sim.particles[k].y

plt.scatter (x,y,color='r',marker='.')
plt.xlabel('X Corodinate from Saturn')
plt.ylabel('Y Corodinate from Saturn')
plt.title ("gamma: " + str(gamma)+ " Mass: " + str(m) + " n: " +str(n))
#plt.grid()
plt.savefig("exercise3, gamma= " + str(gamma)+ " Mass= " + str(m) + "n=" +str(n) + ".png")