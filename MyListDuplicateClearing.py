my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list_copy = my_list
duplicate = True
#

while duplicate:

    for i in my_list:
      duplicate = True
      if  my_list_copy[i] != my_list[i]:
            my_list_copy.append(my_list[i])
            duplicate = True
      else: duplicate = False


    # x=1
    #for j in my_list:
        #print(j)
        #if my_list[i] != my_list[j] : new_list.append(my_list[i])

print("list without duplicate number", my_list)
