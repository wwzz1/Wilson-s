def de_to_binary():
    x=float(input("Enter the decimal: "))
    #bin_x=bin(x)
    p=x
    bin_x=0
    n=0
    while x!=0:
        v=x%2
        if v==1:
            bin_x=(10**n)+bin_x
            n+=1
            x=x-1
        else:
            n+=1
            x = x / 2
    print(bin_x)

    print("The binary number of", p, "is: ", bin_x)
    '''
z=input("What kind of number do you have? (d,b,h)")
y=input("What kind of number do you wish to convert to? (d,b,h)")
if z=="d" and y=="b":
    '''
de_to_binary()