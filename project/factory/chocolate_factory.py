from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name=name, capacity=capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in ChocolateFactory")
        super().add_ingredient(ingredient_type, quantity)

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")
        super().remove_ingredient(ingredient_type, quantity)

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")
        for ingredient, quantity in self.recipes[recipe_name].items():
            self.remove_ingredient(ingredient, quantity)
        if recipe_name in self.products.keys():
            self.products[recipe_name] += 1
        else:
            self.products[recipe_name] = 1
