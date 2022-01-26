list1=['apple','orange']
longest = 0
for words in list1:
    if len(words) > longest:
        longest = len(words)
        longest_word = words
print("The longest word is", longest_word, "with length", len(longest_word))
