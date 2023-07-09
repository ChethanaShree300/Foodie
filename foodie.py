class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

def show_restaurants(restaurants):
    print("Available Restaurants:")
    for i, restaurant in enumerate(restaurants):
        print(f"{i + 1}. {restaurant.name}")

def show_menu(restaurant):
    print(f"\nMenu for {restaurant.name}:")
    for i, item in enumerate(restaurant.menu):
        print(f"{i + 1}. {item.name} - ${item.price}")

def login(users):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def signup(users):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = User(name, email, password)
    users.append(user)
    print("Sign up successful!")

def add_restaurant(restaurants):
    name = input("Enter the restaurant name: ")
    menu = []

    while True:
        item_name = input("Enter the food item name (or 'q' to stop): ")
        if item_name == 'q':
            break
        item_price = float(input("Enter the price for this item: "))
        item = FoodItem(item_name, item_price)
        menu.append(item)

    restaurant = Restaurant(name, menu)
    restaurants.append(restaurant)
    print("Restaurant added successfully!")

def show_cart(cart):
    print("Items in your cart:")
    for i, item in enumerate(cart.items):
        print(f"{i + 1}. {item.name} - ${item.price}")

def place_order(user, cart):
    if user:
        if len(cart.items) == 0:
            print("Your cart is empty!")
            return

        print("Order Details:")
        show_cart(cart)
        total = cart.calculate_total()
        print(f"Total: ${total}")

        confirm = input("Confirm your order (y/n): ")
        if confirm.lower() == 'y':
            print("Order placed successfully!")
            cart.items = []  # Clear the cart after placing the order
        else:
            print("Order cancelled.")
    else:
        print("Please log in first.")


def main():
    users = []
    restaurants = []
    cart = Cart()
    user=None

    while True:
        print("\nWelcome to the Food Delivery App!")
        print("1. Login")
        print("2. Sign up")
        print("3. Add Restaurant")
        print("4. List Restaurants")
        print("5. Show Menu")
        print("6. Add Item to Cart")
        print("7. Show Cart")
        print("8. Place Order")
        print("9. Remove item from Cart")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = login(users)
            if user:
                print(f"Welcome, {user.name}!")
            else:
                print("Login failed! Invalid email or password.")
        elif choice == '2':
            signup(users)
        elif choice == '3':
            add_restaurant(restaurants)
        elif choice == '4':
            show_restaurants(restaurants)
        elif choice == '5':
            restaurant_index = int(input("Enter the restaurant index: ")) - 1
            if restaurant_index >= 0 and restaurant_index < len(restaurants):
                show_menu(restaurants[restaurant_index])
            else:
                print("Invalid restaurant index!")
        elif choice == '6':
            restaurant_index = int(input("Enter the restaurant index: ")) - 1
            if restaurant_index >= 0 and restaurant_index < len(restaurants):
                item_index = int(input("Enter the item index: ")) - 1
                if item_index >= 0 and item_index < len(restaurants[restaurant_index].menu):
                    item = restaurants[restaurant_index].menu[item_index]
                    cart.add_item(item)
                    print(f"{item.name} added to cart.")
                else:
                    print("Invalid item index!")
            else:
                print("Invalid restaurant index!")
        elif choice == '7':
            show_cart(cart)
        elif choice == '8':
            place_order(user, cart) if user else print("Please log in first.")
        elif choice == '9':
            restaurant_index = int(input("Enter the restaurant index: ")) - 1
            if restaurant_index >= 0 and restaurant_index < len(restaurants):
                item_index = int(input("Enter the item index: ")) - 1
                if item_index >= 0 and item_index < len(restaurants[restaurant_index].menu):
                    item = restaurants[restaurant_index].menu[item_index]
                    cart.remove_item(item)
                    print(f"{item.name} removed from the cart.")
                else:
                    print("Invalid item index!")
            else:
                print("Invalid restaurant index!")
        elif choice == '10':
            print("Thank you for using the Food Delivery App!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()