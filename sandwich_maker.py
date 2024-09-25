
class SandwichMaker:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:
                print(f"Sorry, out of {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, quantity in order_ingredients.items():
            self.machine_resources[item] -= quantity
