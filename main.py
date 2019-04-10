import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_square_points(n):
    X = []
    tmp = np.linspace(-n/2,n/2,50)
    for x_cord in tmp:
        X.append(complex(x_cord,n/2))
    for y_cord in tmp:
        X.append(complex(n/2,-y_cord))
    for x_cord in tmp:
        X.append(complex(-x_cord,-n/2))
    for y_cord in tmp:
        X.append(complex(-n/2,y_cord))
    return X


fig = plt.figure()
plt.axis((-5,5,-5,5))

xdata, ydata = [], []
circles = []

r = [5,4,3,2,1]
k = [1,2,3,4,5]

P = get_square_points(3)
fft_P = np.fft.fft(P,len(P))

r=[]
k=[]
phase = []

idx=0
for z in fft_P:
    if np.abs(z) != 0:
        phase.append(np.angle(z))
        r.append(np.abs(z)/len(fft_P))
        k.append(idx)
        idx += 1

print("SIZE OF R : ",len(r))
print(r)
idx = 0
for ri in r:
    if len(circles) ==0:
        xy = (0,0)
    else:
        xy = (circles[-1].get_center()[0] + circles[-1].get_radius() * np.cos(0 + phase[idx-1]),circles[-1].get_center()[1] + circles[-1].get_radius() * np.sin(0+phase[idx-1]))
    circles.append(plt.Circle(xy,ri,fill=False))
    plt.gcf().gca().add_patch(circles[-1])
    idx+=1

def update(time):    
    val_x = 0
    val_y = 0
    ln =[]

    for i in range(1,len(r)+1):
        val_x += r[i-1] * np.cos(k[i-1]*time + phase[i-1])
        val_y += r[i-1] * np.sin(k[i-1]*time + phase[i-1])

    xdata.append(val_x)
    ydata.append(val_y)
    
    for circle_idx in range(1,len(circles)+1):
        prev_circle = circles[circle_idx-1]
        xy= (prev_circle.get_center()[0]+prev_circle.get_radius() * np.cos(k[circle_idx-1]*time+phase[circle_idx-1]),prev_circle.get_center()[1]+prev_circle.get_radius() * np.sin(k[circle_idx-1]*time+phase[circle_idx-1]))
        ln.append(plt.scatter(xy[0],xy[1],c='b',s=20,marker='x'))
        
        if circle_idx < len(circles):
            circles[circle_idx].set_center(xy)

    ln.append(plt.plot(xdata, ydata,c='r')[0])
    return tuple(circles) + tuple(ln)

ani = FuncAnimation(fig, update, frames=np.linspace(0,2*np.pi, 256),
                    blit=True,interval=30,repeat=False)
plt.show()