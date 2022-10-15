# Write a program magicNumber.c to read two positive integers, each with at most 5 digits,
# and for each integer, add up the digits (from right) in positions 1, 3 and 5.
# The right-most digit of the sum is the required answer.


def Magic(input):
    "Get the total of a number less than 5 digits in position 1 3 5 from right to left"
    total = 0
    for i in range(1, 6):
        if i % 2 != 0:
            total += input % 10
        input //= 10
    return total % 10


def main():
    Magic()
    a = int(input("Here: "))
    ma = Magic(a)
    print(ma)

    b = int(input("Here: "))
    mb = Magic(b)
    print(mb)


if __name__ == "__main__":
    main()
