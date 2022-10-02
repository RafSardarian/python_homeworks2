while True:
    number = input('Please enter the numbers separated by ",": ')
            
    if number == '0': #to close the program
        break

    elif number.isalpha():
        print('Wrong input: number is needed')
        continue


    else:
        number = number.split(',')
        if len(number) != 5:
            print('Wrong input: Needed five numbers separated by ","')
   
        else:
            print('+'.join(number))
