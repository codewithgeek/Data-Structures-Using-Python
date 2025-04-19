#FACTORIAL PROGRAM
#using for loop

n = int(input("Enter a number"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    
print("the factorial is", fact)

#using Recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter the number: "))
print("the factorial of", num, "is:  ", fact(num))
