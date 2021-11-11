import matplotlib.pyplot as plt
import numpy as np

#control colours
#x=np.arange(1,3)
#plt.plot(x,'y')
#plt.plot(x*2,'m')
#plt.plot(x*3,'c')
#plt.show()

#control line styling
#x=np.arange(1,3)
#plt.plot(x,'--')
#plt.plot(x*2,'-.')
#plt.plot(x*3,':')
#plt.show()

y=np.arange(1,10)
plt.plot(y,'*',y+0.5,'o',y+1,'D',y+2,'^',y+3,'s')
plt.show()