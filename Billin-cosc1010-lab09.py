# Kaden Billin
# UWYO COSC 1010
# 11-17-2024
# Lab 09
# Lab Section: 12
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:
    def __init__(self, size, sauce='red'):
        if size < 10:
            self.size = 10
        else:
            self.size = size
        self.sauce = sauce
        self.toppings = ['cheese']

    def get_size(self):
        return self.size

    def set_size(self, newsize):
        if newsize < 10:
            self.size = 10
        else:
            self.size = newsize

    def get_sauce(self):
        return self.sauce

    def get_toppings(self):
        return self.toppings

    def add_toppings(self, *newtoppings):
        self.toppings.extend(newtoppings)

    def count_toppings(self):
        return len(self.toppings) - 1

    

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def placeOrder(self):
        print("\nNew Pizza Order:")
        try:
            size = int(input("Enter pizza size: "))
        except ValueError:
            print("Invalid input. Using 10 inches.")
            size = 10

        if size < 10:
            print("Size too small. Using 10 inches.")
            size = 10

        sauce = input("Enter sauce (press Enter to default to red): ")
        sauce = sauce if sauce else 'red'

        print("Enter toppings one at a time. Press Enter when done.")
        toppings = []
        while True:
            topping = input("Add topping: ")
            if not topping:
                break
            toppings.append(topping)

        pizza = Pizza(size, sauce)
        pizza.add_toppings(*toppings)
        self.pizzas.append(pizza)
        self.orders += 1
        print("Order placed!")

    def getPrice(self, pizza):
        size_price = pizza.get_size() * Pizzeria.price_per_inch
        toppings_price = pizza.count_toppings() * Pizzeria.price_per_topping
        return size_price + toppings_price

    def getReceipt(self):
        if not self.pizzas:
            print("No pizzas have been ordered yet.")
            return

        pizza = self.pizzas[-1]
        size_price = pizza.get_size() * Pizzeria.price_per_inch
        toppings_price = pizza.count_toppings() * Pizzeria.price_per_topping
        total_price = size_price + toppings_price

        print("\n--- Receipt ---")
        print(f"Size: {pizza.get_size()} inches - ${size_price}")
        print(f"Sauce: {pizza.get_sauce()}")
        print(f"Toppings ({pizza.count_toppings()}): {', '.join(pizza.get_toppings()[1:])} - ${toppings_price}")
        print(f"Total Price: ${total_price}")
        print("----------------\n")

    def getNumberOfOrders(self):
        return self.orders


if __name__ == "__main__":
    my_pizzeria = Pizzeria()
    while True:
        action = input("Order a pizza? Type 'exit' to cancel: ").strip().lower()
        if action == 'exit':
            break
        elif action == 'yes':
            my_pizzeria.placeOrder()
            my_pizzeria.getReceipt()
        else:
            print("Invalid choice.")

    print(f"\nTotal pizzas ordered: {my_pizzeria.getNumberOfOrders()}")

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""