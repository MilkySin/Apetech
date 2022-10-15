def GreatestSum(listf):
    if len(listf) == 0:
        print("GIVE NUMBERS!!!!1111")
    else:
        maxnum = listf[0]
        for i in listf:
            for j in listf:
                if maxnum < i + j and j != i:
                    maxnum = i + j
        return maxnum


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
    print(GreatestSum(listf))


if __name__ == "__main__":
    main()
