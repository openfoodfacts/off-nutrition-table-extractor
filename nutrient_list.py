import argparse

def make_list(fname):
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    # return tuple(open(fname, 'r'))
    return tuple(content);

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="Enter the path to the Nutrient Labels list")
    args = ap.parse_args()

    print(make_list(args.path))