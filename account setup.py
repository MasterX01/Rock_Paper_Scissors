print("Account Setup")
while True:
    username = input("Please enter the username:  ")
    password = input("Please enter the password:  ")
    password_confirm = input("Please confirm your password:  ")
    if password != password_confirm:
        print("Passwords don't match. Please try again.")
        
    if password == password_confirm:
        print("Your Account has been setup")
        text_file = open("accounts.txt","a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close
        break