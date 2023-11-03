import random as rd


def make_a_bet () :
    random_number = rd.random()
    if random_number < 0.5 :
        return "heads"
    else : return "tails"

def get_bet_hash (bet) :
    return hash(bet)

def flip_a_coin () :
    random_number = rd.random()
    if random_number < 0.5 :
        return "heads"
    else : return "tails"

alice_bet = make_a_bet()
alice_hash = get_bet_hash(alice_bet)
bob_flip = flip_a_coin ()
bob_hash = get_bet_hash(bob_flip)
print(alice_bet, bob_flip, alice_bet == bob_flip)
print(alice_hash, bob_hash, alice_hash == bob_hash)