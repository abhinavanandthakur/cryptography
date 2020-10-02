from random import randint

def generate_random(): #function generating a random number in binary form and then converting to integer
    number="1"
    for _ in range(1,64): 
        number=number+str(randint(0,1))
    return int(number,2)

def sqr_modulo(a,b,n):#FUNCTION IN QUESTION 3
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


def fermat(): #fermat's theorem implementation (randomised)
    iter=int(input("How many iterations:"))
    randon_number=generate_random()
    print("The number",randon_number,"is",end=" ")

    for _ in range(iter):
        a=randint(1,randon_number-1)
        if (sqr_modulo(a,randon_number-1,randon_number)!=1):
            return False
    return True

ret=fermat()
if (ret==True):
    print("Prime")
    pass
else:
    print("Not Prime")


    


