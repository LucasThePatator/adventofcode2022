import numpy as np

if __name__ == "__main__":

    data_list = []

    with open("./data/12") as data_file:
        for l in data_file:
            data_list.append(list(map(ord, list(l[:-1]))))

        field = np.array(data_list)

        start = np.argwhere(field == ord('S'))[0]
        field[*start] = ord('a')
        end = np.argwhere(field == ord('E'))[0]
        field[*end] = ord('z')

        starts = np.argwhere(field == ord('a'))

        #ti Dijkstra
        in_list = np.zeros(field.shape)
        predecessor = np.zeros((*field.shape, 2))
        distance = np.zeros(field.shape)
        open_list = [end]

        def get_neighbours(point):
            if point[0] > 0:
                temp = point - np.array([1, 0])
                if in_list[*temp] == 0 and field[*temp] - field[*point] >= -1 :
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1
            
            if point[0] < field.shape[0] - 1:
                temp = point + np.array([1, 0])
                if in_list[*temp] == 0 and field[*temp] - field[*point] >= -1:
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1

            if point[1] > 0:
                temp = point - np.array([0, 1])
                if in_list[*temp] == 0 and field[*temp] - field[*point] >= -1:
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1
  
            if point[1] < field.shape[1] - 1:
                temp = point + np.array([0, 1])
                if in_list[*temp] == 0 and field[*temp] - field[*point] >= -1 :
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1

        while len(open_list) > 0:
            open_list.sort(key= lambda p : distance[*p])
            exploring = open_list.pop(0)

            get_neighbours(exploring)

        min_distance = 1000000000000000000000000
        for s in starts:
            if distance[*s] > 0:
                min_distance = min(min_distance, distance[*s])

        print(min_distance)







       
                


                
            
        