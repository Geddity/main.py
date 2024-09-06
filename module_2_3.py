my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i in range(0, len(my_list)):
    k = my_list[i]
    if k > 0:
        i += 1
        print(k)
    elif k == 0:
        i += 1
    else:
        break