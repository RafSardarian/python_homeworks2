while True:
    try:
        number = int(input('Write a number '))
        if number == 0: #to close the program
            break
        
        else:
            result = 0
            while number > 0:
                current = number % 10
                number = number // 10
                result += current
            print(result)
    except ValueError:
            print('Wrong input: number is needed')
    
