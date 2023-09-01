print("This is a login page.")

action = input('Do you want to login? (y/n): ')

if action == 'y':
    while True:
        success = False
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open("accounts.txt", 'r') as f:
            for line in f:
                if line == f'username: {username}, password: {password}\n':
                    print(f"You successfully logged in as {username}.")
                    success = True
                    break
                else:
                    print(f"Invalid username or password. Please try again.")
            if success:
                break
elif action == 'n':
    while True: 
        created = False
        username = input('Enter username: ')
        password = input('Enter password: ')
        confirm = input('Confirm password: ')
        userId = '1'

        with open("accounts.txt", 'r') as f:
                for line in f:
                    existingUsers = line.split(', ')[0]
                    prevUserId = line.split('. userId: ')[1]
                    userId = str(int(prevUserId.split(';\n')[0]) +1)
                    if existingUsers == f"username: {username}":
                        created = True
        if created:
            confirm = password +'1'
            print('An account with that username already exists. Please use a different username.')
        if password == confirm:
            with open("accounts.txt", 'a') as f:
                f.write(f"username: {username}, password: {password}. userId: {userId};\n")
            print('Account successfully created.')
            break
        else:
            if not created:
                print("Your Password and Confirmation do not match. Please try again.")
        