"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2021-02-11 15:00:00
Title : PowerofTwo Program
"""


def power_intput():
    num = int(input("Enter the power: "))
    if 0<= num< 31:
        pow_of_two(num)
    else:
        print("Enter value between 0 and 31")
        power_intput()

def pow_of_two(num):
    counter = 0;
    while counter<=num:
        print(pow(2, counter))
        counter += 1

power_intput()
