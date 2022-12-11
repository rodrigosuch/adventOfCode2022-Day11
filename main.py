from monkey import Monkey

monkey0 = Monkey([56, 56, 92, 65, 71, 61, 79], "*", 7, 3, 3, 7)
monkey1 = Monkey([61, 85], "+", 5, 11, 6, 4)
monkey2 = Monkey([54, 96, 82, 78, 69], "^", 2, 7, 0, 7)
monkey3 = Monkey([57, 59, 65, 95], "+", 4, 2, 5, 1)
monkey4 = Monkey([62, 67, 80], "*", 17, 19, 2, 6)
monkey5 = Monkey([91], "+", 7, 5, 1, 4)
monkey6 = Monkey([79, 83, 64, 52, 77, 56, 63, 92], "+", 6, 17, 2, 0)
monkey7 = Monkey([50, 97, 76, 96, 80, 56], "+", 3, 13, 3, 5)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
for round in range(1, 21):
    for monkey in monkeys:
        result = monkey.run_cycle()
        for item in result:
            monkeys[item[1]].add_item(item[0])
#    print(f"Round {round}---- ")
#    for monkey in monkeys:
#        print(monkey.listItems)

for monkey in monkeys:
    print(monkey.get_inspected_items())