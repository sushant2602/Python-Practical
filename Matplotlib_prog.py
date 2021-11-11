import matplotlib.pyplot as plt
import numpy as np

#y_values=[1,2,3,4,10]
#plt.plot(y_values,[i**2 for i in y_values])
#plt.show()

#numpy in matplotlib
#x=np.arange(0,5,0.01)
#print(x)
#plt.plot(x,[i**2 for i in x])
#plt.show()

#multiline plots
#x=range(5)
#plt.plot(x,[x1 for x1 in x])
#plt.plot(x,[x1*x1 for x1 in x])
#plt.plot(x,[x1*x1*x1 for x1 in x])
#plt.show()

#adding grid
#x=range(5)
#plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x],x,[x1*4 for x1 in x])
#plt.grid(True)
#plt.show()

#limiting the axis
#x=range(5)
#plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x],x,[x1*4 for x1 in x])
#plt.grid(True)
#plt.axis([0.5,1.5,2,6])
#plt.show()

#limiting the axis using xlim and ylim
#x=range(5)
#plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x],x,[x1*4 for x1 in x])
#plt.grid(True)
#plt.xlim(0.5,1.5)
#plt.xlim(2,6)
#plt.show()

#Adding Label
#x=range(5)
#plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x],x,[x1*4 for x1 in x])
#plt.grid(True)
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.show()

# Adding Title
#x=range(5)
#plt.plot(x,[x1 for x1 in x],x,[x1*2 for x1 in x],x,[x1*4 for x1 in x])
#plt.grid(True)
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('Learning About Matplotlib')
#plt.show()

#Adding Leged
#x=np.arange(5)
#plt.plot(x,x,label='Linear')
#plt.plot(x,x*x,label='Square')
#plt.plot(x,x*x*x,label='Cube')
#plt.grid(True)
#plt.xlabel('X-Axis')
#plt.ylabel('Y-Axis')
#plt.title("Polynomial Graph")
#plt.legend()
#plt.show()

#Saving Plot
#x=np.arange(5)
#plt.plot(x,x,label='Linear',marker='o',color='r')
#plt.plot(x,x*x,label='Square',marker='+',color='k')
#plt.plot(x,x*x*x,label='Cube',marker='*',color='m')
#plt.grid(True)
#plt.xlabel('X-Axis')
#plt.ylabel('Y-Axis')
#plt.title("Polynomial Graph")
#plt.legend()
#plt.savefig('poly.png')
#plt.show()

#subplot
x=np.arange(1,10,1)
y1=2*x+5
y2=3*x+10

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title('Graph1')
plt.tight_layout(3)

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title('Graph 2')
plt.tight_layout(3)

plt.subplot(2,2,4)
plt.plot(x,y2)
plt.title('Graph 3')
plt.show()