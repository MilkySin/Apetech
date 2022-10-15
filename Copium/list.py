def MakeList(size: int):
    listf = []
    while len(listf) < int(size):
        inputlist = int(input("> "))
        listf.append(inputlist)
        print(listf)
    return listf


def IsAscending(listf: list):
    previous = listf[0]
    for next in listf:
        if next < previous:
            return False
        previous = next
    return True


def main():
    size = input("List size: ")
    listf = MakeList(size)
    print(IsAscending(listf))


if __name__ == "__main__":
    main()
