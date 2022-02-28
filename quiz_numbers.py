"""CSC 161 Quiz: Numbers

Lihang Liu
Lab Section CSC 161-2 TR 2:00-3:15pm
Spring 2022
"""


def main():
    a = int(input("How many numbers do you want to print? "))
    for i in range(a):
        print(i + 1, " ", (i + 1) ** 3)
    print("Have a nice day!")


if __name__ == "__main__":
    main()
