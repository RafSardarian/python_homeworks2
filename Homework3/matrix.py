import random


matrix = [[random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)],
        [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]]

dic = {}
for i in range(0,len(matrix)):
    for j in matrix[i]:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1


#print(matrix)
#print(dic)

print(list(dic.keys())[list(dic.values()).index(max(dic.values()))])
del dic[list(dic.keys())[list(dic.values()).index(max(dic.values()))]]

print(list(dic.keys())[list(dic.values()).index(max(dic.values()))])
del dic[list(dic.keys())[list(dic.values()).index(max(dic.values()))]]

print(list(dic.keys())[list(dic.values()).index(max(dic.values()))])

