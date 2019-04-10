import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
plt.axis((-20,20,-20,20))

xdata, ydata = [], []
circles = []

r = [5,4,3,2,1]
k = [1,2,3,4,5]

for ri in r:
    if len(circles) ==0:
        xy = (0,0)
    else:
        xy = (circles[-1].get_center()[0] + circles[-1].get_radius() * np.cos(0),circles[-1].get_center()[1] + circles[-1].get_radius() * np.sin(0))
    circles.append(plt.Circle(xy,ri,fill=False))
    plt.gcf().gca().add_patch(circles[-1])

def update(time):    
    val_x = 0
    val_y = 0
    ln =[]

    for i in range(0,len(r)):
        val_x += r[i] * np.cos(k[i]*time)
        val_y += r[i] * np.sin(k[i]*time)

    xdata.append(val_x)
    ydata.append(val_y)
    
    for circle_idx in range(1,len(circles)+1):
        prev_circle = circles[circle_idx-1]
        xy= (prev_circle.get_center()[0]+prev_circle.get_radius() * np.cos(k[circle_idx-1]*time),prev_circle.get_center()[1]+prev_circle.get_radius() * np.sin(k[circle_idx-1]*time))
        ln.append(plt.scatter(xy[0],xy[1],c='b',s=20,marker='x'))
        
        if circle_idx < len(circles):
            circles[circle_idx].set_center(xy)

    ln.append(plt.plot(xdata, ydata,c='r')[0])
    return tuple(circles) + tuple(ln)

ani = FuncAnimation(fig, update, frames=np.linspace(0,2*np.pi, 256),
                    blit=True,interval=30,repeat=False)
plt.show()