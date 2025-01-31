def vowel_upper_list(data):
    vowels = 'AEIOUaeiou'
    vowel_list = (word for word in data if word[0] in vowels)
    upper_list = list(map(lambda word: word.upper(), vowel_list))

    return upper_list


user_input = input("Введите список слов, разделенных запятой и пробелом: ").split(", ")

print(vowel_upper_list(user_input))