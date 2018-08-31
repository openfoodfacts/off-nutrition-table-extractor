import re
import argparse
import fuzzydict
from nutrient_list import *

#one of the most common OCR error of returning '9' in
# place of 'g' is being handled by this function
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

#Removes all the unnecessary noise from a string
def clean_string(string):
    pattern = "[\|\*\_\'\—\-\{}]".format('"')
    text = re.sub(pattern, "", string)
    text = re.sub(" I ", " / ", text)
    text = re.sub("^I ", "", text)
    text = re.sub("Omg", "0mg", text)
    text = re.sub("Og", "0g", text)
    text = re.sub('(?<=\d) (?=\w)', '', text)
    text = change_to_g(text)
    text = text.strip()
    return text

#Check whether a nutritional label is present in the
#string or not
def check_for_label(text, words):
    # text = text.lower()
    for i in range(len(text)):
        if any(text[i:].startswith(word) for word in words):
            return True
    return False

def fuz_check_for_label(text, fuzdict, debug):
    if debug:
        print("fuz_check_for_label : {}".format(text))
    # text = text.lower()
    text = clean_string(text)
    if fuzdict.__contains__(text):
        return True
    else:
        if fuzdict.__contains__(re.split('[/|I]',text)[0]):
            return True
    return False


#Separate the value and its label from the string
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

#Separate the value and its label from the string
def get_fuz_label_from_string(string, fuzdict, debug):
     string = clean_string(string)
     if debug:
         print("get_fuz_label_from_string : {}".format(string))
     label_arr = re.findall("([a-zA-Z]+)", string)
     label_name = ""
     label_value = ""

     if fuzdict.__contains__(string):
         label_name = fuzdict[string]
     else:
         label_name = fuzdict[re.split('[/|I]',string)[0]]

     digit_pattern = "[-+]?\d*[\.\,\']?\d+"
     value_arr = re.findall("{0}g|{0}%|{0}J|{0}kJ|{0}mg|{0}kcal|{0}".format(digit_pattern),  string)
     if debug:
        print(value_arr)
     if len(value_arr):
         label_value = value_arr[0]
     else:
         label_value = "|"+string+'|'
     return label_name, label_value

#Separate the unit from its value. (eg. '24g' to '24' and 'g')
def separate_unit(string):
    r1 = re.compile("(\d+[\.\,\']?\d*)([a-zA-Z]+)")
    m1 = r1.match(string)
    r2 = re.compile("(\d+[\.\,\']?\d*)")
    m2 = r2.match(string)
    if m1:
       return (float(m1.group(1).replace(',','.').replace("'",'.')), m1.group(2))
    elif m2:
       return (float(m2.group(1).replace(',','.').replace("'",'.')))
    else:
       return ("")

#main function to test different functions independently
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
    elif FLAG == 3:
        print(separate_unit(args.string))

if __name__ == '__main__':
    main()
