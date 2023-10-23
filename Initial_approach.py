import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as math

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(10):
    # Define the coordinates of the two points

    # UAV 1    
    point1 = (0+i, 0, 50)  
    #UAV 2
    point2 = (0+i, 5, 50)
    #UAV 3
    point3 = (math.sqrt(5**2-2.5**2)+i, 2.5, 50)

    
    # Extract x, y, and z coordinates for each point
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3


    #CENTROID
    x_c=(x1+x2+x3)/3
    y_c=(y1+y2+y3)/3
    z_c=math.sqrt(6**2 - (x1-x_c)**2 - (y1-y_c)**2)
    
    #PAYLOAD
    point4= (x_c,y_c,50-z_c)
    x4, y4, z4 = point4

    

    # Plot the line
    ax.cla()
    ax.plot([x1, x4], [y1, y4], [z1, z4], marker='o', color='b', linestyle='-', linewidth=1)
    ax.plot([x2, x4], [y2, y4], [z2, z4], marker='o', color='r', linestyle='-', linewidth=1)
    ax.plot([x3, x4], [y3, y4], [z3, z4], marker='o', color='g', linestyle='-', linewidth=1)

    # Label the axes (optional)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10,10)
    ax.set_zlim3d(40,60)
    
    plt.pause(0.1)

    # Show the plot
plt.show()