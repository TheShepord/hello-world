import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0,1000)

plt.plot(mySamples,myLinear, 'b-',label = 'linear',linewidth = 2.0)
plt.legend(loc = 'upper left')

plt.subplot(212)
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic, 'ro',label = 'quadratic')

plt.legend(loc = 'upper left')
plt.title('Linear vs Quadratic')



plt.figure('cube vs. expo (log)')
plt.clf()

plt.plot(mySamples,myCubic,'g--', label = 'cubic')
plt.legend(loc = 'upper left')
plt.yscale('log')
plt.title('Cubic vs Exponential')

plt.plot(mySamples,myExponential,'r-', label = 'exponential', linewidth = 2.0)
plt.legend(loc = 'upper left')

