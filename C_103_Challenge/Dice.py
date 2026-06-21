
import random # 5) Changed math to random
while True: # 1) Changed true to True
    dice_list = []
    for i in range(2):
        input("Player {}, press enter to roll the three dice".format(i+1))
        dice = [0]*3 # 7) Changed {} to []
        for j in range(3):
            dice[j] = random.randint(1,6) # 6) Changed to (1,6)
        dice_list.append(dice) # 8) Changed eppend to append
        print("Player {}, dice = {}" .format(i+1,dice))
    if max(dice_list[0]) > max(dice_list[1]):
        print("Player 1 wins!")
    elif max(dice_list[0]) == max(dice_list[1]): # 3) Changed = to ==
        print("No winners!")
    else: # 4) Changed elif to else
        print("Player 2 wins!")
        
    play = input("Play again? (Y/N): ").upper() # 9) Changed isupper to upper
    if play == 'N':
        print("Thank you for playing, goodbye!")
        break # 2) Removed extra ':'
