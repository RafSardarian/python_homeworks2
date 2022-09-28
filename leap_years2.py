while True:
    years = []
    try:
        year = int(input('Enter the year '))
        if year == 0:
            break
        if year < 1600:
            print('Wrong input: PLease enter higher than 1600')
            continue
        start = 1600
        for i in range(1600,year + 1,4):
            if i % 400 == 0 or i % 100 != 0:
                years.append(i)
            
        print(len(years))
        #print(years)
    
    except ValueError:
        print('Wrong input: number is needed')
