"""ans=(lambda z: z*6)
print(ans(5))"""


"""items=[1,2,3,4,5]
square=list(map(lambda x: x**2,items))
print(square)"""


"""items=range(-5,5)
less_than_zero=list(filter(lambda x: x<0,items))
print(less_than_zero)"""

"""from functools import reduce
product=reduce((lambda x,y: (x) * (y)),[1,2,3,4])
print(product)"""

a=10
b=20
print(id(a))
print(id(b))