import re

# while not end-of-File
#     get next expr
#     identify all inner expression ()

# 3 + (6 * 2 * (9 + 2 + 5) * (9 * 2 * 6 + 8 * 5) * (2 + 2 + 3 + 7 * 9)) + 4 * 4 + (6 * 4 * (9 + 4) + 8 * 3 * (5 + 3)) * 5
# 3 + (6 * 2 * val1 * val2 * val3 ) + 4 * 4 + (6 * 4 * val4 + 8 * 3 * val5) * 5
# 3 + val6

# a + b + c + a + b
# numleft = a
# x + c + a + b

# ((a+b))

#jason's strat
# while row
#   while parenthesis in string
#     evaluate string and replace parenthesis phrase with value
#       regex number space operand space number, then relpace with this value
#   evaluate string and replace with value
# sum rows


# read string '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
# while regex '\([\d\s\+\-\*\/]+\)'  #### this should grab inner parenthesis phrases
#   evaluate inner phrases respecting weird order of operations
#   replace captured regex with evaluated number

# from the docs: 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 1
# 
# '(\d+[+*]\d+){1}'
def read_data(fn):
    with open(fn, "r") as f:
        data = [l.strip() for l in f]
    return data

def add_numbers(line):
    numb = 0
    matches = re.finditer(r"\d*[\+\*]\d*", line, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        if matchNum == 1:
            numb = eval(match.group())
        else:
            numb = eval('{}{}'.format(numb, match.group()))
    return numb
    
def regex_match(line):
    regex = r"\([\d\s\+\*]+\)"
    r1 = re.findall(regex, line)
    print(line)
    for match in r1:
        clean_match = match.replace('(', '').replace(')', '').replace(' ', '')
        numb = add_numbers(clean_match)
        print(line.replace(match, numb))
        print(numb)
        

def main():
    data = read_data("test.txt")
    # data = read_data("input.txt")
    for line in data:
        regex_match(line)

    #print(data[:5])

if __name__ == "__main__":
    main()