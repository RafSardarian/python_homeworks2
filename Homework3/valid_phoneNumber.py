while True:
    number = input('Enter a phone number ')
           
    
    check_number = number.replace('-','')
    

    if not check_number.isdigit():
        print('Invalid')

    elif number == '0': #to close the program
        break

        
    else:
        number = number.split('-')
        if number[0] == '1' and len(number[1]) == 3 and len(number[2]) == 3 and len(number[3]) == 4:
            print('Valid')
        elif len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4:
            print('Valid')
        else:
            print('Invalid')
