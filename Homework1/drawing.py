lst = [4,2,2,2,4]
for i in range(len(lst)):
    if i == 0 or i == len(lst) - 1:
        print('*' * lst[i])
        continue
    print('*  ' * lst[i])
