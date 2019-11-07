def prime_number(x):
    counter=0
    c=0
    for y in range(x,0, -1):
        z=x%y
        if z==0:
            counter+=1
        if counter==2:
            c+=1
count=0
while count<10:
    x=count*10
    print(x)
    count+=1
count=0.2
while count<5.3:
    x=count*10
    print(x)
    count+=0.2
count=0
while count<10:
    x=count
    print(prime_number(x))
    count+=1
count=0
a=1
for count in range(0,5):
    a = 2*a + count
print(a)
for x in range(1,101):
    y=x%3
    z=x%8
    if y!=0 and z!=0:
        print(x)
height = 2
for i in range(height):
    print(".")
    for x in range(i):
        print(" ")
        print(".")
    print(".")