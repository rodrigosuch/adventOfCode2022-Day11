import math


class Monkey:

    def __init__(self, listItems, operation, arg, division, trueMonkey, falsemonkey):
        self.listItems = listItems
        self.operation = operation
        self.arg = arg
        self.trueMonkey = trueMonkey
        self.falseMonkey = falsemonkey
        self.division = division
        self.inspected_items = 0

    def add_item(self, item):
        self.listItems.append(item)

    def get_inspected_items(self):
        return self.inspected_items

    def run_cycle(self):
        result = []
        for item in self.listItems:
            self.inspected_items += 1
            if self.operation == "*":
                item *= self.arg
            elif self.operation == "+":
                item += self.arg
            elif self.operation == "^":
                item = math.pow(item, self.arg)

            item = int(item/3)
            if item % self.division == 0:
                result.append((item, self.trueMonkey))
            else:
                result.append((item, self.falseMonkey))

        self.listItems.clear()
        return result
