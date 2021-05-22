import random
import itertools

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

deck = list(itertools.product(values, suits))

def shuffle_deck(deck):
    count = 0

    while count < len(deck):
        current = deck[random.randint(0, len(deck)-1)]

        if current in deck:
            deck.remove(current)

        deck.insert(0, current)

        count += 1

    return deck

print(shuffle_deck(deck))