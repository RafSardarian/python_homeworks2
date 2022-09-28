from fractions import Fraction as frac

while True:
    
    try:
        x = int(input('Please enter a first number '))
        
        if x == 00: #to close the program
            print("BYE")
            break
        
        y = int(input('PLease enter a second number '))
   
        print(frac(abs(x - y) / (x + y)).limit_denominator(1000))
   
    except ValueError:
        print('Wrong input: number is needed')
    

