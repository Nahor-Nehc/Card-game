import random
import itertools
from typing import List

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

  def add_card(self, card: card):
    self.cards.append(card)

class deck:
  def __init__(self, game: str = "blackjack"):
    number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    if game == "blackjack":
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

  def get_top_card(self) -> card:
    return self.deck[0]

  def discard_top_card(self):
    top_card = self.get_top_card() # order ensures cards are never accidentally duplicated
    self.deck.pop(0)
    self.discard.append(top_card)

  def put_discard_under_deck(self):
    self.deck.extend(self.discard)

  def deal(self, number, hands: list[hand]):
    counter = 0
    start_deck_len = len(self.deck)
    attempt_draw_len = number*len(hands)
    while counter < number:
      for hand in hands:
        if len(self.deck) == 0:
          raise Exception(f"Deck has ran out of cards. Starting deck had {start_deck_len} cards. Attempted to draw {attempt_draw_len}")
        hand.add_card(self.get_top_card())
        self.discard_top_card()
      counter += 1

test = deck()
hand1 = hand()
hand2 = hand()
hand3 = hand()
hands = [hand1, hand2, hand3]
for x in test.deck:
  x.display()
test.shuffle()

test.deal(10, hands)
for v_hand in hands:
  print()
  for x in v_hand.cards:
    x.display()
print()
for x in test.deck:
  x.display()