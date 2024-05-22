words_list = ["Exercises", "Exercise9", "kanal", "pp", "Exercis"]
index = 0
for i, n in enumerate(words_list):
    if len(n) > len(words_list[index]):
        index = i

print(f"Longest word: {words_list[index]}")
print(f"Length: {len(words_list[index])}")


# oder mit der built-in Funktion max
words_list = ["Exercises", "Exercise988", "kanal", "pp", "Exercis"]
longest_word = max(words_list, key=len)

print(f"Longest word: {longest_word}")
print(f"Length: {len(longest_word)}")
