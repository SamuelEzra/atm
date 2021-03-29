from datetime import datetime

currentTime = datetime.now()
timeFormat = currentTime.strftime('%d-%m-%Y   %H:%M:%S')

allowedUsers = ['Ezra', 'Samuel', 'Daniel', 'Seyi', 'Abas']
allowedPasswords = ['PasswordEz', 'PasswordSa', 'PasswordDa', 'PasswordSe', 'PasswordAb']

name = input('What is your name? \n')

if (name in allowedUsers):
    userId = allowedUsers.index(name)
    password = input('Please enter your password: \n')

    if (password == allowedPasswords[userId]):
        print('\n')
        print(timeFormat)
        print('Welcome %s' %name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please enter an option: \n'))
        
        if (selectedOption == 1):
            cash = int(input('How much would you like to withdraw? \n'))
            print('Take your cash')
        
        elif (selectedOption == 2):
            cash = int(input('How much would you like to deposit? \n'))
            print('Your current balance is #%d' %cash)

        elif (selectedOption == 3):
            issue = input('What issue will you like to report? \n')
            print('Thank you for contacting us')

        else:
            print('Invalid option selected! Please try again.')

    else:
        print('Incorrect password! Please try again.')
else:
    print('Name not found! Please try again.')
