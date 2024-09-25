class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("how many dollar bill(s)?: "))
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))

        total = (dollars * 1.0) + (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            if coins > cost:
                change = round(coins - cost, 2)
                print(f"Here is your ${change} change back")
            return True
        else:
            print(f"Not enough money, returning money")
            return False

