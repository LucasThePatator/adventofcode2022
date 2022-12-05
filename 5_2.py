stacks = ["BLDTWCFM",
"NBL",
"JCHTLV",
"SPJW",
"ZSCFTLR",
"WDGBHNZ",
"FMSPVGCN",
"WQRJFVCZ",
"RPMLH"]

if __name__ == "__main__":
    with open("./data/5") as data_file:
        for l in data_file:
            nb, temp = l.split(" from ")
            nb = int(nb[5:])
            from_i, to_i = temp.split(" to ")
            from_i = int(from_i) - 1
            to_i = int(to_i[:-1]) - 1
            

            stacks[to_i] += stacks[from_i][-1:-(nb+1):-1]
            stacks[from_i] = stacks[from_i][:-nb]

        output = ""
        for s in stacks:
            output += s[-1]

        print(output)
