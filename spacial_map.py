import argparse
import re

def string_type(string):
    """
    @param string: Type of the string to be checked
        0: both name and value
        1: only the value
        2: only the name
    """
    if any(char.isdigit() for char in string): 
 
        if re.search(r'\D{3,}\s', string):
            return 0
        else:
            return 1

    return 2

def position_definer(center_y, ymin, ymax):
    """
    @param center_y: y coordinate of the search box
    @param ymin: minimum y coordinate of the box to be tested for
    @param ymax: maximum y coordinate of the box to be tested for
    """
    return ymin < center_y < ymax
    
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--string", required=True, help="string to be checked")
    args = ap.parse_args()

    print(string_type(args.string))
