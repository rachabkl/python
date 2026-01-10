import random
while True:
    user_action = input('Enter a choice (rock,paper,scisors)').lower()

    possible_actions = ["rock","paper","scisors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action},computer chose {computer_action}.\n")
    
    if user_action == computer_action:
       print(f"Both players selected{user_action}; It's a tie !")
    elif user_action == "rock":
        if computer_action == "scisors":
            print("Rock smashes scisors! You won")
        else:
            print("Pper covers rock! You lost ")
    
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You won ")
        else:
            print("Scisors cuts paper! You lost ")

    elif user_action == "scisors":
        if computer_action == "paper":
            print("Scisors cuts  paper !You won")
        else:
            print("Rock smashes scisors! You lost ")
    
    else:
        print("Invalid input! Please choose rock, paper , or scisors")

    play_again = input("\n Play again?(y/n): ").lower()
    if play_again != "y":
        print("Thanks for  palying")
        break
    

