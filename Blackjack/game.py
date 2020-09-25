from CardAndDeck import Card, Deck


p_money = 10000.0
d_money = 10000.0

values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values_to_pts = dict(zip(values[:-3], range(2, 11)))
values_to_pts.update({'J': 10, 'Q': 10, 'K': 10})


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


def calculate_winner(hand1, hand2, bid):
    best_hands = calculate_best_hands(hand1, hand2)
    global p_money
    global d_money
    if best_hands[0] == best_hands[1]:
        print("Its a draw!")
        p_money += bid
        d_money += bid
    elif best_hands[0] == 21:
        print(f"Blackjack! You Win ${bid}")
        p_money += 3/2*bid
    elif best_hands[1] == 21:
        print(f"Blackjack! Dealer Wins ${bid}")
        d_money += 3/2*bid
    elif best_hands[0] > best_hands[1]:
        print(f"You Win ${bid}!")
        p_money += 2*bid
    elif best_hands[0] < best_hands[1]:
        print(f"Dealer wins ${bid}!")
        d_money += 2*bid


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
    print(f"Dealer's money: {d_money}")
    print(f"Your Hand: {p_hand}\nYour Worth: {pts}\nYour money: {p_money}\n")


print("\nWelcome to Blackjack!")
while True:
    answer = input("Type y to continue or n to quit...\n")
    if answer == 'n':
        quit()
    elif answer == 'y':
        break


while p_money > 0:
    while True:
        bid = input("Make a bid or enter q to quit\n")
        try:
            bid = float(bid)
            p_money -= bid
            d_money -= bid
            break
        except ValueError:
            if bid == 'q':
                break
            print("Please enter a number\n")
    if bid == 'q':
        break
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
                print("\nDealer is playing...")

                while min(d_pts) < 17:
                    d_hand.append(*deck.deal_hand(1))
                    d_pts = calculate_pts(d_hand)

                display_board(state=True)
                if min(d_pts) > 21:
                    print(f"Dealer Busts! You Win ${bid}")
                    p_money += 2*bid
                    break
                calculate_winner(p_hand, d_hand, bid)
                break
        else:
            print(f"You bust! Sorry you lost ${bid}")
            d_money += 2*bid
            break

if d_money < 0:
    print("Wow, you won all the money I had, Congrats!")

elif p_money < 0:
    print("I think you should stop playing. Losing that much money has got to hurt.")
else:
    print(f"Congrats you won ${p_money - 10000.0}")
