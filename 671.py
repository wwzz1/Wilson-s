
#1
a = 10
b = 20
c = 30

def foo1(a, b):
  a = b + c
  print(a)
  return a


def foo2(b, c):
  b = a + c
  print(b)
  return b


def foo3(a, c):
  c = a + b
  print(c)
  return c

foo1(3, 4) #34
foo2(5, 6) #16
foo3(7, 8) #27
foo2(foo1(1, 2), foo2(1, 2)) #32 #12 #22
foo2(foo2(3, 4), foo3(2, 9)) #14 #22 #32

#2
def add(num1, num2):
  return num1 + num2

def triple(num):
  return add(num, add(num, num))
def quadruple(num):
    return add(num, triple(num))
print(quadruple(2))
#3
 