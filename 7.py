import typing
import time
class Node:
        def __init__(self, name : str, parent, is_dir : bool):
            self.name: str = name
            self.children = {}
            self.parent = parent
            self.size: int = 0
            self.is_directory: bool = is_dir

def print_tree(node : Node, level : int):
    if node.is_directory: 
        print(' ' * level + f'-{node.name}')
        for child in node.children.values():
            print_tree(child, level+1)
    else:
        print(' ' * level + f'-{node.name} {node.size}')

def compute_sizes(node : Node):
    if node.is_directory:
        node.size = 0
        for child in node.children.values():
            node.size += compute_sizes(child)

    return node.size

def get_sizes_with_criteria(node : Node, criteria : typing.Callable , output : list[int]):
    if node.is_directory:
        if criteria(node.size):
            output.append(node.size)

        for child in node.children.values():
            if child.is_directory:
                get_sizes_with_criteria(child, criteria, output)
    else:
        return


if __name__ == "__main__":
    t0 = time.time()
    with open("./data/7") as data_file:
        in_ls = False

        root_node = Node('/', None, True)
        current_node = root_node
        for l in data_file:
            if l[0] == '$':
                in_ls = False
                if l[2:4] =='ls':
                    in_ls = True
                elif l[2:4] == 'cd':
                    if l[5] == '/':
                        current_node = root_node
                    elif l[5:7] == '..':
                        current_node = current_node.parent
                    else:
                        dir_name = l[5:-1]
                        if dir_name in current_node.children and current_node.children[dir_name].is_directory:
                            current_node = current_node.children[dir_name]

            elif in_ls:
                p1, p2 = l.split(' ')
                p2 = p2[:-1]
                if p1 == 'dir':
                    current_node.children[p2] = Node(p2, current_node, True)
                else:
                    current_node.children[p2] = Node(p2, current_node, False)
                    current_node.children[p2].size = int(p1)

        print_tree(root_node, 0)
        compute_sizes(root_node)
        output = []
        get_sizes_with_criteria(root_node, lambda s : s <= 100000, output)
        print(sum(output))

        total_size = 70000000
        current_size = root_node.size
        needed_space = 30000000
        need_to_free = needed_space - (total_size - current_size)
        output = []
        get_sizes_with_criteria(root_node, lambda s : s >= need_to_free, output)
        print(min(output))
        t1=time.time()
        print(t1-t0)


                



          
