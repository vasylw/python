# "LED" table
led_list = [[['#','#','#'], [' ',' ','#'], ['#','#','#'],['#','#','#'],['#',' ','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#']],\
            [['#',' ','#'], [' ','#','#'], [' ',' ','#'],[' ',' ','#'],['#',' ','#'],['#',' ',' '],['#',' ',' '],[' ',' ','#'],['#',' ','#'],['#',' ','#']],\
            [['#',' ','#'], ['#',' ','#'], ['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#']],\
            [['#',' ','#'], [' ',' ','#'], ['#',' ',' '],[' ',' ','#'],[' ',' ','#'],[' ',' ','#'],['#',' ','#'],[' ',' ','#'],['#',' ','#'],[' ',' ','#']],\
            [['#','#','#'], [' ',' ','#'], ['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#']],\
            [['_','_','_'], ['_','_','_'], ['_','_','_'], ['_','_','_'],['_','_','_'], ['_','_','_'], ['_','_','_'], ['_','_','_'],['_','_','_'], ['_','_','_']]\
            ]
rows = len(led_list)
pixels_row = len(led_list[0][0])

INPUT1 = "Please, input any integer number from 0 to 999999999: "
INPUT2 = "WTF man?, can't you enter any number from 0 to 999999999 ?: "

print()

def nums_to_leds(number):
    numbers_list = []
    numbers_list[:] = number
    length = len(numbers_list)

    for k in range(rows):
        print("")
        for n in numbers_list:
            n = int(n)

            for j in range(pixels_row):
                print(led_list[k][n][j], end='')
                if j == (pixels_row-1) : print('  ', end='')


number = input(INPUT1)
if number.isdigit():
    nums_to_leds(number)

else:
   number = input(INPUT2)
   if number.isdigit():
        nums_to_leds(number)
