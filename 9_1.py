import numpy as np

if __name__ == "__main__":
    trees_list = []
    with open("./data/9") as data_file:
        
        H = np.array([0,0], dtype=np.int32)
        T = np.array([0,0], dtype=np.int32)

        visited_positions = set()
        visited_positions.add(tuple(T))

        moves = {
            'R' : np.array([0, +1], dtype=np.int32),
            'L' : np.array([0, -1], dtype=np.int32),
            'U' : np.array([-1, 0], dtype=np.int32),
            'D' : np.array([+1, 0], dtype=np.int32),
        }

        for l in data_file:
            command, value = l.split(' ')
            value = int(value)
            for i in range(value):
                H += moves[command]
                difference = H-T
                distance = np.abs(difference)

                if np.linalg.norm(distance, ord=1) > 2:
                    T += np.array([np.copysign(1, difference[0]), np.copysign(1, difference[1])], dtype=np.int32)
                elif distance[0] > 1:
                    T += np.array([np.copysign(1, difference[0]), 0], dtype=np.int32)
                elif distance[1] > 1:
                    T += np.array([0, np.copysign(1, difference[1])], dtype=np.int32)

                visited_positions.add(tuple(T))

        print(len(visited_positions))
                


                
            
        