from config import *


def hello():
    print("hello")


def plus():
    print(1 + 3)
    print(1 + 6)
    print(1 + 9)


def main():
    hello()
    print(f"{USER_NAME},hello,world!")
    plus()


if __name__ == '__main__':
    main()
