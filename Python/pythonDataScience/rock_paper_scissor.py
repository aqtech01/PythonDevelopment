from random import randint

play_options = ["rock", "paper", "scissors"]

while True:
    computer_play = play_options[randint(0, 2)]
    user_play = input("Rock , paper, Scissors? : ").lower()
    if computer_play == user_play:
        print("It's a tie")
    elif user_play == "rock":
        if computer_play == "paper":
            # code
            print("You Lose", computer_play, "beats", user_play)
        else:
            # code
            print("You Win", user_play, "beats", computer_play)
    elif user_play == "scissors":
        if computer_play == "paper":
            # code
            print("You Win", user_play, "beats", computer_play)
        else:
            # code
            print("You Lose", computer_play, "beats", user_play)
    elif user_play == "paper":
        if computer_play == "scissors":
            # code
            print("You Win", user_play, "beats", computer_play)
        else:
            # code
            print("You Lose", computer_play, "beats", user_play)

    else:
        print("Not Valid Option")
        continue



