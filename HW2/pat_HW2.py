#Patrick Leimer, HW2 BlackJack 02/05/2024
from p1_random import P1Random
rng = P1Random()
def dealCard():
    return rng.next_int(13) + 1
def aJQK(cards, cardIndex, playerHand):
    if(cards[cardIndex - 1] == 13):
        cards[cardIndex - 1] = 10
        playerHand[0] += cards[cardIndex - 1]
        return "KING"
    elif (cards[cardIndex - 1] == 12):
        cards[cardIndex - 1] = 10
        playerHand[0] += cards[cardIndex - 1]
        return "QUEEN"
    elif (cards[cardIndex - 1] == 11):
        cards[cardIndex - 1] = 10
        playerHand[0] += cards[cardIndex - 1]
        return "JACK"
    elif (cards[cardIndex - 1] == 1):
        playerHand[0] += cards[cardIndex - 1]
        return "ACE"
    else:
        playerHand[0] += cards[cardIndex - 1]
        return cards[cardIndex-1]
def printMenu():
    print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")

#Variables for player and dealer
gameCount, choiceU = 0, 1
#Variables for statistics
playerWins, dealerWins, tieGames = 0, 0, 0

while True:
    player1, dealer1 = [], []
    playerHand, dealerHand = [0], 0
    cardsDealt = 0
    print(f"\nSTART GAME #{gameCount + 1}\n")
    player1.append(int(dealCard()))
    cardsDealt += 1
    print(f"Your card is a {aJQK(player1, cardsDealt, playerHand)}!")
    print(f"Your hand is: {playerHand[0]}")
    while choiceU != 4:
        printMenu()
        choiceU = int(input("Choose an option: "))
        if(choiceU == 1): #Get another card
            player1.append(int(dealCard()))
            cardsDealt += 1
            print(f"\nYour card is a {aJQK(player1, cardsDealt, playerHand)}!")
            print(f"Your hand is: {playerHand[0]}")
            if(playerHand[0] == 21):
                print("\nBLACKJACK! You win!")
                playerWins += 1
                gameCount += 1
                break
            elif(playerHand[0] > 21):
                print("\nYou exceeded 21! You lose.")
                dealerWins += 1
                gameCount += 1
                break

        elif(choiceU == 2): #Hold
            dealerCardDealt = 0
            while dealerHand < 16:
                dealerHand = int(rng.next_int(11) + 16) #16 to 26
                print(f"\nDealer's hand: {dealerHand}\nYour hand is: {playerHand[0]}\n")
            if dealerHand > 21 or playerHand[0] > dealerHand:
                print("You win!")
                playerWins += 1
                gameCount += 1
                break
            elif dealerHand == playerHand[0]:
                print("It's a tie! No one wins!")
                tieGames += 1
                gameCount += 1
                break
            elif dealerHand > playerHand[0]:
                print("Dealer wins!")
                dealerWins += 1
                gameCount += 1
                break

        elif(choiceU == 3): #Print statistics
            print(f'''\nNumber of Player wins: {playerWins}\nNumber of Dealer wins: {dealerWins}\nNumber of tie games: {tieGames}\nTotal # of games played is: {gameCount}\nPercentage of Player wins: {round(playerWins/gameCount, 2)*100}%''')
        elif( choiceU < 1 or choiceU > 4):
            print('''\nInvalid input!\nPlease enter an integer value between 1 and 4.''')
    if(choiceU == 4): #Exit
        break