if choice == "1":
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Username or Password")

elif choice == "2":
    print("Add Notes Selected")

elif choice == "3":
    print("View Notes Selected")

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid Choice")