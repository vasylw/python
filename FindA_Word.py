text = input("Please input a word and space separated letters pool to check if \
the word characters are in pool:  ")

words = text.split()

print(words)

n_words = len(words)

if n_words == 0 or n_words > 2:
    print ("Game Over!!!")
    exit()
word = ''
for char in words[0]:
    if words[1].find(char) > -1:
        word += char


if word == words[0]:
    print("Yes, there is!!!")
else:
    print("No, there isn't!")