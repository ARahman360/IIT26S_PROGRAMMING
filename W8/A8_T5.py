import A8_T5_Lib


def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def showUserOptions() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")


def userMenu(username: str, user_id: int) -> None:
    while True:
        showUserOptions()
        choice = input("Your choice: ")
        if choice == "1":
            print(f"Profile ID {user_id} - {username}")
        elif choice == "2":
            print("Change password is not implemented.")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Unknown option!")
        print()
    print()


def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = input("Your choice: ")
        if choice == "1":
            username = input("Insert username: ")
            password = input("Insert password: ")
            user_id = A8_T5_Lib.loginUser(username, password)
            if user_id == -1:
                print("Authentication failed!")
            else:
                print("Authentication successful!")
                print()
                userMenu(username, user_id)
        elif choice == "2":
            username = input("Insert username: ")
            password = input("Insert password: ")
            A8_T5_Lib.registerUser(username, password)
            print("User registration completed!")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
        print()
    print()
    print("Program ending.")


if __name__ == "__main__":
    main()
