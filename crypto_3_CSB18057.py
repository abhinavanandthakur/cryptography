def sqr_modulo(a,b,n): #repeated square modulo N method
    if (b==0):
        return 1%n
    elif(b==1):
        return a%n
    elif (b%2==0):
        c=sqr_modulo(a,b//2,n)
        return ((c%n)*(c%n))%n
    else:
        c=sqr_modulo(a,b//2,n)
        return ((c%n)*(c%n)*(a%n))%n

    pass

a=int(input("write the input a:"))
b=int(input("write the input b:"))
n=int(input("write the input n:"))

print ("The modulo is:",sqr_modulo(a,b,n))

