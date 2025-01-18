def find_longest_word(data: list[str]) -> str:
    new_list = list(map(lambda word: word, data))
    return max(new_list)

words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)

print(result)