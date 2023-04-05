def read_int(prompt, min, max):
    input_str = input(prompt)
    try:
        input_number = int(input_str)
        assert input_number >= min and input_number <= max
        return input_number

    except AssertionError:
        print("Error: the value is not within permitted range")

    except ValueError:
        print("Error: wrong input!")
        read_int(prompt, min, max)

    except:
        print("Something go wrong... ")
    #
    # Write your code here.
    #


v = read_int("Enter a number from -10 to 10: ", -10, 10)

if v: print("The number is:", v)