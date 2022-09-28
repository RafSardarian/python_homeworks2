while True:
    try:
        num = int(input('How many kiloes? '))
        if num == 0: #to close the program
            print("BYE")
            break
        if num < 0:
            print('Wrong input: Positive number is needed')
        else:
            print(num * 2.20462)
    except ValueError:
        print('Wrong input: Number is needed')
