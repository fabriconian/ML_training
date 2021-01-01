# Pulse propagation simulation by solving a wave equation. Represented by movie
import numpy as np
import matplotlib.pyplot as plt


# u[0]=uo[0]=u[-1]=uo[-1]=0          # zero boundary condition
# s=1
# u[0] = A*np.sin(w*s*dt)
# iteration
def amax_of_w(w, params):
	u, uo, a, dt, smax, A = params
	amax = 0
	s=2    # start from step 2. step 0 and 1 are used for initial conditions
	while s<=smax:
		u[0] = A*np.sin(w*s*dt)
		ubuf = u.copy()  # save u to buffer
		u[1:-1] = b*u[1:-1] +a*(u[2:]+u[0:-2]) - uo[1:-1] # update u
		uo = ubuf.copy()  # update uo by old u (saved in ubuf)
		amax = max(amax, u.max())
		  # Shot the figure every 'dsav'th step
		# if s%dsav==0:
		# 	plt.ylim(-1.2,1.2)  # set the ylimit of sub-panels
		# 	plt.yticks(np.arange(-1.2,1.4,0.4)) # yticks
		# 	plt.plot(x,u); plt.draw(); plt.pause(0.01);plt.clf()
		# 	print(s)
		s+=1  # time step advance
	return(amax)

xmax = 1.0
dx = xmax / 200.0
dt = 0.005
smax = 5000
dsav = 20
# Simulation parameters
al=dt/dx   # alpha parameter
a=al**2
b=2*(1-a)

x=np.arange(0,xmax+dx,dx)
u=np.zeros_like(x)
uo=np.zeros_like(x)
ubuf=np.zeros_like(x)                         # buffer array for temporary save of var.
N=len(u)-1                       # last index of the array
A = 0.001
params = (u, uo, a, dt, smax, A)
W = np.linspace(0.1, 2000, 50)
amplitudes = np.zeros_like(W)
for i, w_ in enumerate(W):
	amplitudes[i]=amax_of_w(w_,params)
	print(i)
# apmlitudes = np.array([amax_of_w(w_, params) for w_ in W])
plt.plot(W, amplitudes)
plt.show()
print('done')

