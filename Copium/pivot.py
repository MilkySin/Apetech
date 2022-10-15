from functools import partial
import random


def Pivot(pivot, listf):
    listgreater = []
    listlesser = []
    for i in listf:
        if pivot > i:
            listlesser.append(i)
        if pivot < i:
            listgreater.append(i)
    return listlesser, listgreater


def MakeList(size: int, N: int):
    listf = []
    while len(listf) < int(size):
        listf.append(random.randrange(int(N)))
    print(listf)
    return listf


def Partition(list1: list, list2: list):
    list1.extend(list2)
    return list1


def main():
    pivot = int(input("Your pivot: "))
    size = int(input("List size: "))
    N = int(input("List range: "))
    listf = MakeList(size, N)
    list1, list2 = Pivot(pivot, listf)
    str_list = ", ".join(str(i) for i in list1)
    str_list2 = ", ".join(str(i) for i in list2)
    print(f"Elements less than {pivot}: {str_list}")
    print(f"Elements greater than {pivot}: {str_list2}")
    print(f"Lesser left, greater right {Partition(list1, list2)}")


if __name__ == "__main__":
    main()
