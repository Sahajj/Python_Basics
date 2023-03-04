#  Natural Number > 1
#  which has only 2 factors 1 and itself 
# 
# 19 => 1 and 19 => Prime number
#  28 => 1,2,3,4,7,14,28 => Not a prime number

num = int(input("Enter the value you want to check\n"))

count = 0

if(num > 1):
    for i in range(1, num+1):
        if(num%i) == 0:
            count = count + 1  
    
    if count == 2:
        print("Number is Prime")
    else:
        print("number is not Prime")