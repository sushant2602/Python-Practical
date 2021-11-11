import matplotlib.pyplot as plt
import numpy as np

# Histogram
# y=np.random.randn(2,3)
# plt.hist(y)
# plt.show()

# Bar Chart
# plt.bar([1.5,2.6,4.8],[40,55,89])
# plt.show()

# Horizontal Bar Chart
# plt.barh([1.5,2.6,4.8],[40,55,89])
# plt.show()

# Plotting a Dictionary using a Bar Chart
# dic={'A':25,'B':70,'C':55,'D':90}
# for i, key in enumerate(dic):
#  print(i,key)
#  plt.bar(i,dic[key])
# plt.show()

# Plotting a Dictionary using a Bar Chart and xticks
# dic={'A':25,'B':70,'C':55,'D':90}
# for i, key in enumerate(dic):
#    print(i,key)
#   plt.bar(i,dic[key])
# plt.xticks([0,1,2,3],['A','B','C','D'])
# plt.show()

# Pie Chart
# plt.figure(figsize=(3,3))
# x=[40,20,5]
# la=['Python','JAVA','C++']
# plt.pie(x,labels=la,autopct='%1.1f%%',shadow=True,startangle=90,explode=(0.1,0,0))
# plt.show()

# Scatter Plot
x = np.random.rand(3)
y = np.random.rand(3)
plt.scatter(x, y, color='m', s=400)
plt.show()

# line Plot
