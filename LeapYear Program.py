"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-08 15:00:00
Title : Leap Year Program
"""

def check_year():
    Year = int(input("Enter the Year: "))
    if Year>999:
           CheckLeap(Year)
    else:
        print("Please Enter the 4-digit Year:")
        check_year()

def CheckLeap(Year):

    if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)):
        print("Given Year is a leap Year");
    else:
        print ("Given Year is not a leap Year")
check_year()