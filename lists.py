#!/usr/bin/env python3

# Created by: Dylan Melo
# Created on: Feb 2022
# This program asks a user for a list of either ints,
# floats, or strings and locate and count the character
# they inputted in the list.

# let user choose which element for the list.
def list_position_str():

    index_list3 = []
    string_3 = input("Enter your amount of strings: ")

    try:
        string_3_int = int(string_3)
    except Exception:
        print("Invalid input!")
        list_position_str()

    # loop the input to the appending value
    for i in range(1, string_3_int + 1):
        value_3 = input("Enter your string: %d: " % i)
        index_list3.append(value_3)

    item_3 = input("Enter the character(s) "
                   "you want to find\n> ")

    try:
        print("The first position of your string= ", index_list3.index(item_3))
        print("Your string occurs {} time(s)".
              format(index_list3.count(item_3)))
    except ValueError:
        print("Number entered is on -1(not on list)")
        list_position_int()


def list_position_float():

    index_list2 = []
    floats_2 = input("Please enter the amount of floats: ")

    try:
        floats_2_int = int(floats_2)
    except Exception:
        print("Invalid input!")
        list_position_float()

    for i in range(1, floats_2_int + 1):
        value_2 = input("\nEnter the value of the float %d: " % i)

        try:
            value_2_float = float(value_2)
        except Exception:
            print("Invalid input!")
            list_position_float()
        index_list2.append(value_2_float)

    item_2 = input("Enter the float you wish to count: ")

    try:
        item_2_float = float(item_2)
    except Exception:
        print("Invalid input!")
        list_position_choice()

    try:
        print("\nThe first position of your number = ",
              index_list2.index(item_2_float))
        print("Your number occurs {} time(s)".
              format(index_list2.count(item_2_float)))
    except ValueError:
        print("Number entered is on -1(not on list)")
        list_position_int()


def list_position_int():

    index_list1 = []
    int_1 = input("Enter the number of elements on your list : ")

    try:
        int_1_int = int(int_1)
    except Exception:
        print("Invalid input!")
        list_position_float()

    for i in range(1, int_1_int + 1):
        value_1 = input("Please enter the Value of %d Element: " % i)

        try:
            value_1_int = int(value_1)
        except Exception:
            print("Invalid input!")
        index_list1.append(value_1_int)

    item_1 = input("Enter the integer you want: ")

    try:
        item_1_int = int(item_1)
    except Exception:
        print("Invalid input!")
        list_position_choice()

    try:
        print("The first position of your number = ",
              index_list1.index(item_1_int))
        print("Your string occurs {} time(s)".
              format(index_list1.count(item_1_int)))
    except ValueError:
        print("String entered is on -1(not on list)")
        list_position_str()


def choice():

    element_choice = input("Which element is your list made of "
                           "enter(floats, integers, strings)?\n> ")

# bounce them to the function of their choosing.
    if (element_choice == "int" or element_choice == "integer" or
            element_choice == "ints" or element_choice == "integers"):
        print()
        list_position_int()
    elif (element_choice == "floats" or element_choice == "float"):
        print()
        list_position_float()
    elif (element_choice == "strings" or element_choice ==
            "string" or element_choice == "str"):
        print()
        list_position_str()
    else:
        print("Invalid choice!")
        list_position_choice()


def list_position_choice():
    print("Invalid choice.")
    list_position_choice()


def main():
    # Introduce the program to user.
    print("Welcome to my program, you can enter a list of\n "
          "strings, ints, or floats, and find the first index of the\n "
          "element along with how many times it occurs.")
    choice()


if __name__ == "__main__":
    main()
