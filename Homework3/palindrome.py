res = []
for i in range(100,1000):
    i = str(i)
    if i[:] == i[::-1]:
        res.append(i)




print(res)
