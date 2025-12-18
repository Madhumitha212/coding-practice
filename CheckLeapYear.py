year = input("Enter year: ")

# Check if input is a 4-digit number
if len(year) != 4:
    print("Invalid Digit")
else:
    year = int(year)
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")