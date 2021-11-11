#Program to print the Non-Trivial Factors of Numbers
LOWER_LT=2
UPPER_LT=100
for i in range(LOWER_LT,UPPER_LT+1):
    print(i,": ",end="")
    for j in range(2,i):
        if(i%j==0):
            print(j,"",end="")
    print()   