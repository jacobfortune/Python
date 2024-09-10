#Let the Auth begin...
Main = 0
Begin = 0

#These are the permanent values for each password
#This file is classified and must not be able to be viewed from the outside
Password1 = "Legendary"
Password2 = "FoxyLOL123!"
Password3 =  "77xZzZjaya77jaya888"

print("Hello user!")

user_name = input("Please input your username here | ")

#We begin to validate usernames and find out if a user needs to log in or sign up
if user_name == "jacobPortla":
    Main = Main +1
elif user_name == "zacLOL":
    Main = Main +2
elif user_name == "jonnyLOL":
    print("Sorry user is banned from this guild")
    Main = Main + 6
elif user_name == "Dazzle":
    Main = Main +3
elif user_name == " ":
    print("Password:     LOL")
    Main = Main +4
else:
    choice = input("Would you like to sign up? | ")
    if choice == "yes":
        Main = Main + 5
    elif choice == "Yes":
        Main = Main + 5
    elif choice == "Yes Please":
        Main = Main + 5
    elif choice == "ye":
        Main = Main + 5
    elif choice == "yeah":
        Main = Main + 5
    else:
        print("Okay, sure sure")

#Whatever username was chosen, they will get a distinct main value
#The Main value will allow them to either log in with a pre-selected password or create a new account
if Main == 1:
    Input1 = input("Please enter the password for that account | ")
    if Input1 == "Legendary":
        print("You have administrator access to the .com servers.")
        Passed = True
    else:
        print("Username or password was incorrect.")
        Passed = False
elif Main == 2:
    Input2 = input("Please enter the password for that account | ")
    if Input2 == "FoxyLOL123!":
        print("You have guest access to the .co.uk servers")
        Passed = True
    else:
        print("Username or password was incorrect.")
        Passed = False
elif Main == 3:
    Input3 = input("Please enter the password for that account | ")
    if Input3 == "77xZzZjaya77jaya888":
        Input5 = input("Please enter a secondary passphrase. | " )
        if Input5 == "IRON MAN SUCKS":
            Input6 = input("Please enter the tertiary passphrase. | ")

            if Input6 == "Jonny is an UWU kitten fr fr":
                input7 = input("What is the encryption key for IEEE | ")
                if input7 == "Ls5Sb?da@3Dfgfsfdsfead":
                    print("You have access to the IEEE servers and administrator access to any server on the Cloudflare network.")
                    Passed = True
                else:
                    print("You have administrator access to the Cloudflare Network. ")
                    Passed = "Partial"
            else:
                print("Username or password was incorrect.")
                Passed = False
        else:
            print("Username or password was incorrect.")
            Passed = False
    else:
        print("Username or password was incorrect.")
        Passed = False
elif Main == 4:
    print("Invalid.")
    Passed = False
elif Main == 5:
    Begin = Begin + 1
elif Main == 6:
    print("User is still banned from this guild... lol.")
    Passed = False
else:
    print("username or password was incorrect!")
    Passed = False

#This block of code will allow a user to create a new username and password and authenticate here.
while Begin == 1:
    user_name2 = input("What will be your new user_name? | ")
    if user_name2 == "zacLOL":
        print("Username is already taken")
        Begin = 1
    elif user_name2 == "jacobPortla":
        print("Username is already taken")
        Begin = 1
    elif user_name2 == "Dazzle":
        print("Username is already taken")
        Begin = 1
    elif user_name2 == "jonnyLOL":
        print("User is banned from this guild")
    else:
        Begin = 2

    while Begin == 2:
        Password4 = input("What will be your new password | ")
        char_COUNT = len(Password4)
        if char_COUNT < 8:
            print("Password is too small. Must be 8 characters or longer.")
        else:
            print("Now you can log in!")
            user_name = input("Please input your username here | ")
            if user_name == user_name2:
                Input4 = input("Please enter the password for that account | ")
                if Input4 == Password4:
                    print("You have successfully authenticated to the IEEE servers, you have guest-level access.")
                    Passed = True
                    Begin = Begin + 1
                else:
                    print("Incorrect password or username")
                    Begin = 3
                    Passed = False
            else:
                print("Incorrect username or password")
                Begin = 3
                Passed = False

print("User has Passed Authentication: | " + str(Passed))