import numpy as np

if __name__ == "__main__":
    trees_list = []
    with open("./data/8") as data_file:
        for l in data_file:
            trees_list.append(list(map(int, list(l[:-1]))))

        trees = np.array(trees_list)
        height, width = trees.shape

        visible = np.ones(trees.shape)

        for row_i in range(height):
            for col_i in range(width):
                tree_size = trees[row_i, col_i]

                current_count = 0
                for row in range(row_i+1, height):
                    current_count += 1
                    if trees[row, col_i] >= tree_size:
                        break
                visible[row_i, col_i] *= current_count

                current_count = 0
                for row in range(row_i-1, -1, -1):
                    current_count += 1
                    if trees[row, col_i] >= tree_size:
                        break            
                visible[row_i, col_i] *= current_count

                current_count = 0
                for col in range(col_i+1, width):
                    current_count += 1
                    if trees[row_i, col] >= tree_size:
                        break
                visible[row_i, col_i] *= current_count                 
                
                current_count = 0
                for col in range(col_i-1, -1, -1):
                    current_count += 1
                    if trees[row_i, col] >= tree_size:
                        break
                visible[row_i, col_i] *= current_count
                    

        print(np.max(visible))

        