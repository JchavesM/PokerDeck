# PokerDeck
Poker deck modelled through the Python Data model

Card example:
```python
>>> card = Card("7", "diamonds")
>>> card
Card(rank='7', suit='diamonds')
```

Deck and picking a card example:
```python
>>> deck = FrenchDeck()
>>> len(deck)
52

>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
```

Random draw example:
```python
>>> choice(deck)
Card(rank='6', suit='clubs')
>>> choice(deck)
Card(rank='5', suit='diamonds')
>>> choice(deck)
Card(rank='9', suit='spades')
```

Slicing example:
```python
>>> deck[:3]    
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
>>> deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
```

Iteration example:
```python
>>> for card in deck:
...     print(card)
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
Card(rank='5', suit='spades')
Card(rank='6', suit='spades')
...

>>> for card in reversed(deck):
...     print(card)
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
Card(rank='J', suit='hearts')
Card(rank='10', suit='hearts')
Card(rank='9', suit='hearts')
...
```

Membership example:
```python
>>> Card('Q', 'hearts') in deck
True
>>> Card('Q', 'horses') in deck
False
```

Sorting example:
```python
>>> for card in sorted(deck, key=spade_ace_high):
...     print(card)
... 
Card(rank='2', suit='spades')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='clubs')
Card(rank='2', suit='hearts')
Card(rank='3', suit='spades')
Card(rank='3', suit='diamonds')
...
Card(rank='K', suit='diamonds')
Card(rank='K', suit='clubs')
Card(rank='K', suit='hearts')
Card(rank='A', suit='spades')
Card(rank='A', suit='diamonds')
Card(rank='A', suit='clubs')
Card(rank='A', suit='hearts')
```

Shuffle monkey patching example:
```python
>>> def set_card(deck: FrenchDeck, position: int, card: Card) -> None:
...     deck._cards[position] = card
>>> FrenchDeck.__setitem__ = set_card
>>> shuffle(deck)
>>> deck[:5]
[Card(rank='A', suit='spades'), Card(rank='J', suit='diamonds'), Card(rank='8', suit='hearts'), Card(rank='2', suit='hearts'), Card(rank='Q', suit='diamonds')]
```