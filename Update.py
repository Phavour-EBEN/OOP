class Restaurant:
    def __init__(self, name, address, cuisine_type):
        self.name = name
        self.address = address
        self.cuisine_type = cuisine_type
        self.menu = {}

    def add_item_to_menu(self, item_name, item_price):
        self.menu[item_name] = item_price

    def remove_item_from_menu(self, item_name):
        self.menu.pop(item_name, None)

    def display_menu(self):
        return "\n".join([f"{item}: ${price}" for item, price in self.menu.items()])


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def display(self):
        return "\n".join([f"{item}: ${price}" for item, price in self.items.items()])


class Customer:
    def __init__(self, name):
        self.name = name
        self.order = {}

    def add_to_order(self, item_name, quantity):
        self.order[item_name] = self.order.get(item_name, 0) + quantity

    def remove_from_order(self, item_name, quantity):
        if item_name in self.order:
            self.order[item_name] = max(0, self.order[item_name] - quantity)

    def view_order(self):
        return "\n".join([f"{item}: {quantity}" for item, quantity in self.order.items()])

    def clear_order(self):
        self.order = {}


def print_receipt(customer, restaurant):
    print("------ Receipt ------")
    print(f"Customer Name: {customer.name}")
    print("Ordered Items:")
    for item, quantity in customer.order.items():
        price = restaurant.menu.get(item, 0)
        total_cost = price * quantity
        print(f"{item} - Quantity: {quantity}, Price: ${price}, Total Cost: ${total_cost}")
    print("------")
    print(f"Restaurant: {restaurant.name}")
    print(f"Address: {restaurant.address}")
    print("Thank you for your order!")
    print("---------------------")


def main():
    restaurant1 = Restaurant("Delicious restaurant", "Accra, Ghana", "Ghanaian Cuisine")
    restaurant1.add_item_to_menu("fufu", 12.99)
    restaurant1.add_item_to_menu("banku", 14.50)
    restaurant1.add_item_to_menu("jollof rice", 18.75)
    restaurant1.add_item_to_menu("kenkey", 10.99)
    restaurant1.add_item_to_menu("waakye", 8.99)
    restaurant1.add_item_to_menu("kelewele", 6.99)

    print("WELLCOME TO DELICIOUS RESTAURANT")
    print("Menu:")
    print(restaurant1.display_menu())

    customer_name = input("Please enter your name: ")
    customer1 = Customer(customer_name)

    while True:
        item_name = input("Enter the item you want to order (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break

        if item_name not in restaurant1.menu:
            print("Item not found in the menu. Please choose a valid item.")
            continue

        try:
            quantity = int(input("Enter the quantity you want to order: "))
            if quantity <= 0:
                print("Please enter a valid quantity (greater than zero).")
                continue
        except ValueError:
            print("Invalid input for quantity. Please enter a number.")
            continue

        customer1.add_to_order(item_name, quantity)

    print("\nCustomer's Order:")
    print(customer1.view_order())

    # Print receipt
    print_receipt(customer1, restaurant1)


if __name__ == "__main__":
    main()
