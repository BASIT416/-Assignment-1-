#Question no 1:
number=int(input("Enter a number:"))
if (number>=0 | number<=100):
    if number<=10:
        print("Low Range")
    elif number<=50:
        print ("Medium Range")
    elif number<=100:
        print("High Range")
else:
    print("Out of range")

#Question no 2:
year=int(input("Enter a year: "))
if year%4==0:
    print("This is a leap year")
else:
    print("Not a Leap Year")