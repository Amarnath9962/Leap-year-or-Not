print("Mini Project ")
Year = int(input("Please enter the year :"))

def Leap_year(Year):
    if (Year % 4==0 and (Year % 100!=0 or Year % 400 ==0 )):
        print("Entered year is Leap Year :",Year)
        print()
    else:
        print("Entered year is not leap year :",Year)
        print()

Leap_year(Year);
print("Check in below calendar.")
import calendar
# print(calendar.calendar(Year))
year = calendar.month(Year,2)
print(year)