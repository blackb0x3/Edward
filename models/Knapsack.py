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

        # we want to insert items whilst keeping the order of the list
        # increases search efficiency
        while pointer <= len(self.items):
            if new_item.value < self.items[pointer].value:
                self.items.insert(pointer, new_item)
                break
            elif new_item.value == self.items[pointer].value:
                if new_item.cost < self.items[pointer].cost:
                    self.items.insert(pointer, new_item)
                    break

            pointer += 1

    def remove_item(self, pointer=False, cost=False, value=False):
        if pointer is not False:
            return self.items.pop(pointer) if pointer is not False and pointer < len(self.items) else False

        elif pointer is False
                and cost is not False
                and value is not False:
            for ksi in self.items[:]:
                if ksi.cost == cost and ksi.value == value:
                    return self.items.remove(ksi)

        else:
            raise ValueError("You must supply either a pointer or a cost and value.")

    def update_item(self, pointer, cost, value):
        return self.items[pointer] = KnapsackItem(cost, value)
