#! Python 3 Sudoku

ROW = 9 # number rows of play table
COL = 9 # number columns of play table
AD_RULE = 3 # subtable dimensions for rule checking
ROW_CHECK = ['1','2','3','4','5','6','7','8','9'] #Sequence to check if rows, columns
            # and subtables are according to Sudoku rules
IS_SUDOKU = True #to set False if the table is none as Sudoku

print("Welcome to SUDOKU game!!! Good luck ^_^ ")


def row_input():
    in_row_list = []
    in_row = input ("Please, enter nine different digits, according to Sudoku rules: ")

    if in_row.isalnum and len(in_row) == ROW:
        in_row_list = list(in_row)
        return in_row_list
    else:
        in_row = input ("Please, enter nine digits, other didn't working: ")
        if in_row.isalnum and len(in_row) == ROW:
            in_row_list = list(in_row)
            return in_row_list
        else:
            print("Your Game is over :( !")
            exit()


table = []

while len(table) < COL:

    in_row_list = row_input()

    if ROW_CHECK == sorted(in_row_list):

        table.append(in_row_list)



for k in range(AD_RULE):

    for m in range(AD_RULE):

        check_list = []

        for i in range(k*AD_RULE, k*AD_RULE + AD_RULE):

            for j in range(m*AD_RULE, m*AD_RULE + AD_RULE):
                check_list.append(table[i][j])

        if  ROW_CHECK != sorted(check_list):
            IS_SUDOKU = False

        print(check_list)


print(table)
if IS_SUDOKU:
    print("Congratulation! It's Sudoku!!")
else:
    print("Sorry! It's not Sudoku!!")