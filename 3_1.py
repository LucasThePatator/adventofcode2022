import typing

def get_priority(object : str):
    if object[0].islower():
        return ord(object[0]) - (ord('a') - 1)
    return ord(object[0]) - (ord('A') - 1) + 26


if __name__ == "__main__":

    with open("./data/3") as data_file:
        score = 0
        for l in data_file:
            length = len(l)
            l1 = l[0:int(length/2)]
            l2 = l[int(length/2):]
            intersect = set(l1).intersection(set(l2))
            score += get_priority(intersect.pop())
            
        print(score)