incorrect_counter = 0
input1 = int(input("Player 1, Enter a number between 1-50 inclusive: "))
if input1 >= 1 and input1 <= 50:
    difficulty = input("Player 2, Select your difficulty (Easy, Medium, Hard): ")
    if difficulty == "Easy":
        count = 8
    elif difficulty == "Medium":
        count = 6
    elif difficulty == "Hard":
        count = 4

    for i in range(count):
        input2 = int(input("Player 2, Guess the number given by player 1: "))
        if input2 == input1:
            print("You guessed the correct number.")
            break
        else:
            print("You did not guess the correct number.")
            if input1 > input2:
                print("Your guess is lower than the answer")
            else:
                print("Your guess is higher than the answer")
            incorrect_counter += 1
    else:
        print("Game over")
print(f"You have made {incorrect_counter+1} guess(es)")