import random

def select_word(w_list):
    r_num= random.randint(0,len(w_list)-1)
    word = w_list[r_num]
    return word
def check_word(word1, word2):
    if word1 == word2:
        return True
    else:
        return False
def check_letter(word,letter_list):
    return_str = ""
    for letter in word:
        if letter not in letter_list:
            return_str = return_str + "_"
        else:
            return_str = return_str + letter
    return return_str

word_list = ["house","grass","green","block"]
random_word = select_word(word_list)
count = 0
letter_list = []
won = False
for i in range(6):
    choice = str(input("Do you wish to guess the word or letter? ")).lower()
    if choice == "word":
        while True:
            word_input = input("Enter your word: ")
            if len(word_input) == 5 and word_input.isalpha() == True:
                break
        if check_word(random_word,word_input) == True:
            print("You win!")
            print(f"You attempted {count} times")
            won = True
            break
    elif choice == "letter":
        while True:
            letter_input = input("Enter your letter: ")
            if len(letter_input) == 1 and letter_input.isalpha() == True:
                break
        letter_list.append(letter_input)
        print(check_letter(random_word,letter_list))
        count += 1
if won == False:
    print("Game over!")


            

