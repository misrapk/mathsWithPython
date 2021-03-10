import matplotlib.pyplot as plt
from matplotlib import animation
import math


g = 9.8

def getIntervals(u, theta):
    t_f = 2 * u*math.sin(theta)/g
    intervals = []
    start = 0
    interval= 0.005
    while start< t_f:
        intervals.append(start)
        start = start + interval
    return intervals

def updatePos (i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * math.cos(theta) * t
    y = u * math.sin(theta)*t - 0.5*g*t*t
    circle.center = x, y
    return circle


def createAnimation(u, theta):
    intervals = getIntervals(u, theta)
    
    xMin = 0
    xMax = u*math.cos(theta)*intervals[-1]
    yMin =0
    tMax = u*math.sin(theta)/g
    yMax = u*math.sin(theta) * tMax - 0.5*g*tMax**2
    
    fig = plt.gcf()
    ax = plt.axes(xlim=(xMin, xMax), ylim=(yMin, yMax))
    
    circle = plt.Circle((xMin, yMin), 1)
    ax.add_patch(circle)
    
    
    anim = animation.FuncAnimation(
        fig, updatePos,
        fargs=(circle, intervals, u, theta),
        frames = len(intervals), interval=50,
        repeat =False
    )
    plt.title('Projectile')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    
if __name__ == '__main__':
    try:
        u =float(input('ENter initial vleocity(m/s): '))
        theta = float(input('Enter angle of projection(Deg): '))
    except ValueError:
        print("INvalid")
    
    else:
        theta = math.radians(theta)
        createAnimation(u, theta)
    