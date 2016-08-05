import numpy as np
from scipy.optimize import minimize,fmin_cobyla

N = 5

U = np.random.uniform(low=-4,high=4,size=(N,2))
print U
print U*U

a = 1
b = 2
R = lambda t: np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

f_opt = lambda x: np.abs(x[0])*np.abs(x[1])
f_cons = lambda x: (1-((R(x[2]).dot(U.T))**2).T.dot(np.array([[1./(x[0]**2),1./(x[1]**2)]]).T)).T[0]


eps = 1e-3

list_cons = [lambda x,i=i: f_cons(x)[i] for i in range(N)] 

all_f_cons = lambda x: [fc(x) for fc in list_cons]

x0 = [1,1,0]

print f_cons(x0)
cons = [{'type': 'ineq', 'fun':fc} for fc in list_cons]

result = minimize(f_opt,x0,bounds=((0,None),(0,None),(-np.pi,np.pi)),method="SLSQP",constraints=cons)

print result
print result.x
x = result.x
c=  f_cons(x)
print c
print  [fc['fun'](x) for fc in cons]

import matplotlib.pyplot as plt

plt.plot(U[:,0],U[:,1],"x")
a = result.x[0]
b = result.x[1]
T = np.linspace(0,2*np.pi,100)

X = np.cos(T)*a
Y = np.sin(T)*b

pts = np.array([X.T,Y.T])
pts = R(-x[2]).dot(pts)

plt.plot(pts[0,:],pts[1,:])

plt.axis('equal')

scale = 1.0
input_str = lambda i: "\draw[inputpoint] plot coordinates {(%fcm,%fcm)} node[anchor=south west] {$u_%i$};"%(U[i,0],U[i,1],i)
ellipse_str = "\\node[elli=%f:%fcm and %fcm] at (0, 0) (e) {};"%(-x[2]/np.pi*180,x[0],x[1])

for i in range(N):
	print input_str(i)

print ellipse_str

plt.show()