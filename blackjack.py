#Blackjack Project

import random
from os import system

#Returns random card from the deck
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#calculate score on hand
def calculate_score(cards):
    #return 0 when player got blackjack at the first time with 2 cards.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #choice of 11 or 1 for Ace
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#compare score between player and computer
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return  "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    #adding cards on hand
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" computer's first card: {computer_cards[0]}")

        #play game again? 
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'h' to get another card, type 's' to pass: ")
            if user_should_deal == 'h':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    #computer turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_cards}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_cards}")
    print(compare(user_score, computer_score))

#restarting game?
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  system("cls")
  play_game()