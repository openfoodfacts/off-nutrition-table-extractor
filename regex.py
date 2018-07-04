import re
import argparse
from nutrient_list import label_list

def clean_string(string):
    pattern = "[\|\*\_\'\—\-]"
    text = re.sub(pattern, "", string)
    text = text.strip()
    return text

def check_for_label(text, words):
    # text = text.lower()
    for i in range(len(text)):
        if any(text[i:].startswith(word) for word in words):
            return True
    return False

def get_label_from_string(string):
    label_arr = re.findall("([A-Z][a-zA-Z]*)", string)
    label_name = ""
    label_value = ""
    # print(label_arr)
    if len(label_arr) == 1:
        label_name = label_arr[0]
    elif len(label_arr) == 2:
        label_name = label_arr[0] + ' ' + label_arr[1]
    
    digit_pattern = "[-+]?\d*\.\d+|\d+"
    value_arr = re.findall("{0}g|{0}%|{0}J|{0}kJ|{0}mg".format(digit_pattern), string)
    # print(value_arr)
    if len(value_arr):
        label_value = value_arr[0]
    else:
        label_value = "|"+string+'|'
    return label_name, label_value

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--string", required=True, help="Enter the string to be cleaned")
    ap.add_argument("-f", "--flag", required=True, help="Get which function ot call")
    args = ap.parse_args()

    FLAG = int(args.flag)
    
    if FLAG == 0:
        print('Input: '+ args.string)
        print('Output: ' + clean_string(args.string))
        
    elif FLAG == 1:
        print(check_for_label(args.string, label_list))
    elif FLAG == 2:
        print(get_label_from_string(args.string))

if __name__ == '__main__':
    main()