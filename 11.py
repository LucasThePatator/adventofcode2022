import copy

class Monkey:

    common_divisor = 1

    def __init__(self):
        self.items : list[int] = []
        self.operation = lambda x : x
        self.test_value : int = 1
        self.true_throw : int = 0
        self.false_throw : int = 1
        self.count_inspected : int = 0

    def __str__(self):
        ret = f'\n{self.items}\n'
        ret += f'divisor {self.test_value}\n'
        ret += f'{self.true_throw} / {self.false_throw}\n'
        ret += f'inspected {self.count_inspected}\n'

        return ret
    
    def __repr__(self):
        return self.__str__()

    def inspect_1(self, monkeys):
        current_item = self.items.pop(0)
        current_item = int(self.operation(current_item) / 3)
        current_item %= Monkey.common_divisor

        if current_item % self.test_value == 0:
            monkeys[self.true_throw].items.append(current_item)
        else:
            monkeys[self.false_throw].items.append(current_item)

        self.count_inspected += 1

    def inspect_2(self, monkeys):
        current_item = self.items.pop(0)
        current_item = int(self.operation(current_item))
        current_item %= Monkey.common_divisor

        if current_item % self.test_value == 0:
            monkeys[self.true_throw].items.append(current_item)
        else:
            monkeys[self.false_throw].items.append(current_item)

        self.count_inspected += 1

monkeys: list = []

def parse_text(text: str):
    monkeys_text = text.split('\n\n')
    for monkey in monkeys_text:
        monkeys.append(parse_monkey(monkey))

def parse_monkey(monkey_text: str):
    monkey = Monkey()
    lines = monkey_text.split('\n')
    monkey.items = list(map(int, lines[1][18:].split(',')))
    monkey.operation = lambda old : eval(lines[2][19:])
    monkey.test_value = int(lines[3][21:])
    Monkey.common_divisor *= monkey.test_value
    monkey.true_throw = int(lines[4][29:])
    monkey.false_throw = int(lines[5][30:])

    return monkey

if __name__ == "__main__":
    with open("./data/11") as data_file:
        text = data_file.read()
        parse_text(text)

        original_monkeys = copy.deepcopy(monkeys)
        for round in range(20):
            for monkey in monkeys:
                while len(monkey.items) > 0:
                    monkey.inspect_1(monkeys)

        monkeys_1 = sorted(monkeys, key = lambda m : -m.count_inspected)
        print(monkeys_1[0].count_inspected * monkeys_1[1].count_inspected)

        monkeys = original_monkeys
        for round in range(10000):
            for monkey in original_monkeys:
                while len(monkey.items) > 0:
                    monkey.inspect_2(monkeys)

        monkeys_2 = sorted(original_monkeys, key = lambda m : -m.count_inspected)
        print(monkeys_2[0].count_inspected * monkeys_2[1].count_inspected)




       
                


                
            
        