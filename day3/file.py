import re

import numpy as np


file = open("day3/input.txt", "r")
cards = file.readlines()

def getValue(card):
    match = re.search(r'Card +\d+:(.*) \| (.*)', card)
    matches = match.groups()
    winningNumbers = list(filter(lambda x: x!= '', matches[0].split(" ")))
    myNumbers = list(filter(lambda x: x!= '', matches[1].split(" ")))
    return len([value for value in myNumbers if value in winningNumbers])
   
copies = np.ones(len(cards))
for index, card in enumerate(cards):
    size = getValue(card)
    copies[index + 1 : index + 1 + size] += copies[index]


print (f'Sum: {copies.sum()}')
