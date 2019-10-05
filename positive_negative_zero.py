# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program lets the user enter an integer and tells them if it's positive
# or negative or a zero


def main():
    # this functions runs the program

    # input
    integer = int(input("Enter an integer: "))

    # process
    if (integer == 0):
        print("0")
    elif (integer < 0):
        print("negative")
    else:
        print("positive")


if __name__ == "__main__":
    main()
