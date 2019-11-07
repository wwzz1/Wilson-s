from math import sqrt
print(9%7)
print(8*4-4)
print(bool(4))
print(10+abs((-1*4)))
print(pow(4,4)%2+1)
print(20-int(14.5))
print(bool(10-5*int(2.2)))
print(divmod(19,4))
print(str(5*10-(13+5)))
print(float(int(True)+4-(15%4)))
print(1<4 and 3>2)
print(len("Hi")<3)
print(6<8 or 10>12)
print(not(7>10))
print(5>6 and 7>8)
print(not(5>6 and 7>8))
print('A'!='B' and 10/5 == 2)
print('A'!='B' and 5/2==10)

#1 can't have caculation on the right hand side
a = 10
b = 100-1
print(a, b)

#2 can't have  calculation inside a print()
var1 = 100
var2 = 50
var1 += 10
print(var1)

#3
a = 'Hi'
b = 'Bye'
a += a + b
a *= 2
print(a)
#4 can't do any calculation in the function, second line has to be "=", cannot use += with text
my_name = 'Mr. Bach'
your_name = 'Mr. Student'
x = my_name + ' or ' + your_name + '?'
print(x)

#5
this_val = False
that_val = True
some_val = 0
this_val += 1
print(this_val)
this_val = False
that_val = False
print(some_val+ 0)

a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
c=int(input("Please enter c: "))
x=-(b+(sqrt(b**2-(4*a*c))))/2*a
y=-(b-(sqrt(b**2-(4*a*c))))/2*a
print(x,y)

a=True
b=True
c=True
x= a and b or not a or c
print(x)