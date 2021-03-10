#we are using two rules
''' rule 1: x, y = x+1, y-1
    rule 2: x, y, = x+1, y+1'''
    
import matplotlib.pyplot as plt
import random

def rule1(p):
    x, y = p[0],p[1]
    
    return x+1, y-1

def rule2(p):
    x, y = p[0], p[1]
    return x+1, y+1

def transform(p):
    #list of function
    rules = [rule1, rule2]
    #pick random
    t = random.choice(rules)
    x, y = t(p)
    return x,y

def buildTrajectory(p, n):
    x, y = [p[0]], [p[1]]
    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
        
    return x, y

if __name__ == '__main__':
    p = (1,1)
    n = int(input('Enter iterations: '))
    x,y = buildTrajectory(p,n)
    plt.plot(x,y)
    plt.show()    