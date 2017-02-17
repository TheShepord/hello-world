# -*- coding: utf-8 -*-

class Item:
    def __init__(self,name,weight,value):
        self.name = name
        self.weight = weight
        self.value = value
        
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def getValue(self):
        return self.value
    def __str__(self):
        return 

def greedy(items,constraint,keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    
    totalValue,totalWeight = 0.0,0.0
    result = []
    
    for i in range(len(itemsCopy)):
        if itemsCopy[i].getWeight() + totalWeight <= constraint:
            totalValue += itemsCopy[i].getValue()
            totalWeight += itemsCopy[i].getWeight()
            result.append(itemsCopy[i].getName())
    
    return(totalValue,totalWeight,result)

def buildList(names,weights,values):
    list = []
    for i in range(len(values)):
        list.append(Item(names[i],weights[i],values[i]))
    return list




max_weight= 14

names = ['dirt','computer','fork','problem_set']
weights = [4,10,4,0]
values = [0,30,1,-10]

x,y,z = greedy(buildList(names,weights,values),max_weight,Item.getValue)
print("Total value: ", x, "\nTotal weight: ", y,"\nItems taken: ")
for item in z: 
    print('    ',item)

