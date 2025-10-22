from typing import NamedTuple

class Card(NamedTuple):
    rank: str
    suit: str

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position: int) -> Card:
        return self._cards[position]
    
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def set_item(deck, key: int, value: Card) -> None:
    deck._cards[key] = value

def spade_ace_high(card: Card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(FrenchDeck.suits) + suit_values[card.suit]