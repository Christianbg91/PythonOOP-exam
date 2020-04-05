from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name=name, capacity=capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type not in ["white", "yellow", "blue", "green", "red"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in PaintFactory")
        super().add_ingredient(ingredient_type, quantity)

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError('No such ingredient in the factory')
        if quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")
        super().remove_ingredient(ingredient_type, quantity)

    @property
    def products(self):
        return self.ingredients


