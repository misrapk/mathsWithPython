from matplotlib import pyplot as plt
import math

def drawGraph(x, y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion')
    
    
def myRange(start, end, interval):
    num = []
    while start<end:
        num.append(start)
        start += interval
        
    return num

def drawProjectile(u, theta):
    theta = math.radians(theta)
    g = 9.8
    
    #time
    t = 2 * u * math.sin(theta)/g
    print(t)
    
    
    #interval
    intervals = myRange(0, t, 0.001)
    
    #list of x and y 
    x =[]
    y = []
    
    
    for t in intervals:
        x.append(u*math.cos(theta) * t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        
    drawGraph(x,y)
    

# if __name__ == '__main__':
#     try:
#         u = float(input("Enter the initial Velocity: "))
#         theta = float(input("enter the value of theta(projection angle): "))
#     except ValueError:
#         print("Invalid Input!!!")
        
#     else:
#         drawProjectile(u, theta)
#         plt.show()

#TODO: comparing trajectory
if __name__ == '__main__':
    uList = [20,40,60]
    
    theta = 30
    for u in uList:
        
        drawProjectile(u, theta)
        
    plt.legend(['20','40','60'])
    plt.show()