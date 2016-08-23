import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete
import scipy

import sys

def closest_point(s,p):
	c1 = np.array([s,s])
	c2 = np.array([-s,-s])
	c3 = np.array([0,0])
	p1 = p-c1
	d1 = np.abs(np.linalg.norm(p1)-r)
	p1 = c1 + s*p1/np.linalg.norm(p1)
	p2 = p-c2
	d2 = np.abs(np.linalg.norm(p2)-r)
	p2 = c2 + s*p2/np.linalg.norm(p2)

	p3 = p-c3
	d3 = np.abs(np.linalg.norm(p3)-r)
	p3 = c3 + 1.5*s*p3/np.linalg.norm(p3)

	d = [(p1,d1),(p2,d2),(p3,d3)]
	return min(d,key = lambda e:e[1])[0]


U = []
T = []
X = []
dt  =0.01

r = -1.5
b = 2.0
A = np.array([[r,b],[-b,r]])
B = np.eye(2)
E = np.eye(2)

G = np.eye(2)
F = 1.0

Q = -r*np.eye(2)
P = scipy.linalg.solve_lyapunov(A.T,-Q)
vp,V = np.linalg.eig(P)
vq,V = np.linalg.eig(Q)
vp = np.real(vp)

a = np.min(vq)/np.max(vp)

print "vp ",vp
print "vq ",vq
print "a ",a

print A.T.dot(P) + P.dot(A)

R = np.eye(2)
S = 1.0

K = E.T.dot(P).dot(R).dot(P.T).dot(E)
vk,V = np.linalg.eig(K)
print vk

b = 2*np.sqrt(S*np.max(vk)/np.min(vp))

v,V = np.linalg.eig(A)
print v

Ad,Bd,Cd,Dd,dt = cont2discrete((A,B,np.eye(2),np.eye(2)), dt, method='zoh')
x0 = np.array([[1.5,0]]).T

x = x0
t = 0

X = [x0]
T = [t]
U = [np.array([[0,0]]).T]
_B = np.linalg.inv(Bd)

while t<10.0:
	if (t<3):
		_u = -x.copy()
	if t%2.<2.0*dt and ( t>5):
		_u = x.copy()
	if t<8 and t>5:
		_u = x.copy()
	_u = _u/np.linalg.norm(_u)
	x = Ad.dot(x) + Bd.dot(_u)
	X.append(x.copy().T[0])
	t += dt
	T.append(t)
	U.append(_u.copy().T[0])
X = np.array(X)
T = np.array(T)
U = np.array(U)

print X

plt.plot(X[:,0],X[:,1])

px = P.dot(X.T)
V = X*(px.T)
V = V.sum(axis=1)
Vs = ( (np.sqrt(V[0]) - b/a)* np.exp(-a*T/2) + b/a)
Vs = Vs*Vs

print "Vsup=",(b/a)**2
print "radius=",b/a
plt.figure()
plt.plot(T,Vs,'b')
plt.plot(T,V,'g')
plt.plot(T,((X*X).sum(axis=1))**0.5,'g')

# plt.plot(T,U[:,0],'r')
# plt.plot(T,U[:,1],'r')

D = [np.array([T]).T,X,U,np.array([V]).T,np.array([Vs]).T]
labels = 'T X1 X2 U1 U2 Vx Vsup'
print [d.shape for d in D]
D = np.concatenate(D,axis=1)
np.savetxt("data.dat",D,header=labels,comments="")
plt.show()
