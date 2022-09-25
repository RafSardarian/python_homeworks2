#Program checks if the input number is even or odd
while True:
    integer = int(input('Please write a number '))
    if integer == -1: #if you need to close the program
        break
    integer = 'Even' if integer % 2 == 0 else 'Odd'
    print(integer)
