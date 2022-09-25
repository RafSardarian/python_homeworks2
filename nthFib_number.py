def fibonacci(n,a=0,b=1):
    return a if n == 0 else fibonacci(n-1,b,a+b)



print('To close the program please enter "-11"')
while True:
    try:
        number = int(input('Enter a number '))
        if number == -11: #to close the program
            break
        if number < 0:
            print('Wrong input: possitive number is needed')
        else:
            print(f"Fibonacci number is {fibonacci(number)}")
    
    except ValueError:
        print('Wrong input: number is needed')


    
