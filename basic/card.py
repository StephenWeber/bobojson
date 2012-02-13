import bobo
import json
from random import choice
from itertools import product

SUITS = ['spades', 'hearts', 'clubs', 'diamonds']
PIPS = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

def new_deck():
    return ['%s of %s' % (p, s) for p in PIPS for s in SUITS]

@bobo.subroute('/cards', scan=True)
class Deck:
    current_deck = new_deck()

    def __init__(self, bobo_request):
        pass

    @bobo.query('')
    def redirect(self, bobo_request):
        return bobo.redirect(bobo_request.url+'/')

    @bobo.query('/')
    def reset(self, bobo_request):
        Deck.current_deck = new_deck()
        return 'Deck reset to 52 cards.'

    @bobo.query('/:quantity?')
    def get_cards(self, bobo_request, quantity=1):
        num_left = len(Deck.current_deck)
        qty = int(quantity)
        if num_left < qty:
            return 'Could not fulfill request, %d cards left.' % num_left
        draw = list()
        for i in range(qty):
            card = choice(Deck.current_deck)
            s = set(Deck.current_deck)
            s.remove(card)
            Deck.current_deck = list(s)
            draw.append(card)
        return json.dumps({'drawn_cards':draw})

application = bobo.Application(bobo_resources=__name__)
