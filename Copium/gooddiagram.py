from email.policy import default
import os


def MenuDialog():
    print("+===================================================================+")
    print("|                    EMPLOYEE MANAGEMENT PROGRAM                    |")
    print("+===================================================================+")
    print("| 1. Input |2. Sort |3. Analyze |4. Find |5. Save |6. Open |7. Exit |")
    print("+===================================================================+")


def UserInput():
    user_input = input("> ")
    return user_input


def YesNoCancel():
    print("Do you want to continue ?\n")
    print("- Yes, I do. (press 'y', 'Y')\n")
    print("- No, I don't. (press 'n', 'N')\n")
    print("- Please clear the screen ! (press 'c', 'C')\n")
    user = UserInput().upper()
    while True:
        match user:
            case "Y":
                main()
                return
            case "N":
                return False
            case "C":
                os.system("cls" if os.name == "nt" else "clear")
                main()
                return
            case default:
                YesNoCancel()
                return


def Case(user: str):
    while True:
        match user:
            case "1":
                YesNoCancel()
                return
            case "2":
                YesNoCancel()
                return
            case "3":
                YesNoCancel()
                return
            case "4":
                YesNoCancel()
                return
            case "5":
                YesNoCancel()
                return
            case "6":
                YesNoCancel()
                return
            case "7":
                return False
            case default:
                main()
                return


def main():
    MenuDialog()
    user = UserInput()
    Case(user)


if __name__ == "__main__":
    main()
