import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


def print_report(machine_resources):
    """Print current resource values"""
    print(f"Bread: {machine_resources['bread']} slices")
    print(f"Ham: {machine_resources['ham']} slices")
    print(f"Cheese: {machine_resources['cheese']} ounces")

def main():
    # Make an instance of other classes
    resources = data.resources
    recipes = data.recipes
    sandwich_maker_instance = SandwichMaker(resources)
    cashier_instance = Cashier()

    while True:
        choice = input("Choose Options (small / medium / large / off / report): ").lower()

        if choice == "off":
            print("Turning machine off")
            break
        elif choice == "report":
            print_report(sandwich_maker_instance.machine_resources)
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print("Please insert money.")
                total_amount = cashier_instance.process_coins()
                if cashier_instance.transaction_result(total_amount, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
                    print(f"Your {choice} sandwich is ready. BON APPETIT!")
        else:
            print("Try Order again.")

if __name__ == "__main__":
    main()


