

counting_words = {}
user_text = input("Text: ")
user_words = user_text.split() #split words into list

for word in user_words: #iterate through each variable in list
    occurrence = counting_words.get(word, 0) #check if word is already stored
    counting_words[word] = occurrence + 1 #add 1 to its value of occurrence



longest_word = max(len(word) for word in user_words) #check for longest word in list

for word, occurrence in counting_words.items():
    print("{:{}} is {}".format(word, longest_word, occurrence))#print respective words in list with alignment





