DF = 'YYYYMMDD'

input_string = input("Please input a date like YYYYMMDD to to find digit of life: ")

if input_string == "":
    input_string = input("Can You input some date like YYYYMMDD to to find a digit?: ")


date=''
for char in input_string:
    if char != ' ':
        date += char

#print(date)

MSG = "You loose this Game!!! ^_^"

if date == "" :
    print(MSG)
    exit()
elif date.isalnum() == False:
    print(MSG)
    exit()
elif len(date) > len(DF):
    print(MSG)
    exit()
else:
    date_numbers = list(date)

#print(date_numbers)


while len(date_numbers) > 1:

    date_digit = 0

    for char in date_numbers:
        date_digit = date_digit + int(char)

    date_numbers = list(str(date_digit))
    #print(date_numbers)
    #print(len(date_numbers))



print("Digit of the life is: ", date_digit)

#print(str(list(date))[-1])



