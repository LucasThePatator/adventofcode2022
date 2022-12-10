import numpy as np

def draw(x: int, cycle: int):
    row = int(cycle/40)
    col = cycle % 40

if __name__ == "__main__":
    with open("./data/10") as data_file:
        x = 1
        strength = 0
        cycle = 1
        for l in data_file:
            
            if cycle % 40 == 20:
                strength += cycle*x

            cycle+=1
            if l[0] == 'a':
                command, value = l.split(' ')
                #deal with the passed cycle
                if cycle % 40 == 20:
                    strength += cycle*x
                cycle += 1

                x += int(value)
                
        print(strength)
                


                
            
        