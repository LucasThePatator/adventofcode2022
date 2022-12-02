if __name__ == "__main__":

    scores = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }

    with open("./data/2") as data_file:
        score = 0
        counts = []
        for l in data_file:
            opp, me = l.split()
            score += scores[me]
            if ord(opp) + 23 == ord(me):
                score += 3
            elif opp == 'A' and me=='Y' or opp == 'B' and me=='Z' or opp == 'C' and me=='X':
                score+=6
            
        print(score)