import random


def rock_paper_scissor():
    ROCK = """
               __ __ __ __ 
            __|  |  |  |  |  
           |  |  |  |  |  |  
            --|  |  |  |  |  
               -- -- -- --
        """

    PAPER = """
               __ __ __ __ 
              |  |  |  |  |  
              |  |  |  |  |  
              |  |  |  |  |
            __|           |
           |  |           |
           |  |           |
           |  |           |
           ----------------

            """

    SCISSOR = """
          __       __
          \ \     / / 
           \ \   / /
            \ \ / /
             \   /  __ __
             |----| | | |
             |_____)| | | 
             |          |
             |          |    
              ------------
        """

    ROCK_PAPER_SCISSOR = ["rock", "paper", "scissor"]

    def game_intro():
        print("Welcome to Rock, Paper, Scissor. Press 'q' to quit")

    def play_game():
        your_choice = input("Choose rock, paper, or scissor \n").strip().lower()

        if your_choice == "q":
            quit()

        computer_choice = ROCK_PAPER_SCISSOR[int(random.randrange(0, 2))]

        your_pick_sentence = "You chose " + your_choice
        computer_pick_sentence = "The computer chose " + computer_choice
        print(your_pick_sentence)

        if your_choice == "rock" or your_choice == "paper" or your_choice == "scissor":
            if your_choice == "rock":
                print(ROCK)
            elif your_choice == "paper":
                print(PAPER)
            else:
                print(SCISSOR)

            print(computer_pick_sentence)

            if computer_choice == "rock":
                print(ROCK)
            elif computer_choice == "paper":
                print(PAPER)
            else:
                print(SCISSOR)

            if your_choice == "rock" and computer_choice == "rock":
                print("Game is a tie")
            elif your_choice == "rock" and computer_choice == "paper":
                print("You lost")
            elif your_choice == "rock" and computer_choice == "scissor":
                print("You won")
            elif your_choice == "paper" and computer_choice == "rock":
                print("You won")
            elif your_choice == "paper" and computer_choice == "paper":
                print("Game is a tie")
            elif your_choice == "paper" and computer_choice == "scissor":
                print("You lost")
            elif your_choice == "scissor" and computer_choice == "rock":
                print("You lost")
            elif your_choice == "scissor" and computer_choice == "paper":
                print("You won")
            elif your_choice == "scissor" and computer_choice == "scissor":
                print("Game is a tie")

        else:
            wrong_input()

    def wrong_input():
        print("You did not pick rock, paper, or scissor,\nChoose one of the following: rock, paper, or scissor"
              "\nOr press q to exit")
        answer = input().strip().lower()
        if answer == "q":
            exit()
        else:
            wrong_input()

    def play_again():
        play_game()
        end_game()

    def end_game():
        answer = input("Would you like to play again?\n").strip().lower()
        if answer == "yes":
            play_again()
            main()
        elif answer == "no":
            main()
        else:
            print("Answer not understood")
            end_game()

    def rock_paper_scissor_game():
        game_intro()
        play_game()
        end_game()

    rock_paper_scissor_game()


def black_jack():
    CARDS = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
             "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 11, "King": 11}
    cards_list = CARDS.values()

    YOUR_CARDS = []
    YOUR_HAND = []

    COMPUTER_CARDS = []
    COMPUTER_HAND = []

    def game_intro():
        print("Welcome to Blackjack")

    def hit():
        x = 1
        score = 0
        dealt_card = random.choice(list(cards_list))
        YOUR_HAND = YOUR_CARDS.append(dealt_card)
        COMPUTER_HAND = COMPUTER_CARDS.append(dealt_card)
        print("Your hand: ", YOUR_CARDS)
        for card in range(0, len(YOUR_CARDS)):
            score = score + YOUR_CARDS[card]
            print("Your score is now: ", score)
            x = x + 1
            if score > 21:
                print("You busted")
                main()
        answer()

    def play_game():
        hit()

    def hit_continue():
        hit()

    def computer_turn():
        x = 1
        score = 0
        dealt_card = random.choice(list(cards_list))
        COMPUTER_HAND = COMPUTER_CARDS.append(dealt_card)
        print("The house is hand: ", COMPUTER_CARDS)
        for card in range(0, len(COMPUTER_CARDS)):
            score = score + COMPUTER_CARDS[card]
            print("The House score is now: ", score)
            x = x + 1
            if score > 22:
                print("The House busted, you win")
                main()
        computer_turn()

    def answer():
        answer = input("Would you like to hit or stay?\n").strip().lower()
        if answer == "yes" or answer == "hit":
            hit_continue()
        else:
            print("Computer's turn")
            computer_turn()

    def blackjack():
        game_intro()
        play_game()
        computer_turn()

    blackjack()


def main():
    answer = input("Do you want to play blackjack (1) or rock, paper, scissor (2). \nPress 'q' to quit \n").strip().lower()
    if answer == "1" or answer == "blackjack":
        black_jack()
    elif answer == "2" or answer == "rock, paper, scissor":
        rock_paper_scissor()
    elif answer == "q":
        exit()
    else:
        second_answer = input("Input not understood, choose 1 or 2, or press q to quit\n")
        if second_answer == "q":
            exit()
        else:
            main()


main()
