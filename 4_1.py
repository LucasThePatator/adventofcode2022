import typing

if __name__ == "__main__":
    with open("./data/4") as data_file:
        score = 0
        for l in data_file:
            p1, p2 = l[:-1].split(',')
            p1 = list(map(int, p1.split('-')))
            p2 = list(map(int, p2.split('-')))

            if(p1[0] <= p2[0] and p1[1] >= p2[1]) or (p1[0] >= p2[0] and p1[1] <= p2[1]):
                score += 1

        print(score)
