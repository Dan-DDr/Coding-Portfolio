from random import shuffle
class Card:
	"""A Card Instance has two properties suit and value. 
	Created by Card(suit,value)"""
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	def __repr__(self):
		return f"{self.value} of {self.suit}"

suits = ('♠','♣','♦','♥')
values = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
class Deck:
	"""Deck has property .cards which contains all 52 cards. 
	Has .deal_hand(num) which allows you to deal a num hand
	Has .shuffle() which shuffles the Deck instance
	"""
	def __init__(self):
		self.cards = [Card(suit,value) for value in values for suit in suits]

	def __len__(self):
		return len(self.cards)

	def __repr__(self):
		return f"A Deck of {len(self.cards)} cards"

	def _deal(self, num):
		return self.cards[:num]

	def deal_hand(self, num):
		hand = self._deal(num)
		self.cards = self.cards[num::]
		return hand
	def shuffle(self):
		shuffle(self.cards)