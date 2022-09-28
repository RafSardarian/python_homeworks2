
while True:
    try:
        year = int(input('Enter the year '))
        if year == 0: #to close the program 
            break
        if year < 1600:
            print('Wrong input: Please enter higher than 1600')
            continue
        year -= 1600 #how many years beetween 1600 and the input year 
   
        x = year // 4 #how many years divisible by 4 
        y = year // 100 #how many years divisible by 100
        z = year // 400 # how many years divisible by 400


        print(x - (y - z) + 1) # +1 is the year 1600 which is also leap year

    except ValueError:
        print('Wrong input: number is needed')
