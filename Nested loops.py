#1
for row in range(10):
    for col in range(10):
        print("* ", end="")
    print("")
#2
for row in range(1):
    for i in range(1,10,2):
        print(" "*(10-i), end="")
        print("* "*i, end="")
        print("")
print("")
#3
width=7
print("*\t"*width)

for i in range(0,width-2):
    print("*\t",end="")

    for j in range(0,i):
        print("\t",end="")
    print("*",end="")

    for j in range(5-i):
        print("\t",end="")
    print("*",end="")
    for j in range(0,i):
        print("\t",end="")
    print("*")


print("*\t"*width)

'''for i in range(1,int(((height+1)/2)+1)):
    print("*", end="")
    print("\t"*i,end="")
    print("*",end="")
    z=width-i
    print("\t"*z,end="")
    print("*",end="")
    print("\t"*i,end="")
    print("*")

for i in range(int(height/2),0,-1):
    print("*", end="")
    print("\t"*i,end="")
    print("*",end="")
    z=width-i
    print("\t"*z,end="")
    print("*",end="")
    print("\t"*i,end="")
    print("*")'''