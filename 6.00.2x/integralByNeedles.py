import random, pylab

def mean(data):
    return sum(data)/len(data)

def stdDev(data):
    mu = mean(data)
    total = sum((x-mu)**2 for x in data)
    
    return (total/len(data))**0.5

def dropNeedles(numNeedles,function,lower,upper,plot):
    """numNeedles(int): number of needles to drop
    function: which function to compute
    lower(float): lower bound for integral
    upper(float): upper bound for integral
    plot(bool): plot graph?"""
    
    inArea = 0
    if plot:
        pylab.figure(1)
        xVals = pylab.arange(lower,upper,upper/100)
        yVals = function(xVals)
    
        
    for needle in range(numNeedles):
        x = random.uniform(lower,upper)
        y = random.uniform(0,1)

        if y <= function(x):
            inArea += 1
            if plot:
                pylab.scatter(x,y, c = 'r', marker = '.')
        elif plot:
            pylab.scatter(x,y, c = 'k', marker = '.')
    if plot:
        pylab.plot(xVals,yVals,linewidth =7.0)

    return inArea/numNeedles

def semiCircle(x):
    y = 1-x**2
    print(y)
    if y < 0:
        return -99999
    return pylab.sqrt(y)
    
def integrate(numNeedles,numTrials,function,lower,upper):
    means = []
    for i in range(numTrials):
        means.append(dropNeedles(numNeedles,function,lower,upper,0))
    print('mean = ', mean(means),'\nStd Dev = ',stdDev(means))

#print(integralNeedles(1000,pylab.sin,0,pylab.pi,True))
