if __name__ == "__main__":

    scores_result = {
        'X' : 0,
        'Y' : 3,
        'Z' : 6
    }

    scores_play = {
        'A' : 1,
        'B' : 2,
        'C' : 3
    }

    with open("./data/2") as data_file:
        score = 0
        counts = []
        for l in data_file:
            opp, me = l.split()
            score += scores_result[me]
            if me=='X':
                score+=scores_play['C' if opp=='A' else chr(ord(opp) - 1)]
            if me=='Y':
                score+=scores_play[opp]
            if me=='Z':
                score+=scores_play['A' if opp=='C' else chr(ord(opp) + 1)]
            
        print(score)