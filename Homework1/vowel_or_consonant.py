#A program which cheks if character is vowel or consonant
while True:
    let = ['a','e','i','o','u']
    char = input('Please write a character ')
    if char == ' ' or char == '':
        continue

    elif char == '0': #to close the program
        break

    elif char.isnumeric():
        print('Wrong input: character is needed')

    elif len(char) > 1:
        print('Wrong input: one character is needed')

    else:
        if char in let:
            print('Vowel')
        else:
            print('Consonant')


    


