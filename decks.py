import random
import itertools

class card:
  def __init__(self, number, suit, value):
    self.number = number
    self.suit = suit
    self.value = value
  def display(self):
    print(str(self.number)+self.suit)

class hand:
  def __init__(self):
    self.cards = []
  def add_card(self, card):
    self.cards.append(card)

class deck:
  def __init__(self):
    number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    numberVal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A"]
    suits = ["♣", "♠", "♥", "♦"]
    combinations = list(itertools.product(number, suits))
    self.unshuffled_deck = [card(combo[0], combo[1], numberVal[number.index(combo[0])]) for combo in combinations]
    self.deck = self.unshuffled_deck
    self.discard = []
  def shuffle(self) -> None:
    self.deck = self.unshuffled_deck
    random.shuffle(self.deck)
    self.discard = []
  def get_top_card(self) -> list:
    return self.deck[0]
  def discard_top_card(self):
    top_card = self.get_top_card()
    self.deck.pop(0)
    self.discard.append(top_card)
  def put_discard_under_deck(self):
    self.deck.extend(self.discard)
  def deal(self, number, *hands: hand):
    counter = 0
    while counter < number:
      

test = deck()
for x in test.deck:
  x.display()
test.shuffle()
for x in test.deck:
  x.display()
test.shuffle()
for x in test.deck:
  x.display()