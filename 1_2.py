if __name__ == "__main__":
    with open("./data/1") as data_file:
        current_count = 0
        counts = []
        for l in data_file:
            if l =='\n':
                counts.append(current_count)
                current_count = 0
            else:
                current_count += int(l)

        counts.sort()
        print(sum(counts[-3:]))