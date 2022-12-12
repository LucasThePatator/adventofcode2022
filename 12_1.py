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

        #ti Dijkstra
        in_list = np.zeros(field.shape)
        predecessor = np.zeros((*field.shape, 2))
        distance = np.zeros(field.shape)
        open_list = [start]

        def get_neighbours(point):
            if point[0] > 0:
                temp = point - np.array([1, 0])
                if in_list[*temp] == 0 and field[*temp] - field[*point] <= 1 :
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1
            
            if point[0] < field.shape[0] - 1:
                temp = point + np.array([1, 0])
                if in_list[*temp] == 0 and field[*temp] - field[*point] <= 1:
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1

            if point[1] > 0:
                temp = point - np.array([0, 1])
                if in_list[*temp] == 0 and field[*temp] - field[*point] <= 1:
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1
  
            if point[1] < field.shape[1] - 1:
                temp = point + np.array([0, 1])
                if in_list[*temp] == 0 and field[*temp] - field[*point] <= 1 :
                    open_list.append(temp)
                    distance[*temp] =  distance[*point] + 1
                    in_list[*temp] = 1

        while True:
            open_list.sort(key= lambda p : distance[*p])
            exploring = open_list.pop(0)
            if (exploring == end).all():
                break

            get_neighbours(exploring)

        print(distance[*end])







       
                


                
            
        