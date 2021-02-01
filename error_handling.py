# Run with “python3 ben_lee_hw1.py”. 
# Enter a number when requested for user input, and it will print out whether it is a leap year or not.
while True:
    try: 
        year = int(input("Please enter a year: "))
        if year >=0:
            break
    except:
        print("That's not a valid integer.")
if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
   print("It is a leap year.")
else:
   print("It is not a leap year.")

