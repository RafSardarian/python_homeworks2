dic = {}
while True:
    try:
        key = input('Enter a product ')
        if key == 'done' or key == 'Done':
            print('All data is successfully stored')
            break
        
        value = int(input('Enter a price '))
        value = str(value)     
        dic.update({key:'$' + value})
    
    except ValueError:
        print('Wrong input: price must be digit')




while True:
    print('Type the product name to see the price')
    prod = input()

    if prod == '0': #to close the program
        break

    elif prod == 'all': #to see all the data
        print(dic)

    elif prod in dic:
        print(dic[prod])
  
    else:
        print('Not found: No such product')

