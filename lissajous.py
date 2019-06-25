from numpy import sin,cos,tan,pi,linspace
from pylab import plot,show,subplot
import random

a=[1,2,3,4,5,6,7,8,9,0] # plotting the curves for
b=[1,4,7,2,9,8,5,3,6,2] # different values of a/b
delta = pi/4
t = linspace(-pi,pi,400)
#i=random.randint(0,10)
for i in range(0,10):
 x = sin(a[i]* t + delta)
 y = sin(b[i] * t)
 subplot(3,5,i+1)
 plot(x,y)

show()


