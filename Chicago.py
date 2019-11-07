import random
#1
def driving(a):
    if a>= 20:
        z=True
        return z
    else:
        z= False
        return z
print(driving(16))
print(driving(25))
#2
def id_triangle(a,b,c):
    if a>=b and a>=c:
        side_c=a
        side_a=b
        side_b=c
    elif b>=a and b>=c:
        side_c=b
        side_a=a
        side_c=c
    else:
        side_c=c
        side_a=a
        side_b=b
    if side_c**2==a**2+b**2:
        return "Right-Triangle"
    elif side_c**2>a**2+b**2:
        return "Obtuse-Triangle"
    elif side_c**2<a**2+b**2:
        return "Acute-Triangle"
print(id_triangle(1,2,2))
#3
def fizzbuzz(x):
    if x>0 and x%3==0 and x%5==0:
        return "FIZZBUZZ"
    elif x>0 and x%3==0:
        return "FIZZ"
    elif x>0 and x%5==0:
        return "BUZZ"
    else:
        return "Huh?"
print(fizzbuzz(15))
#4
def guess_dice(a,b,c):
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    count = 0
    if x == a:
        count += 1
    if y == b:
        count += 1
    if z == c:
        count += 1
    return "Rolled: " + str(x) + " " + str(y) + " " + str(z) + ", with " + str(count) + " correct"
print(guess_dice(1,1,1))
#5
def gimme_random(type, a, b):
    if type == "int":
        a=int(a)
        b=int(b)
        num=int(random.randint(a,b))
        return num
    elif type == "float":
        num=float(random.uniform(a,b))
        return num
print(gimme_random("int", 2.3, 3))