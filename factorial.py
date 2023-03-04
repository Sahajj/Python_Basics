#  How to find factorial of a number:
# 
# 
# num = 5 
# 
# 1*2*3*4*5=120 

Factorial = 1

num = int(input("Enter the value:"))

if num<0:
    print("Factorial does not exitst for -ve numbers")
elif(num == 0):
    print("the facrotrial of Zero is 1")
else:
    for i in range(1,num+1):
        Factorial = Factorial * i
    print("The factorail of", num , "is", Factorial)


print("\n\n")
# Approach 2 

n = int(input("Enter the value :"))


def Facto(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n * Facto(n-1)

print("Factorial of ", n, "is", Facto(n))

#  Ternary operator 

# num2 = int(input("Enter the value :"))

# def eazzy(num2):
#     return 1 if(n==1 or n==0) else n*eazzy(n-1)

# print("Factorial of ", num2, "is", eazzy(num2))

