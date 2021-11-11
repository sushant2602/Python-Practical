// for practise purpose git merge
#def Addition(a,b):
  #  c=a+b
    #return(c)

#print(Addition(1,4))
#print(Addition(10,7))



#def greet(str):
    #wel=("Welcome Home "+str)
   # return(wel)

#a=input("Enter Name ")
#c=greet(a)
#print(c)


"""def factorial(num):
    fact=1
    for i in range(1,num+1):
      fact=fact*i
    return(fact)

n=int(input("Enter Number "))
ans=factorial(n)
print(ans)"""


def add(a,b,c,d=2):
  sum=a*d+b*c
  return(sum)

p=int(input("Enter 1st number"))
q=int(input("Enter 2nd number"))
r=int(input("Enter 3rd number"))
s=int(input("Enter 4th number"))
ans=add(p,q,r,s)
ans1=add(p,q,r)
print(ans)
print(ans1)
