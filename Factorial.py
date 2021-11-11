#Program to print the factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    while(n>1):
        return (n*factorial(n-1))
num=int(input("Enter the number to compute Factorial\n"))
if(num>=0):
    print("The Factorial of ",num," is",factorial(num))
else:
    print("You need to enter a positive number to compute factorial\n")