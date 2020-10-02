def rep_mul_modulo(a,b,n): #repeated multiplication modilo N method
    c=a%n
    for _ in range(1,b):
        c=(c*a)%n
    return c

a=int(input("write the input a:"))
b=int(input("write the input b:"))
n=int(input("write the input n:"))

print ("The modulo is:",rep_mul_modulo(a,b,n))

