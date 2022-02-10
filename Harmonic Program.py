"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2021-02-11 15:00:00
Title : Harmonic Program
"""
def nthHarmonic(num):

  harmonic = 1.00
  for i in range(2, num + 1):
    print("1/",i)
    harmonic += 1 / i

  return harmonic

if __name__ == "__main__":
    num = int(input("Enter the number:"))
    print(round(nthHarmonic(num), 5))




