def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence
def vowel_check(word_string):
    vowels_list = ["a","e","i","o","u"]
    present_vowels = []
    missing_vowels = []
    sentence_list = split_sentence(word_string)
    for word in sentence_list:
        for letter in word:
            if letter in vowels_list and letter not in present_vowels:
                present_vowels.append(letter)
    for vowel in vowels_list:
        if vowel not in present_vowels:
            missing_vowels.append(vowel)
    return missing_vowels
def reverse_sentence(word_string):
    sentence_list = split_sentence(word_string)
    reverse_list = []
    count = -1
    for i in range(len(sentence_list)):
        reverse_list.append(sentence_list[count])
        count -= 1
    return reverse_list

word_string = input("Enter a string of words: ").lower()
print(split_sentence(word_string))
missing_vowels = vowel_check(word_string)
if missing_vowels == []:
    print("There are no missing vowels.")
else:
    print(f"There are {len(missing_vowels)} missing vowels, and they are {missing_vowels}")
print(reverse_sentence(word_string))