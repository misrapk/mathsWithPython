#F = G.m1.m2/r^2

import matplotlib.pyplot as plt

#draw graph
def drawGraph(x,y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distances')
    plt.ylabel('Gravitational force in Newton')
    plt.title("Gravitational Force vs distance")
    plt.show()
    
    
def generateR():
    r = range(100, 1001, 50)
    F = [] #sotre calculated F
    G = 6.674 * (10**-11)
    
    m1 = 0.5
    m2 = 1.5
    
    # force
    for dist in r:
        force = G*(m1*m2)/dist**2
        F.append(force)
    
    drawGraph(r, F)
    
    
if __name__=='__main__':
    generateR()