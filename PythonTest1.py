#1 Python Code to Print the Time in Hour,Min and Seconds Format given Time in seconds.
seconds = int(input("Enter the number of seconds\n"))
hours = seconds//3600
minutes = seconds//60-hours*60
seconds = seconds%60
print(hours, " Hours",minutes," minutes",seconds, " seconds")

#2 Python Code to approximate the value of PI using Walli's Series.
#PIE/2=(2*2/1*3)*(4*4/3*5)
LIMIT=100
n=2
PI=1
for i in range(1,LIMIT+1):
    PI=PI*(n*n)/((n-1)*(n+1))
    n=n+2
print(PI*2)

#3 Python Code to print trim the list such that min and max values are removed from list passed as arg.
def trim(lst):
    miny=min(lst)
    maxy=max(lst)
    temp_lst=[]
    for i in range(len(lst)):
        if(lst[i]==miny or lst[i]==maxy):
            continue
        else:
            temp_lst.append(lst[i])
    return temp_lst
test=[23,452,523,544,2,32,2,2,2,2,2,234,243,6534,287,329]
print("The Original List is:\n")
print(min(test))
print(test)
print("The Trimmed List is:\n")
print(trim(test))

#4 Python Code to find the pythagorean triplets with sides below 100
for x in range(1,LIMIT+1):
    for y in range(x,LIMIT+1):
        for z in range(y,LIMIT+1):
            if (z*z==x*x+y*y):
                print(x," ",y," ",z)