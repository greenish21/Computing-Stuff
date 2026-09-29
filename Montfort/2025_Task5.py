def textChanger1(word):
    word_list = list(word)
    word_list.reverse()
    word_str = ""
    for char in word_list:
        word_str = word_str + char
    return word_str
def textChanger2(word):
    word_list = list(word)
    odd_str = ""
    even_str = ""
    odd_count = 0
    even_count = 1
    for char in word_list:
        if odd_count < len(word_list) and char == word_list[odd_count]:
            odd_str = odd_str + char
            odd_count += 2
        elif even_count < len(word_list) and char == word_list[even_count]:
            even_str = even_str + char
            even_count += 2
    final_str = odd_str + even_str
    return final_str
def textChanger3(word):
    if len(word) <= 4:
        return word
    else:
        last_two = word[-2:]
        final_str = last_two + word
        return final_str
word = input("Enter a word to scramble: ")
text_changers = [textChanger1, textChanger2, textChanger3]
count = 0
while count < len(text_changers):
    result = text_changers[count](word)
    print(f"Scrambled word {count+1} is", result)
    count += 1
