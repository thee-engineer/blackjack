from enum import Enum
import random
import api 


# register a player

# the initialization of the game
def initGame(no_of_players):
    if no_of_players > 9:
        return "too many players, we cannot support more than 9 players"
    elif no_of_players < 1:
        return "the game needs at least one player"

if __name__ == "__main__":
    deck = api.Deck()
    print(deck.getNextCard().value)
        