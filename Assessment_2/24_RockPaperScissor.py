import random

def AIChoice():
    lst = ["rock", "paper", "scissors"]
    return random.choice(lst)

def Winner(user_input, player_score, ai_score):
    AI = AIChoice()

    if user_input == AI:
        print("User Input =", user_input, "| AI =", AI)
        print("It's a tie")
    elif (user_input == "rock" and AI == "scissors") or (user_input == "scissors" and AI == "paper") or (user_input == "paper" and AI == "rock"):
        print("User Input =", user_input, "| AI =", AI)
        print("You won")
        player_score += 1
    else:
        print("User Input =", user_input, "| AI =", AI)
        print("You lose, AI won")
        ai_score += 1
    return player_score, ai_score

player_score = 0
ai_score = 0

while True:
    print("\n   Rock Paper Scissors   \n")
    user_input = input("\n Rock \n"
                       "Paper \n"
                       "Scissors\n"
                       "Enter 1 to exit from the game\n"
                       "\nEnter an option: ").lower()

    if user_input == '1':
        print("Exiting!!")
        break
    elif user_input not in ["rock", "paper", "scissors"]:
        print("Choose a valid option\n")
    else:
        player_score, ai_score = Winner(user_input, player_score, ai_score)
        print("Player Score:", player_score)
        print("AI Score:", ai_score)
