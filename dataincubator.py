import pandas as pd
import numpy as np

def P_calculator(cards, suits):
    number_suits = int(cards/suits)
    lists = [[j for j in range(((number_suits * i)+1),(number_suits*(i + 1)+1))] for i in range(suits)]



    card_list =[]
    for i in range(cards):
        card_list.append(np.random.randint(1, cards))

    p = 0

    for i in range(1, len(card_list)):
        for suit in lists:
            if (card_list[i-1] in suit) and (card_list[i] in suit):
                p += 1
    return p
#runnning the code to find different points in each iteration, we will find the mean and std by running the code several times.
p =[]
for i in range(2000000):
    p.append(P_calculator(26,2))
p = np.array(p)
conditional_probabality = ((p>=12).sum())/(p >=6).sum()

print( conditional_probabality)

#finding the mean and standard deviation,
#print(p)
#print("mean", np.mean(p), np.std(p))


