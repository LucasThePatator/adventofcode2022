import typing

if __name__ == "__main__":
    with open("./data/6") as data_file:
        line = data_file.readline()
        current = line[0:4]
        for i in range(4, len(line)):
            if len(set(current)) == 4:
                print(i)
                break

            current = [*current[1:], line[i]]
