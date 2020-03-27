

counting_words = {}
user_text = input("Text: ")
user_words = user_text.split()

for word in user_words:
    occurrence = counting_words.get(word, 0)
    counting_words[word] = occurrence + 1



longest_word = max(len(word) for word in user_words)

for word, occurrence in counting_words.items():
    print("{:{}} is {}".format(word, longest_word, occurrence))





