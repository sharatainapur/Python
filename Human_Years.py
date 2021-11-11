#Program to Convert Human Years to Dog Years
human_year=int(input("Enter the human years\n"))
if human_year <=2:
    dog_year=10.5*human_year
else:
    dog_year=(10.5*2)+(4*(human_year-2))
print("The Dog Years equivalent to human year",human_year," is",dog_year)

#INPUT=1 OUTPUT=10.5
#INPUT=2 OUTPUT=21.0
#INPUT=3 OUTPUT=25.0
#INPUT=4 OUTPUT=29.0