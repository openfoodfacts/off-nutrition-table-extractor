import re
import argparse
from nutrient_list import make_list

def change_to_g(text):
    search_ln = re.search("\d\s|\d$", text)
    if search_ln and search_ln.group().strip() == "9":
        index = search_ln.span()[0]
        text = text[:index] +"g"+ text[index+1:]

    search_lnq = re.search("\dmq\s|\dmq$", text)
    if search_lnq:
        index = search_lnq.span()[0] +2
        text = text[:index] +"g"+ text[index+1:]
    return text

def clean_string(string):
    pattern = "[\|\*\_\'\—\-\{}]".format('"')
    text = re.sub(pattern, "", string)
    text = re.sub("Omg", "0mg", text)
    text = re.sub("Og", "0g", text)
    text = re.sub('(?<=\d) (?=\w)', '', text)
    text = change_to_g(text)
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

    if len(label_arr) == 0:
        label_name = "|"+string+'|'
    elif len(label_arr) == 1:
        label_name = label_arr[0]
    else:
        label_name = label_arr[0] + ' ' + label_arr[1]

        

    digit_pattern = "[-+]?\d*\.\d+g|\d+"
    value_arr = re.findall("{0}g|{0}%|{0}J|{0}kJ|{0}mg|{0}kcal".format(digit_pattern), string)
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
        print(check_for_label(args.string, make_list("data/big.txt")))
    elif FLAG == 2:
        print(get_label_from_string(args.string))

if __name__ == '__main__':
    main()