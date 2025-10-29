def lucas(n):                     # im defining the function lucas 
    if n == 0:                    # this is the base one
        return 2                  # im returning the first term
    elif n == 1:                  # this is base 2 
        return 1                  # im returning the second turn
    else:                         # recursive case
        return lucas(n-1) + lucas(n-2)   # im adding the 2 previous numbers

# print the first 10 Lucas numbers
for i in range(10):               # looping 0–9
    print(lucas(i))               # printing each term of the function