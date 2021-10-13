#!/usr/bin/python3

inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
        print(f"Total snowfall inches", {total_inches})

print_total_snowfall(inches_snow)
new_user = input("How many inches of snow fell on Thursday? ")
inches_snow["Thursday"] = int(new_user)
print_total_snowfall(inches_snow)

