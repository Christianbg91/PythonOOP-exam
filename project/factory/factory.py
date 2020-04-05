from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        self.capacity -= quantity
        if ingredient_type not in self.ingredients.keys():
            self.ingredients[ingredient_type] = quantity
        else:
            self.ingredients[ingredient_type] += quantity

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        self.ingredients[ingredient_type] -= quantity
        self.capacity += quantity

    def can_add(self, value: int):
        return self.capacity >= value
