two_words = input("Input two space-seperated words: ")

two_words.split()
two_words_list = two_words.split()

word1 = two_words_list[0]
word2 = two_words_list[1]

word1_sorted = sorted(word1)
word2_sorted = sorted(word2)

if word1_sorted == word2_sorted:
    print("the words are anagrams.")
else:
    print("the words are not anagrams.")