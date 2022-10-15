import sys
import os


def MenuDialog():
    listf = list(range(1, 8))
    print("+===================================================================+")
    print("|                    EMPLOYEE MANAGEMENT PROGRAM                    |")
    print("+===================================================================+")
    print("| 1. Input |2. Sort |3. Analyze |4. Find |5. Save |6. Open |7. Exit |")
    print("+===================================================================+")
    return listf


def UserInput():
    user_input = input("> ")
    return user_input


def YesNoCancel():
    print("Do you want to continue ?\n")
    print("- Yes, I do. (press 'y', 'Y')\n")
    print("- No, I don't. (press 'n', 'N')\n")
    print("- Please clear the screen ! (press 'c', 'C')\n")
    return


def Loop():
    YesNoCancel()
    str_input = UserInput().upper()
    if str_input == "Y":
        main()
    if str_input == "N":
        sys.exit()
    if str_input == "C":
        os.system("clear")
        main()
    else:
        Loop()
    return


def main():
    listf = MenuDialog()
    new = []
    for i in listf:
        new.append(str(i))
    user_input = UserInput()
    if user_input not in new:
        main()
    if user_input == "7":
        sys.exit()
    else:
        Loop()


if __name__ == "__main__":
    main()
