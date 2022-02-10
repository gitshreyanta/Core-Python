"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2021-02-11 15:00:00
Title : flipcoin Program
"""
import random
import itertools

def flip_coin(num):
    tail_count = 0
    head_count = 0

    for i in range(num):
        flip = random.uniform(0,1)
        #print(flip)
        if flip > 0.5 :
            head_count +=1
        else:
            tail_count +=1

    print("Head count :" , head_count)
    print ("Tail Count :", tail_count)

    tail_percentage = ((tail_count / num)*100)
    head_percentage = ((head_count / num)*100)

    print('Head Percentage:',head_percentage )
    print('Tails Percentage:',tail_percentage )
num = int(input("Please Enter The number of times to Flip Coin:"))
flip_coin(num)

