#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 28, 2023
# This program calculates the area of a triangle


def calc_area_triangle(base, height):
    # calculate area
    area = (base * height) / 2

    # display area
    print("The area is {} cm^2".format(area))


def main():
    # get base and height
    print("Calculating the Area of a Triangle")
    base_from_user_str = input("What is the base of your triangle (cm)?")
    height_from_user_str = input("What is the height of your triangle (cm)?")
    try:
        # convert base to float
        base_from_user_float = float(base_from_user_str)

        # convert height to float
        height_from_user_float = float(height_from_user_str)

        # if the height or base <= 0, tell them to enter positive num
        if height_from_user_float <= 0 or base_from_user_float <= 0:
            print("Please enter a positive number for both values.")
        else:
            # otherwise, call the calc_area_triangle() function
            calc_area_triangle(base_from_user_float, height_from_user_float)
    except:
        # if the base or height cannot become a number, then tell the user to enter a number.
        print(
            "{} or {} is not a valid number.".format(
                base_from_user_str, height_from_user_str
            )
        )


if __name__ == "__main__":
    main()
