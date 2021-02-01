# Run with “python3 ben_lee_hw1.py”. 
# Enter a number when requested for user input, and it will print out whether it is a leap year or not.

year = int(input("Please enter a year: "))
print(year)
if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
   print("It is a leap year.")
else:
   print("It is not a leap year.")

