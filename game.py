from random import shuffle



VALUES = {
	'J': 10,
	'Q': 10,
	'K': 10,
	'A': 11
}


class Deck:

	cards = []

	SUITS = ['S', 'H', 'D', 'C']
	RANKS = [i for i in range(2, 11)] + 'J Q K A'.split()	

	def __init__(self):
		self.cards = [{'rank': r, 'suit': s} for r in self.RANKS for s in self.SUITS]
		self.shuffle()

	def shuffle(self):
		shuffle(self.cards)

	def take_first(self):
		return self.cards.pop(0)


class Hand:
	def __init__(self):
		self.hand = []
		self.score = 0
	
	def get_card(self, card):
		self.hand.append(card)
	
	@property
	def hand_value(self):
		total = 0
		for card in self.hand:
			if str(card['rank']) in 'JQKA':
				total += VALUES[card['rank']]
			else:
				total += card['rank']
		return total

class Player(Hand):
	
	def __init__(self, name=None):
		self.name = name
		super().__init__()

class Dealer(Hand):
	
	def show_one_card(self):
		return self.hand[0]

def init_turns(deck, player, dealer):
	for i in range(2):
		player.get_card(deck.take_first())
		dealer.get_card(deck.take_first())
		

def turn(deck, player, dealer):
	player.get_card(deck.take_first())
	dealer.get_card(deck.take_first())

def game():
	deck = Deck()
	player = Player()
	dealer = Dealer()

	init_turns(deck, player, dealer)

	GAME = True	
	
	print('Dealer:', dealer.show_one_card)
	print('Player:', player.hand, player.hand_value)

	while GAME:
		action = input('Hit (H) or Stand (S)')
		if action.lower().startswith('h'):
			player.get_card(deck.take_first())
			print('Player: \n', player.cards, player.hand_value)
			if player.hand_value > 21:
				print('Lose') 
				GAME = False
		if action.lower().startswith('s'):
			print(dealer.hand)
			while dealer.hand_value < 17:
				dealer.get_card(deck.take_first)
				print('Dealer:', dealer.hand, dealer.hand_value)
				if dealer.hand_value > 21:
					print('Win')
					GAME = False
			GAME = False	
	if player.hand_value > dealer.hand_value:
		print('Win')
		return
	else: 
		print('Lose')
		return
	
if __name__ == '__main__':
	game()

