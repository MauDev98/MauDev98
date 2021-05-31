# MODULES

import random
import os
def clear(): os.system('cls')


# GLOBAL VARIABLES
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |
      `------'                           |__/
"""


clubArt = {"\u2663": [(' A', 11), (' 2', 2), (' 3', 3), (' 4', 4), (' 5', 5), (' 6', 6), (' 7', 7), (' 8', 8), (' 9', 9), ('10', 10), (' J', 10), (' Q', 10), (' K', 10)],
           "\u2660": [(' A', 11), (' 2', 2), (' 3', 3), (' 4', 4), (' 5', 5), (' 6', 6), (' 7', 7), (' 8', 8), (' 9', 9), ('10', 10), (' J', 10), (' Q', 10), (' K', 10)],
           "\u2665": [(' A', 11), (' 2', 2), (' 3', 3), (' 4', 4), (' 5', 5), (' 6', 6), (' 7', 7), (' 8', 8), (' 9', 9), ('10', 10), (' J', 10), (' Q', 10), (' K', 10)],
           "\u2666": [(' A', 11), (' 2', 2), (' 3', 3), (' 4', 4), (' 5', 5), (' 6', 6), (' 7', 7), (' 8', 8), (' 9', 9), ('10', 10), (' J', 10), (' Q', 10), (' K', 10)]}

initialBank = [1000]

# GAME BETTING DISPLAY AND LOGIC


def actualizeMoney(listOfChips):
    totalMoney = sum(listOfChips)
    return totalMoney


def formatBank(bank):
    if len(str(bank)) == 3:
        bankAdjusted = " " + str(bank)
    elif len(str(bank)) == 2:
        bankAdjusted = "  " + str(bank)
    elif len(str(bank)) == 1:
        bankAdjusted = "   " + str(bank)
    else:
        bankAdjusted = str(bank)
    return bankAdjusted


def formatBet(bet):
    if len(str(bet)) == 4:
        betAdjusted = str(bet)
    if len(str(bet)) == 3:
        betAdjusted = " " + str(bet)
    if len(str(bet)) == 2:
        betAdjusted = "  " + str(bet)
    if len(str(bet)) == 1:
        betAdjusted = "   " + str(bet)
    return betAdjusted


def displayFirstTable(bank):
    print(logo)
    logoMoneyDisplay = actualizeMoney(bank)
    initialTable = """
        .─────────────────────────────────────.
        |                                     |
        |       BANK = $ {}                 |
        |                                     |
        |       YOUR BET = $ ???              |
        |                                     |
        .─────────────────────────────────────.
                         .-""-.         .-""-.         .-""-.         .-""-.        .-""-.         .-""-.
                        /      \.      /      \.      /      \.      /      \.     /      \.      /      \.
        POSSIBLE BETS: ;  ALL   ;     ;   25   ;     ;   50   ;     ;  100   ;    ;  250   ;     ;  500   ;
                        \  IN  /       \      /       \      /       \      /      \      /       \      /
                         '-..-'         '-..-'         '-..-'         '-..-'        '-..-'         '-..-'
    """.format(formatBank(logoMoneyDisplay))
    print(initialTable)


def displayOnGameTable(bank, bet):
    moneyDisplayed = actualizeMoney(bank) + bet
    onGameTable = """
        .─────────────────────────────────────.
        |                                     |
        |       BANK = $ {}                 |
        |                                     |
        |       YOUR BET = $ {}             |
        |                                     |
        .─────────────────────────────────────.
    """.format(formatBank(moneyDisplayed), formatBet(-1*bet))
    print(onGameTable)


def betResolution(initialBank, playerBet, WoL=True or False):
    if WoL == True:
        initialBank.append(-1*playerBet)
    elif WoL == False:
        initialBank.append(playerBet)


def makeABet(initialBank):
    cv = 0
    while cv == 0:
        allIn = actualizeMoney(initialBank)
        validBets = [allIn, "25", "50", "100", "250", "500"]
        playerBet = input(
            "Please enter a valid amount to bet // -ALL IN- -25- -50- -100- -250- -500-\n").upper()
        if playerBet in validBets:
            playerBet = int(playerBet)
            return (-1*playerBet)
        elif playerBet == "ALL IN":
            playerBet = allIn
            return (-1*playerBet)

# GAME LOGIC FUNCTIONS


def getScore(aListOfCards):
    aScore = sum(aListOfCards)
    return aScore


def getACard(cardList, cardValueList):
    selectedLogo = random.choice(list(clubArt.keys()))
    selectedCard = random.choice(clubArt[selectedLogo])
    logo, cardString, cardValue = selectedLogo, selectedCard[0], selectedCard[1]
    cardTotal = (logo, cardString, cardValue)
    cardList.append(cardTotal)
    cardValue = cardTotal[2]
    if cardTotal[1] == ' A':
        if getScore(cardValueList) + cardValue > 21:
            cardValue = 1
            cardValueList.append(cardValue)
        else:
            cardValueList.append(cardTotal[2])
    else:
        cardValueList.append(cardTotal[2])


def obscureDealerCards(dealerCards):
    displayedCards = []
    if len(dealerCards) == 1:
        newTuple = ("X", " X")
        displayedCards.append(newTuple)
    if len(dealerCards) > 1:
        for i in range(len(dealerCards)):
            if i == 0:
                newTuple = ("X", " X")
                displayedCards.append(newTuple)
            if i > 0:
                newTuple = (dealerCards[i][0], dealerCards[i][1])
                displayedCards.append(newTuple)
    return displayedCards


def dealersTurn(dealerCards, dealerCardsValues):
    dealerScore = getScore(dealerCardsValues)
    while dealerScore < 17:
        getACard(dealerCards, dealerCardsValues)
        dealerScore = getScore(dealerCardsValues)


def checkIfBash(aScore):
    if aScore == 21:
        return True
    elif aScore > 21:
        return False
    else:
        return None


def compareScores(aScore, anotherScore):
    if aScore > anotherScore:
        return True
    elif aScore < anotherScore:
        return False
    else:
        return "DRAW"

# GAME VISUAL DISPLAY


def cardDisplay(playerCards):
    for ele in playerCards:
        cardArt = """
        ┌────────┐
        │{}      │
        │        │
        │   {}    │
        │        │
        │      {}│
        └────────┘""".format(ele[1], ele[0], ele[1])
        print(cardArt)


def gameVisual(playerCards, playerScore, dealerCards, bank, bet):
    clear()
    # PRINTS GAME LOGO
    print(logo)
    print("----These are your cards----")
    cardDisplay(playerCards)
    print("Your score is {}".format(playerScore))
    print("----These are the dealer's cards----")
    cardDisplay(obscureDealerCards(dealerCards))
    print("----This is your betting table----")
    displayOnGameTable(bank, bet)


def gameVisualFinal(playerCards, playerScore, dealerCards, dealerScore, bank, bet):
    clear()
    # PRINTS GAME LOGO
    print(logo)
    print("----These are your cards----")
    cardDisplay(playerCards)
    print("Your score is {}".format(playerScore))
    print("----These are the dealer's cards----")
    cardDisplay(dealerCards)
    print("The dealer's score is {}".format(dealerScore))
    print("----This is your betting table----")
    displayOnGameTable(bank, bet)


# HERE STARTS THE GAME EXECUTION

while True:
    # DISPLAY THE BETTING ASCII
    displayFirstTable(initialBank)
    playerBet = makeABet(initialBank)
    # PLAYER VARIABLES
    playerCards = []
    playerCardsValues = []
    playerScore = getScore(playerCardsValues)
    # DEALER VARIABLES
    dealerCards = []
    dealerCardsValues = []
    dealerScore = getScore(dealerCardsValues)
    # PLAYER RECIEVES CARD
    getACard(playerCards, playerCardsValues)
    getACard(playerCards, playerCardsValues)
    playerScore = getScore(playerCardsValues)  # PLAYER'S SCORE ACTUALIZED
    # DALER RECIEVES CARD
    getACard(dealerCards, dealerCardsValues)
    getACard(dealerCards, dealerCardsValues)
    dealerScore = getScore(dealerCardsValues)  # DEALER'S SCORE ACTUALIZED
    # FIRST DISPLAY / PLAYER AND DEALER CARDS
    gameVisual(playerCards, playerScore, dealerCards, initialBank, playerBet)
    # CHECK IF THE PLAYER GOT A BLACKJACK
    if playerScore == 21:
        print("BLACKJACK")
        print("YOU WIN")
        break
    # SECOND LOOP AFTER THE FIRST CARDS REPARTITION
    while True:
        # HIT, DOUBLE OR STAND
        playerDecision = input("Please enter HIT, DOUBLE or STAND\n").upper()
        if playerDecision == "HIT":
            # PLAYER RECIEVES ANOTHER CARD
            getACard(playerCards, playerCardsValues)
            # PLAYER'S SCORE ACTUALIZED
            playerScore = getScore(playerCardsValues)
            # GAME VISUAL DISPLAY ACTUALIZED
            gameVisual(playerCards, playerScore,
                       dealerCards, initialBank, playerBet)
            # CHECK IF BASH
            if checkIfBash(playerScore) == True:
                # LAST CHANCE FOR THE DEALER TO PUSH
                # DEALER RECIEVES CARDS
                dealersTurn(dealerCards, dealerCardsValues)
                # DEALER'S SCORE ACTUALIZED'
                dealerScore = getScore(dealerCardsValues)
                # GAME VISUAL DISPLAY FINAL
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                if checkIfBash(dealerScore) == True:
                    print("The dealer and you got a BLACKJACK")
                    print("PUSH")
                    break
                elif checkIfBash(dealerScore) == False:
                    print("BLACKJACK!")
                    print("YOU WIN")
                    betResolution(initialBank, playerBet, True)
                    break
            elif checkIfBash(playerScore) == False:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("BASH")
                print("YOU LOSE")
                betResolution(initialBank, playerBet, False)
                break
        elif playerDecision == "DOUBLE":
            # PLAYER RECIEVES A CARD
            getACard(playerCards, playerCardsValues)
            # PLAYER'S SCORE ACTUALIZED
            playerScore = getScore(playerCardsValues)
            # GAME VISUAL DISPLAY ACTUALIZED
            gameVisual(playerCards, playerScore,
                       dealerCards, initialBank, playerBet)
            if checkIfBash(playerScore) == True:
                # LAST CHANCE FOR THE DEALER TO PUSH
                # DEALER RECIEVES CARDS
                dealersTurn(dealerCards, dealerCardsValues)
                # DEALER'S SCORE ACTUALIZED'
                dealerScore = getScore(dealerCardsValues)
                # GAME VISUAL DISPLAY FINAL
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                if checkIfBash(dealerScore) == True:
                    print("Dealer and player got a BLACKJACK")
                    print("PUSH")
                    break
                elif checkIfBash(dealerScore) == False:
                    print("BLACKJACK!")
                    print("YOU WIN")
                    betResolution(initialBank, (playerBet*2), True)
                    break
            elif checkIfBash(playerScore) == False:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("BASH")
                print("YOU LOSE")
                betResolution(initialBank, (playerBet*2), False)
                break
            # DEALER'S TURN
            dealersTurn(dealerCards, dealerCardsValues)
            # DEALER'S SCORE ACTUALIZED'
            dealerScore = getScore(dealerCardsValues)
            # CHECK IF THE DEALER GOT BASH
            if checkIfBash(dealerScore) == True:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("DEALER GOT A BLACKJACK")
                print("YOU LOSE")
                betResolution(initialBank, (playerBet*2), False)
                break
            elif checkIfBash(dealerScore) == False:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("THE DEALER GOT BASH")
                print("YOU WIN")
                betResolution(initialBank, (playerBet*2), True)
                break
            # SHOW THE CARDS ACTUALIZED
            gameVisualFinal(playerCards, playerScore, dealerCards,
                            dealerScore, initialBank, playerBet)
            # COMPARE SCORES
            if compareScores(playerScore, dealerScore) == True:
                print("YOU WIN")
                betResolution(initialBank, (playerBet*2), True)
                break
            elif compareScores(playerScore, dealerScore) == False:
                print("YOU LOSE")
                betResolution(initialBank, (playerBet*2), False)
                break
            elif compareScores(playerScore, dealerScore) == "DRAW":
                print("PUSH")
                break
        elif playerDecision == "STAND":
            # DEALER'S TURN
            dealersTurn(dealerCards, dealerCardsValues)
            # DEALER'S SCORE ACTUALIZED'
            dealerScore = getScore(dealerCardsValues)
            # CHECK IF THE DEALER GOT BASH
            if checkIfBash(dealerScore) == True:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("DEALER GOT A BLACKJACK")
                print("YOU LOSE")
                betResolution(initialBank, playerBet, False)
                break
            elif checkIfBash(dealerScore) == False:
                gameVisualFinal(playerCards, playerScore,
                                dealerCards, dealerScore, initialBank, playerBet)
                print("THE DEALER GOT BASH")
                print("YOU WIN")
                betResolution(initialBank, playerBet, True)
                break
            # GAME VISUAL DISPLAY FINAL
            gameVisualFinal(playerCards, playerScore, dealerCards,
                            dealerScore, initialBank, playerBet)
            # COMPARE SCORES
            if compareScores(playerScore, dealerScore) == True:
                print("YOU WIN")
                betResolution(initialBank, playerBet, True)
                break
            elif compareScores(playerScore, dealerScore) == False:
                print("YOU LOSE")
                betResolution(initialBank, playerBet, False)
                break
            elif compareScores(playerScore, dealerScore) == "DRAW":
                print("PUSH")
                break
    if actualizeMoney(initialBank) == 0:
        print("Your bank is empty, you LOST")
        break
    print("After the game your bank is ${}".format(actualizeMoney(initialBank)))
    gameDecision = input(
        "Would you like to play again? 'Y' to play again, 'N' to close the game\n").upper()
    if gameDecision == 'Y':
        clear()
        continue
    elif gameDecision == 'N':
        clear()
        break
