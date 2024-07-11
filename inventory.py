class GroceryInventory:
    def __init__(self, apples, bananas, oranges):
        self.inventory = {
            "a": apples,
            "b": bananas,
            "o": oranges
        }

    def purchase(self, item, amount=1):
        if item not in self.inventory:
            raise ValueError("Invalid item type.")
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        if self.inventory[item] < amount:
            raise ValueError(f"Not enough stock of the selected item. Current quantity: {self.inventory[item]}")
        self.inventory[item] -= amount

    def restock(self, item, amount):
        if item not in self.inventory:
            raise ValueError("Invalid item type.")
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self.inventory[item] += amount

    def __str__(self):
        return (f"Apples: {self.inventory['a']}\n"
                f"Bananas: {self.inventory['b']}\n"
                f"Oranges: {self.inventory['o']}")

def main():
    apples = int(input("Enter the initial number of apples: "))
    bananas = int(input("Enter the initial number of bananas: "))
    oranges = int(input("Enter the initial number of oranges: "))
    inventory = GroceryInventory(apples, bananas, oranges)

    while True:
        command = input("Enter command (p for purchase, r for restock, pr for print, q for quit): ")

        if command == 'q':
            break
        elif command in ("p", "r"):
            item = input("Enter item type (a for apples, b for bananas, o for oranges): ").lower()
            if item not in inventory.inventory:
                print("Invalid item type.")
                continue
            try:
                amount = int(input(f"Enter amount to {'buy' if command == 'p' else 'restock'}: "))
                if command == "p":
                    inventory.purchase(item, amount)
                else:
                    inventory.restock(item, amount)
            except ValueError as e:
                print(e)
        elif command == "pr":
            print(inventory)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
