number = 5
while True:
    user_input = input("Enter a number: ")
    user_number = int(user_input)
    if user_number == number:
        print('congrats you guessed the number!!!')
        break 
    elif user_number>number:
        print('too hing')
    elif user_number<number:
        print('too low')