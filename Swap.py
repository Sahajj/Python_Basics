num1=input("enter num1 value:")
num2 = input("Enter num2 value:")

print("value of num1 befour swapping", num1)
print("value of num2 befour swapping", num2)

# Approach 1
# Using temp variable
temp = num1 
num1 = num2
num2 = temp

print("calue of num1 after swapping:",num1)    
print("calue of num2 after swapping:",num2)

# Approach 2
print("\n") 
num3=input("enter num3 value:")
num4 = input("Enter num4 value:")
num3,num4=num4,num3

print("calue of num3 after swapping:",num3)    
print("calue of num4 after swapping:",num4)

