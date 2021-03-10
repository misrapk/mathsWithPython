#Draw Circle

import matplotlib.pyplot as plt

def createCircle():
    return plt.Circle((0,0), radius=1)       #fc = 'r/g/b'
    
    
def showShape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')   #adjust the axis limit
    plt.show()
    
if __name__ == '__main__':
    c = createCircle()
    showShape(c)