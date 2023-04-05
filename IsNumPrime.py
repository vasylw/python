def is_prime(num):
    prime = True
    check_list = [ 2, 3, 4, 5, 6, 7, 8, 9]

    for n in check_list:
        if num != n:
            if num%n == 0:
                prime = False
        else: break

    return prime

    #print(str(prime))


for i in range(1, 200):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

