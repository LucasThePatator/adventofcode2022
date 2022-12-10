import numpy as np

CRT = [['.' for _ in range(40)] for _ in range(6)]

def draw(x: int, cycle: int):
    row = int((cycle-1)/40)
    col = (cycle-1) % 40
    if(col == x-1):
        CRT[row][col] = '#'
    if(col == x):
        CRT[row][col] = '#'
    if(col == x+1):
        CRT[row][col] = '#'


if __name__ == "__main__":
    with open("./data/10") as data_file:
        x = 1
        strength = 0
        cycle = 1
        for l in data_file:

            draw(x, cycle)
            cycle+=1          
            if l[0] == 'a':
                command, value = l.split(' ')
                #deal with the passed cycle
                draw(x, cycle)
                cycle += 1

                x += int(value)
                
        for l in CRT:
            print(l)
                


                
            
        