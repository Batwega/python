class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity_in_stock}\n")


class ShoppingCart:
    total_carts = 0  

    def __init__(self):
        self.items = []  
        ShoppingCart.total_carts += 1  

    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Sorry, not enough {product.product_name} in stock.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0].product_name == product.product_name:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  
                print(f"Removed {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart Items:")
            for product, quantity in self.items:
                print(f"{product.product_name} - Quantity: {quantity} - Price: ${product.price:.2f}")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total



product1 = Product("smart tv,s", 1200.00, 5)
product2 = Product("Smartphone", 800.00, 10)
product3 = Product("home studio speakers", 150.00, 20)


product1.display_product_info()
product2.display_product_info()
product3.display_product_info()


cart1 = ShoppingCart()
cart2 = ShoppingCart()


cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart1.add_to_cart(product3, 3)


cart2.add_to_cart(product2, 2)
cart2.add_to_cart(product3, 5)
cart2.add_to_cart(product1, 1)


print("\n--- Cart 1 ---")
cart1.display_cart()
print(f"Total Amount Due: ${cart1.calculate_total():.2f}")

print("\n--- Cart 2 ---")
cart2.display_cart()
print(f"Total Amount Due: ${cart2.calculate_total():.2f}")


cart1.remove_from_cart(product2)


print("\n--- Cart 1 After Removal ---")
cart1.display_cart()
print(f"Total Amount Due: ${cart1.calculate_total():.2f}")


print(f"\nTotal Shopping Carts Created: {ShoppingCart.total_carts}")





