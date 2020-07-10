from CardAndDeck import Card, Deck


values = ('2','3','4','5','6','7','8','9','10','J','Q','K')
values_to_pts = dict(zip(values[:-3],range(2,11)))
values_to_pts.update({'J':10,'Q':10,'K':10})


p_money = 10000.0
d_money = 10000.0
gamestate = True

def calculate_best_hands(hand1, hand2):
	hands = [calculate_pts(hand1), calculate_pts(hand2)]
	best_hands = []
	for hand in hands:
		if max(hand) <= 21:
			best_hands.append(max(hand))
		elif min(hand) <= 21:
			best_hands.append(min(hand))
	return best_hands

def calculate_pts(hand):
	pts = 0
	pts2 = 0
	for card in hand:
		if card.value == 'A':
			pts += 1
			pts2 += 11
		else:
			pts += values_to_pts[card.value]
			pts2 += values_to_pts[card.value]
	return (pts, pts2)

def display_board(state=False):

	if p_pts[0] == p_pts[1] or p_pts[1] > 21:
		pts = p_pts[0]
	else:
		pts = p_pts

	if state:
		if d_pts[0] == d_pts[1] or d_pts[1] > 21:
			pts_d = d_pts[0]
		else:
			pts_d = d_pts
		print(f"\nDealer's Hand: {d_hand}\nDealer's Worth: {pts_d}")
	else:
		print(f"\nDealer's Hand: {[d_hand[0],'*']}")

	print(f"Your Hand: {p_hand}\nYour Worth: {pts}\n")
	
def calculate_winner():
	best_hands = calculate_best_hands(p_hand, d_hand)
	if best_hands[0] == best_hands[1]:
		print("Its a draw!")
	elif best_hands[0] == 21:
		print("Blackjack! You Win")
	elif best_hands[1] == 21:
		print("Blackjack! Dealer Wins")
	elif best_hands[0] > best_hands[1]:
		print("You Win!")
	elif best_hands[0] < best_hands[1]:
		print("Dealer wins!")


print("\nWelcome to Blackjack!")
while True:
	answer = input("Type y to continue or n to quit...\n")
	if answer == 'n':
		quit()
	elif answer == 'y':
		break

while gamestate:	
	deck = Deck()
	deck.shuffle()

	p_hand = deck.deal_hand(2)
	d_hand = deck.deal_hand(2)

	p_pts = calculate_pts(p_hand)
	display_board()

	while True:
		if min(p_pts) <= 21:
			p_choice = input("What do you want to do?\nHit, Stand...\n")
			if p_choice.lower() == "hit":
				p_hand.append(*deck.deal_hand(1))
				p_pts = calculate_pts(p_hand)
				display_board()
			elif p_choice.lower() == 'stand':
				d_pts = calculate_pts(d_hand)

				while min(d_pts) < 17:
					d_hand.append(*deck.deal_hand(1))
					d_pts = calculate_pts(d_hand)

				display_board(state=True)
				if min(d_pts) > 21:
					print("Dealer Busts! You Win")
					break
				calculate_winner()
				break
		else:
			print("You bust! Sorry you lose :(")
			break

	while True:
		answer = input("Do you want to play again or quit?(y/n)\n")
		if answer == 'n':
			quit()
		elif answer == 'y':
			break
	



