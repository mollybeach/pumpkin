#how to build basic python program thats getting user input and if statement 
print('create account now')

username = input('Create new username :')
password = input('Create new password : ')
print('Your account has been created successfully please enter your credentials again to login ')
print('Login now here: \n')

username2 = input('Enter username : ')
password2 = input('Enter password : ')

if username == username2 and password == password2:
    print('Logged in successfully')
else: 
    print('Login failed')