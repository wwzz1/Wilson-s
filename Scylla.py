from fractions import Fraction
from math import pi
#1
def mixed_number(a,b):
    x=str(a//b)
    y=str(a%b)
    b=str(b)
    z=x+" "+y+"/"+b
    return z
print(mixed_number(5,2))
#2
def vowel_count_1(x):
    num=0
    for char in x:
        if char in "aeiouAEIOU":
            num+=1
    return num
print(vowel_count_1("This is a sample"))
#3
def vowel_count_2(x):
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
    return numa,nume,numi,numo,numu
print(vowel_count_2("This is a sample"))
#4
def sphere_volume(x):
    x=float(x)
    y=4/3*(pi)*(x**3)
    return y
print(sphere_volume(10))
def sphere_surface_area(x):
    x=float(x)
    y=4*pi*(x**2)
    return y
print(sphere_surface_area(10))
#5
def sphere_metics(x):
    x=float(x)
    y=str(sphere_volume(x))
    y="Sphere Volume "+y
    z=str(sphere_surface_area(x))
    z="Sphere Surface Area: "+z
    return y, z
print(sphere_metics(10))
#6
def name_function(x):
    if x=="Ted":
        return "Ted", 50, 80
print(name_function("Ted"))
#7
def rgb_to_hex(r,b,g):
    r=hex(r)
    g=hex(g)
    b=hex(b)
    return r,g,b
print(rgb_to_hex(255,0,0))
def hex_to_rgb(r,b,g):
    r=int(r, 16)
    g=int(g, 16)
    b=int(b, 16)
    return r,g,b
print(hex_to_rgb("ff","00","00"))
