from typing import List

class KnapsackItem:
    """
    Class which models an item contained in a Knapsack or KnapsackCollection. 
    """

    def __init__(self, cost: float, value: float):
        self.cost = cost
        self.value = value

    def __eq__(self, other: KnapsackItem):
        return self.cost == other.cost and self.value == other.value


class KnapsackCollection:
    """
    Class which models a list of all possible items to be added to a knapsack.
    """

    def __init__(self, items: List[KnapsackItem] = []):
        self.items = items

    def add_item(self, cost, val):
        """
        Add a new item to the knapsack.

        :param cost: The cost of the item.
        :param val: The value of the item.
        :return 
        """

        new_item = KnapsackItem(cost, val)
        pointer = 0

        # we want to insert items whilst keeping the order of the list
        # increases search efficiency
        while pointer <= len(self.items):
            if new_item.value < self.items[pointer].value:
                return self.items.insert(pointer, new_item)
            elif new_item.value == self.items[pointer].value:
                if new_item.cost < self.items[pointer].cost:
                    return self.items.insert(pointer, new_item)

            pointer += 1

        return False

    def remove_item(self, pointer=False, cost=False, value=False):
        """
        Remove an item from the knapsack.

        :param pointer: Uses an integer index to remove the item.
        :param cost: Uses the item's cost to remove it. Must be supplied with a value.
        :param value: Uses the item's value to remove it. Must be supplied with a cost.

        :return: True if the item was removed, False otherwise.

        :raises:
            ValueError if the cost is not supplied with a value and vice versa.
            TypeError if the pointer doesn't exist in the knapsack.
        """

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
        """
        Updates a knapsack item via it's integer index.

        :param pointer: The index location of the item in the knapsack.
        :param cost: The new cost of the item to be updated.
        :param value: The new value of the item to be updated.

        :return: True when the item is updated.
        """
        try:
            self.items[pointer] = KnapsackItem(cost, value)
            self.items.sort(key=lambda x: (x.cost, x.value))
            return True

        except TypeError e:
            return False

    def is_sorted(self):
        """
        Determines if the knapsack items are sorted.

        :return: True if the items are sorted in ascending order, False otherwise.
        """

        current_ksi = self.items[0]

        for new_ksi in self.items[1:]:
            cost_check = current_ksi.cost < new_ksi.cost
            cost_check_equal = current_ksi.cost == new_ksi.cost
            val_check = current_ksi.value <= new_ksi.value

            if cost_check is False or (cost_check_equal is True and val_check is False):
                return False

            current_ksi = new_ksi

        return True


class Knapsack:
    """
    Class which models a knapsack.
    """

    def __init__(self, max_cost):
        self.max_cost = max_cost
        self.items = []
        self.current_cost = 0
        self.current_value = 0

    def _update(self):
        self.current_cost = sum(list(map(lambda x: x.cost, self.items)))
        self.current_value = sum(list(map(lambda x: x.value, self.items)))

    def add_item(self, item: KnapsackItem):
        if self.current_cost + item.cost > self.max_cost:
            return False
        else:
            self.items.append(item)
            self._update()
            return True

    def remove_item(self, cost, value):
        for ksi in self.items[:]:
            if ksi.cost == cost and ksi.value == value:
                self.items.remove(ksi)
                self._update()
                return True

        return False

    def replace_item(self, old, new):
        ksi_to_be_replaced = next((x for x in self.items if x.cost == old.cost and x.value == old.value), None)

        if ksi_to_be_replaced is None:
            return False

        # works for both positive negative differences in cost
        if self.current_cost + (old.cost - new.cost) > self.max_cost:
            return False

        self.items.remove(ksi_to_be_replaced)
        self.items.append(new)
        self._update()

        return True
