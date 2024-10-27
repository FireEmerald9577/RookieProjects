import random

def cardValue():
    chance = [36/52] * 9 + [16/52]
    card = list(range(2, 12))
    return random.choices(card, weights=chance)[0]

balance = input("enter your balance: $ ")
while True:
    status = ""
    balance = balance
    bet = 0
    while bet == 0:
        bet = input("place your Bet: $ ")
        if bet == "allin":
            bet = balance
        if int(bet) > int(balance):
            print("you don't have enough money")
            bet = 0
        else:
            print("you have bet $", bet)

    dealer1 = cardValue()
    dealer2 = cardValue()
    dealer = dealer1 + dealer2

    draw1 = cardValue()
    draw2 = cardValue()
    hand = draw1 + draw2

    print("--------BLACKJACK--------")
    print("Dealer's hand = ", dealer1)
    print("Your hand = ", draw1, "and ", draw2)

    if hand == 21:
        print("You win!")
        status = "win"
    elif dealer == 21:
        print("Dealer wins!")
        status = "lose"
    else:
        status = ""
        while hand < 21 or status == "":
            choice = input("Your choice! (D to draw, S to stand): ")
            if choice == "D":
                draw3 = cardValue()
                hand = hand + draw3
                print("Your hand = ", hand)
                draw3 = 0
                if hand > 21:
                    print("You lose!")
                    status = "lose"
                elif hand == 21:
                    print("You win!")
                    status = "win"
            elif choice == "S":
                while dealer < 17:
                    dealdraw = cardValue()
                    dealer = dealer + dealdraw
                    print("Dealer draws. Dealer's hand: ", dealer)
                    dealdraw = 0
                    if dealer > 21:
                        print("You Win!")
                        status = "win"
                    elif dealer > hand:
                        print("You Lose! Dealer's hand = ", str(dealer))
                        status = "lose"
                    elif dealer == hand:
                        print("It's a tie!")
                        status = "tie"
                if dealer < hand:
                    print("Dealer's hand = ", str(dealer))
                    print("You Win!")
                    status = "win"
            if status == "win":
                balance = int(balance) + int(bet)
                break
            elif status == "lose":
                balance = int(balance) - int(bet)
                break
            elif status == "tie":
                break
    choice2 = input("Good Game, you now have $"+str(balance)+" wanna go again?(Y/N): ")
    if choice2.upper() != "Y":
        break
