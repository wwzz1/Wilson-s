import random
x=20
while x!=0:
    x=x/2
    print(x)
#1
def both():
    count=1
    while count<=2:
        for x in range(8,-4, -1):
            print(x)
        count+=1
both()
#2
def is_odd(x):
    if x%2==1:
        return True
    else:
        return False
print(is_odd(1000001))
print(is_odd(1234567890))
#3
def dice_roll(x):
    y=0
    count=0
    while y==0:
        a=random.randint(1,6)
        b=random.randint(1,6)
        c=random.randint(1,6)
        count+=1
        if x==a+b+c:
            y+=1
    return count
print(dice_roll(17))
#4
def odd_even_count(x):
    nodd=0
    neven=0
    while x>0:
        y=x%10
        if y%2==1:
           nodd+=1
        else:
            neven+=1
        x=int(x/10)
    z="odd: "+str(nodd)+" even: "+str(neven)
    return z
print(odd_even_count(1234567890))
#5
def string_analysis(x):
    space=0
    number=0
    letter=0
    for i in x:
        if i ==" ":
            space+=1
        if i.isalpha()==True:
            letter+=1
        if i.isdigit()==True:
            number+=1
    z= "Space: "+str(space)+", Letter: "+str(letter)+", Number: "+str(number)
    return z
print(string_analysis("Hi my name is 123"))