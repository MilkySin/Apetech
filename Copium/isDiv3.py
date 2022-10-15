def isDiv3(listf: list):
    total = 0
    for i in listf:
        if i % 3 == 0:
            total += 1
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
    total = isDiv3(listf)
    print(f"number of elements divisable by 3 is {total}")


if __name__ == "__main__":
    main()
