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
        # convert base and height to float
        base_from_user_int = float(base_from_user_str)
        height_from_user_int = float(height_from_user_str)

        # call the calc_area_triangle() function
        calc_area_triangle(base_from_user_int, height_from_user_int)
    except:
        # if the base or height cannot become a number, then tell the user to enter a number.
        print(
            "{} or {} is not a valid number.".format(
                base_from_user_str, height_from_user_str
            )
        )


if __name__ == "__main__":
    main()
