word = input("Please enter your word: ")
word = word.lower() # 4) Changed to lower
begin_p = word.startswith("p") # 3) Changed to startswith
end_h = word.endswith("h")
contain_e = "e" in word # 5) Changed to find "e"
word_length = len(word) # 7) Changed to len
if not begin_p and not end_h and contain_e == -1: # 1) Changed = to ==
    if word_length <= 3: # 6) Changed to <=
        print("The length of the word is short.")
    elif word_length <= 10: # 8) Changed to word_length
        print("The length of the word is medium.")
    else: # 2) Changed elif to else
        print("The length of the word is long.")
if begin_p:
    print("Invalid. You entered a word that begins with 'p'.")
elif end_h:
    print("Invalid. You entered a word that ends with 'h'.")
elif contain_e: # 9) Removed not
    print("Invalid. You entered a word that contains 'e'.") # 10) Changed a to e