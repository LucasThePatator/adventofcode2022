from functools import cmp_to_key

def parse_line(line: str):
    ret = []
    current_char = 0
    while current_char < len(line):
        if line[current_char] == '[':
            parsed, end = parse_line(line[(current_char+1):])
            ret.append(parsed)
            current_char += end + 2
        elif line[current_char] == ']':
            return ret, current_char
        elif line[current_char] == ',':
            current_char += 1
        else:
            end_char = current_char
            while ord('0') <= ord(line[end_char]) <= ord('9'):
                end_char += 1
            ret.append(int(line[current_char:end_char]))
            current_char = end_char
    
    return ret, len(line)
    
def compare(left, right):
    for val_l, val_r in zip(left, right):
        if type(val_l) == int and type(val_r) == int:
            if val_l < val_r:
                return 1
            if val_r < val_l:
                return -1

        elif type(val_l) == list and type(val_r) == list:
            ret = compare(val_l, val_r)
            if ret == 1:
                return 1      
            if ret == -1:
                return -1

        elif type(val_l) == int and type(val_r) == list:
            ret = compare([val_l], val_r)
            if ret == 1:
                return 1      
            if ret == -1:
                return -1

        elif type(val_l) == list and type(val_r) == int:
            ret = compare(val_l, [val_r])
            if ret == 1:
                return 1      
            if ret == -1:
                return -1

    if len(left) < len(right):
        return 1
    if len(left) == len(right):
        return 0
    
    return -1


with open('./data/13') as data_file:
    left = right = None
    count = 0
    packets = [[[2]], [[6]]]
    for i, l in enumerate(data_file):
        if i % 3 == 0:
            left, _ = parse_line(l[1:-1])
            packets.append(left)
        if i % 3 == 1:
            right, _ = parse_line(l[1:-1])
            packets.append(right)

            if(compare(left, right)):
                count +=  int(i/3) + 1


    packets.sort(key=cmp_to_key(compare), reverse=True)

    for i, p in enumerate(packets, start=1):
        print(f'{i} : {p}')

    

