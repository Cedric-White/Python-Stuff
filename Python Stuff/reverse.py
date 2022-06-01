import math

def print_reverse(num):
    stringA = str(num%10)
    stringB = str((num//10)%10)
    stringC = str((num//10**2)%10)
    stringD = str(num//10**3)
    print(stringA + stringB + stringC + stringD)

def return_reverse(num):
    stringA = str(num%10)
    stringB = str((num//10)%10)
    stringC = str((num//10**2)%10)
    stringD = str(num//10**3)
    nString = (stringA + stringB + stringC + stringD)
    return nString

num1 = int(input("Give me a number: "))
print_reverse(num1)
return_reverse(num1)
