from math import sqrt
x=0.01

if x==int(x):
    print(x,"is an integer")
else:
    print(x,"is not an integer")

x="abc"

numa=0
nume=0
numi=0
numo=0
numu=0
for char in x:
    if char in "aA":
        numa+=1
for char in x:
    if char in "eE":
        nume+=1
for char in x:
    if char in "iI":
        numi+=1
for char in x:
    if char in "oO":
        numo+=1
for char in x:
    if char in "uU":
        numu+=1
if numa>=1 and nume>=1 and numi>=1 and numo>=1 and numu>=1:
    print(x, "contians all five vowels")
elif numa>=1 or nume>=1 or numi>=1 or numo>=1 or numu>=1:
    print(x, "only contains some of the five vowels")
else:
    print(x, "contains none of the five vowels")

a=10
b=2
print("Yes")if a<b else print("No")

print("Yes")if a<b else print("Winner") if a**b <=100 else print("No")

x=25
y=sqrt(x)
if y<5:
    print("The square root of ", x, "is less than 5")
elif y>10:
    print("The square root of ", x, "is greater than 10")
else:
    if y==10:
        print("The square root of ", x, "is 10")

x="Jeni"
if len(x)>30 and x.isalpha():
    print(x, " is a valid name")
else:
    print(x, " is not a valid name")
