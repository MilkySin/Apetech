list1 = [1, 2, 3, 4]
list2 = [3, 4, 2, 1, 9]


def isSubset(list1: list, list2: list) -> bool:
    print(list1, list2)
    for i in list1:
        if i in list2:
            return True
        return False


def MakeList(size: int):
    listf = []
    while len(listf) < int(size):
        inputlist = int(input("> "))
        listf.append(inputlist)
        print(listf)
    return listf


def main():
    size = int(input("size of first list: "))
    list1 = MakeList(size)
    size2 = int(input("size of first list: "))
    list2 = MakeList(size2)
    print(isSubset(list1, list2))


if __name__ == "__main__":
    main()
