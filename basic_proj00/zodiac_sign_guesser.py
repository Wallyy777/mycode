#!/usr/bin/env python3
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid date"

# Get user input
While True:

    day = int(input("Enter the day of your birth (1-31): "))
   
    if day < 1 or day > 31:
        print("Invalid day. Please enter a valid day between 1 and 31.")
        continue

    month = int(input("Enter the month of your birth (1-12): "))
    if month < 1 or month > 12:
        print("Invalid month. Please enter a valid month between 1 and 12.")
        continue

    # Valid input, break out of the loop
    break

# Call the function and print the zodiac sign
    zodiac_sign = get_zodiac_sign(day, month)
    print(f"Your zodiac sign is: {zodiac_sign}")


