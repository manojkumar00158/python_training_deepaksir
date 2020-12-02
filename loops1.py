
i = 1
while True:
        user_name = input("Enter user name: ")
        password = input("password: ")
        if i<3:
                if user_name == "Manoj kumar" and password == "something":
                    print("logged in")
                    break
        else:
            print("attemped maximum")
            break
        i+=1
