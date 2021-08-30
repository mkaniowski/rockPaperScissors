import random

# 0 - wins with 2; loses with 1
# 1 - wins with 0; loses with 2
# 2 - wins with 1; loses with 0

choices = ("ROCK", "PAPER", "SCISSORS")


def main():
    try:  # Checks if input is int
        round_number = int(input("How many rounds: "))
        if round_number % 2 == 1:  # checks for B01, B03 etc.
            epsGame(round_number)
        else:
            print("Number of rounds has to be odd")
            main()
    except ValueError:
        print("Wrong input! Please type in a number.")
        main()
    exit()


def epsGame(round_number) -> None:
    round_number_const = round_number  # round_number_const is used for logic
    no_round = 1  # first number of round to display
    player_score = 0
    ai_score = 0
    random.seed()
    while round_number != 0:
        if abs(player_score - ai_score) < (round_number_const / 2):  # in B03 with 2-0 it's pointless to play 3rd round
            if (player_score or ai_score) != round_number_const:  # stops if someone gets eg. 3 points in B03
                player_input = input("Rock, paper, scissors: ").upper()
                if player_input in choices:
                    ai_input = random.choice(choices)
                    print(f"\n \n-=Round {abs(no_round)}=-")
                    print(f"{player_input} vs {ai_input}")
                    if ai_input == player_input:
                        print("DRAW!")
                    elif player_input == choices[1] and ai_input == choices[0]:
                        player_score += 1
                        print("You win this round!")
                        round_number -= 1
                    elif player_input == choices[0] and ai_input == choices[2]:
                        player_score += 1
                        print("You win this round!")
                        round_number -= 1
                    elif player_input == choices[2] and ai_input == choices[1]:
                        player_score += 1
                        print("You win this round!")
                        round_number -= 1
                    else:  # I just need to check whether player has won
                        ai_score += 1
                        print("Ai wins this round")
                        round_number -= 1
                    no_round = round_number - round_number_const - 1  # since I count count rounds from high to low
                    print(
                        f"Player-{player_score} : Ai-{ai_score} \n \n")  # I need something to display current round no.
                else:
                    print("Please choose from 'Rock', 'Paper' or 'Scissors'")
            else:
                round_number = 0  # Exits the loop and statements
        else:
            round_number = 0  # Exits the loop and statements
    end(player_score, ai_score)
    return


def end(player_score, ai_score):
    if player_score > ai_score:
        print(f"You have won the game with score: Player-{player_score} : Ai-{ai_score}")
    else:
        print(f"You have lost the game with score: Player-{player_score} : Ai-{ai_score}")
    return


main()
