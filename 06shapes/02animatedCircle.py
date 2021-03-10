import matplotlib.pyplot as plt
from matplotlib import animation


def createCircle():
    circle = plt.Circle((0,0), 0.05)
    print("radius: {0}f".format(circle.radius))
    return circle

def updateCircle(frame, circle):
    print(circle.radius)
    
    circle.radius = frame*0.5
    print("frame: {0}".format(frame))
    return circle

def createAnimation():
    fig = plt.gcf()   #get the reference of current figure
    ax = plt.axes(xlim = (-10, 10), ylim=(-10,10))
    ax.set_aspect('equal')     #to equal the aspect ratio
    circle = createCircle()
    ax.add_patch(circle)
    
    #create animation
    anime = animation.FuncAnimation(
        fig, updateCircle,
        fargs=(circle,), 
        frames=30, 
        interval=100,
        # repeat=False
    )
    plt.title("CIRCLE ANIMATION")
    plt.show()
    
    
if __name__ == '__main__':
    createAnimation()
    
    
    