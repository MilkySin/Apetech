import random


def Logic(first: list, second: list) -> int:
    lol = [first, second]
    previous = lol[0][0]
    print(lol)
    for i in lol:
        for next in i:
            if next < previous:
                previous = next
    print(previous)


def MakeList(size: int, N: int):
    listf = []
    while len(listf) < int(size):
        listf.append(random.randrange(1, int(N)))
    print(listf)
    return listf


def main():
    sizeA = input("size of list: ")
    rangeA = input("range of elements: ")
    a = MakeList(sizeA, rangeA)
    sizeB = input("size of list: ")
    rangeB = input("range of elements: ")
    b = MakeList(sizeB, rangeB)
    Logic(a, b)


if __name__ == "__main__":
    main()
