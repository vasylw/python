# Check if entered words are annagramd

text = input("Please input space separated words to check if tey are annagrams: ")
words = text.split()

n_words = len(words)

annagrams = True

for w in range(n_words-1):
    word = words[0]
    if len(words[0]) != len(words[w+1]):
        annagrams = False
        break
    else:
        for i in range(len(words[0])):
            word_length = len(words[w+1])

            for j in range(word_length):

                if words[w+1][j] == words[0][i]:
                    word = word.replace(words[w+1][j], '', 1)

        if len(word) == 0:
            annagrams = True
        else:
            #print(word, '  ', words[0], '  ', words[w+1])
            annagrams = False
#print(word)
if annagrams:
    print("Words are annagrams")
else:
    print("Words are not annagrams")