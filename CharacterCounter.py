from os import strerror

fname = str(input("Please input text filename for letters counting: "))
out_dict = dict()
letters_A = [x for x in range(65,91)]
letters_a = [x for x in range(97,123)]
#print(letters_A)
#print(letters_B)

try:
    fstream = open(fname, 'rt')
    ch = fstream.read(1)
    while ch != '':
        if ch in out_dict.keys():
            out_dict[ch] += 1
        elif ord(ch) in letters_A or ord(ch) in letters_a :
            out_dict[ch] = 1
        ch = fstream.read(1)
    fstream.close()

    for key in out_dict.keys():
        print(key, " --> ", out_dict[key])

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))