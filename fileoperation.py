import os

newfile=open("some.txt","w")
for i in range(0,10):
    newfile.write("Hello I am Sushant \n")

#newfile=open("some.txt","r")
#for i in range(0,10):
 #   print(newfile.read(50))

#os.rename('some.txt','NotSome.txt')

#os.remove("NotSome.txt")

#newfile= open("some.txt","r")
#newfile.seek(50)
#print(newfile.read())
#print(newfile.tell())
#print(newfile.mode)
#print(newfile.name)
#print(newfile.softspace)