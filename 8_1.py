import numpy as np



if __name__ == "__main__":
    trees_list = []
    with open("./data/8") as data_file:
        for l in data_file:
            trees_list.append(list(map(int, list(l[:-1]))))

        trees = np.array(trees_list)

        visible = np.zeros(trees.shape)
        visible[:, 0] = 1
        visible[:, -1] = 1
        visible[0, :] = 1
        visible[-1, :] = 1

        running_max = np.maximum.accumulate(trees, 1)
        visible[:, 1:] += (running_max[:, 1:] - running_max[:, :-1]) > 0

        running_max = np.maximum.accumulate(trees, 0)
        visible[1:, :] += (running_max[1:, :] - running_max[:-1, :]) > 0

        running_max = np.maximum.accumulate(trees[:, ::-1], 1)
        visible[:, :-1] +=  (running_max[:, 1:] - running_max[:, :-1])[:, ::-1] > 0

        running_max = np.maximum.accumulate(trees[::-1, :], 0)
        visible[:-1, :] += (running_max[1:, :] - running_max[:-1, :])[::-1, :] > 0

        print(np.count_nonzero(visible))

        