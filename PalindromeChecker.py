# Palindrome checker

input_text = input("Please input a text to check if it is palindrome: ")
if input_text == "":
    input_text = input("Input some text to check if it is palindrome: ")
    if input_text == "":
        print("You loose a Game!!! ^_^")
        exit()

text2=''
for char in input_text:
    if char != ' ':
        text2 += char

text=''
i = len(text2)

while i >= 1:
    text += text2[i-1]
    i -= 1
print(text)


ispalindrome = True

for index in range(len(text)):
    if text[index] != text2[index]:
        ispalindrome = False

if ispalindrome: print("Yes, it's palindrome :-)")
else: print("No, it's not palindrome...")