from typing import List

class KnapsackItem:
    def __init__(self, cost: float, value: float):
        self.cost = cost
        self.value = value

    def __eq__(self, other: KnapsackItem):
        return self.cost == other.cost and self.value == other.value


class Knapsack:
    def __init__(self, items: List[KnapsackItem] = []):
        self.items = items

    def add_item(self, cost, val):
        new_item = KnapsackItem(cost, val)
        pointer = 0

        while pointer <= len(self.items):
            if new_item.value < self.items[pointer].value:
                self.items.insert(pointer, new_item)
                break
            elif new_item.value == self.items[pointer].value:
                if new_item.cost < self.items[pointer].cost:
                    self.items.insert(pointer, new_item)
                    break

            pointer += 1

        #self.items.append(item)
