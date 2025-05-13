"""
Contains the main functions
"""


import random as rd


def make_a_bet () :
    """
    Return a str containting a random bet between 'heads' and 'tails'
    """
    random_number = rd.random()
    if random_number < 0.5 :
        return "heads"
    return "tails"

def get_bet_hash (bet) :
    """
    Return the hash of a str
    """
    return hash(bet)

def flip_a_coin () :
    """
    Simulate a coin tossing, return 'heads' or 'tails'
    """
    random_number = rd.random()
    if random_number < 0.5 :
        return "heads"
    return "tails"

ALICE_BET = make_a_bet()
alice_hash = get_bet_hash(ALICE_BET)
BOB_FLIP = flip_a_coin ()
bob_hash = get_bet_hash(BOB_FLIP)
print(ALICE_BET, BOB_FLIP, ALICE_BET == BOB_FLIP)
print(alice_hash, bob_hash, alice_hash == bob_hash)
