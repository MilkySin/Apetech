def SumLast3(listf):
    list_range = len(listf)
    total = sum(listf[: (-list_range + 1) : -1])
    return total


def MakeList(size: int):
    listf = []
    while len(listf) < int(size):
        inputlist = int(input("> "))
        listf.append(inputlist)
        print(listf)
    return listf


def main():
    size = input("List size: ")
    listf = MakeList(size)
    print(SumLast3(listf))


if __name__ == "__main__":
    main()
