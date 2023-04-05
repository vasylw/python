# Caesar cipher.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = ALPHABET.lower()
print(alphabet)
#
#alphabet_lehgth = len(alphabet)

def alphabet_index(char='A'):
    char = char.upper()
    if char in ALPHABET:
        return int(abs(ALPHABET.find(char)))
    else: return 0

#def tebahpla_index(char='Z'):
#   char = char.upper()
#    if char in tebahpla:
#        return int(abs(alphabet.find(char)))
#    else: return 26


text = input("Enter your message: ")
shift = input('Enter a shift value from 1 to 25: ')
try: shift=int(shift)
except:
    shift = input("Enter a valid numeric shift value from 1 to 25: ")
    try: shift=int(shift)
    except:
        print ("You loose this Game ^_^  !!!")
        for i in shift:
            print("_____ --- - ______ ____  &^&&*7 *&&% 9")
        exit()


cipher = ''
for char in text:

    if not char.isalpha():
        cipher += char
        continue

    if char.islower():
        if alphabet_index(char) + shift > alphabet_index('z'):
            char_nindex =  shift - (alphabet_index('z') - alphabet_index(char))\
             + 1
            cipher = cipher + alphabet[char_nindex -1]
        else:
            cipher = cipher + alphabet[shift+alphabet_index(char) -1]

    if char.isupper():
        if alphabet_index(char) + shift > alphabet_index('Z'):
            char_nindex =  shift - (alphabet_index('Z') - alphabet_index(char))\
             + 1
            cipher = cipher + alphabet[char_nindex -1]
        else:
            cipher = cipher + alphabet[shift+alphabet_index(char) -1]


print(cipher)

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')

text = ''
for char in cipher:
    if not char.isalpha():
        text += char
        continue

    if char.islower():
        if alphabet_index(char) - shift < alphabet_index('a'):
            char_nindex =  (alphabet_index('z') - abs(alphabet_index(char) - shift))\
             - 1

            text = text + alphabet[char_nindex - 1]
        else:
            text = text + alphabet[alphabet_index(char) - shift - 1]

    if char.isupper():
        if alphabet_index(char) - shift < alphabet_index('A'):
            char_nindex =  (alphabet_index('Z') - abs(alphabet_index(char) - shift))\
             - 1
            text = text + alphabet[char_nindex -1]
        else:
            text = text + alphabet[alphabet_index(char) - shift -1]

print(text)
