"""This is a simple program that will ask the user to provide any year as input to check whether it is a leap year
or not and after calculation it will return the result"""

while True:  # A loop that will keep asking the user for the year as input

    year = int(input("Which year do you want to check: "))  # Year as input
    if year % 4 == 0 and year % 100 != 0:  # It will check if a year evenly divisible by 4 but not 100
        print("We have a leap year")  # Print the result
    elif year % 100 == 0 and year % 400 == 0:  # As per the Gregorian calendar's rule
        print("Aha, we have a leap year")  # Print the result
    else:
        print("Nope! Not a leap year ")  # If all the above conditions failed

