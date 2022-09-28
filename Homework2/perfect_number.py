import math
def find_divisors(number):
    x = math.ceil(math.sqrt(number))
    divisors = []
    while x > 0:
        if number % x == 0:
            divisors.append(int(x))
            divisors.append(int(number // x))
        x -= 1
    divisors.pop(-1)
    return set(divisors)

def perfect_number(num):
    if num == sum(find_divisors(num)):
        return True
    else:
        return False

for i in range(6,10000,2):
    if perfect_number(i):
        print(i)



#print(find_divisors(6))
#print(find_divisors(28))
#print(find_divisors(15))
#print(find_divisors(16))
#print(find_divisors(36))
#print(perfect_number(6))
#print(perfect_number(28))
#print(perfect_number(15))
