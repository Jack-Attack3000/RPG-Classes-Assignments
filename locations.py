# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing wiht locations


def print_loc_list(loc_list):
    """Prints list of locations and their info"""
    for loc_name, loc_info in loc_list.items():
        print(f"\nThe {loc_name.title()} is {loc_info['description']}.")
