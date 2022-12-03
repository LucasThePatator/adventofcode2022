import typing

def get_priority(object : str):
    if object[0].islower():
        return ord(object[0]) - (ord('a') - 1)
    return ord(object[0]) - (ord('A') - 1) + 26


if __name__ == "__main__":
    with open("./data/3") as data_file:
        score = 0
        current_set = set()
        for i, l in enumerate(data_file):
            if i % 3 == 0:
                current_set = set(l[:-1])
            else :
                current_set = set(l[:-1]).intersection(current_set)

            if i % 3 == 2:
                score += get_priority(current_set.pop())
            
        print(score)