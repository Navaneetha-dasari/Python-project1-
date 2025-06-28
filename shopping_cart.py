class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}  # product_id: quantity
        self.product_list = {}

    def add_product(self, product, qty=1):
        if product.id not in self.product_list:
            self.product_list[product.id] = product
        self.items[product.id] = self.items.get(product.id, 0) + qty
        print(f"{qty} x {product.name} added to cart.")

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Product removed.")
        else:
            print("Product not found in cart.")

    def view_cart(self):
        total = 0
        print("\n🛒 Your Cart:")
        for pid, qty in self.items.items():
            product = self.product_list[pid]
            subtotal = qty * product.price
            print(f"{product.name} x {qty} = ₹{subtotal}")
            total += subtotal
        print(f"Total: ₹{total}")

    def save_to_file(self):
        with open("cart.txt", "w") as f:
            for pid, qty in self.items.items():
                p = self.product_list[pid]
                f.write(f"{p.name},{qty},{p.price}\n")
        print("Cart saved to cart.txt")

# Sample products
p1 = Product(1, "Phone", 9999)
p2 = Product(2, "Laptop", 45999)
p3 = Product(3, "Headphones", 1999)

cart = Cart()
while True:
    print("\n📦 Shopping Cart Menu:")
    print("1. Add Product\n2. View Cart\n3. Remove Product\n4. Save Cart\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Select Product: 1.Phone  2.Laptop  3.Headphones")
        p = input("Enter product number: ")
        if p == '1':
            cart.add_product(p1)
        elif p == '2':
            cart.add_product(p2)
        elif p == '3':
            cart.add_product(p3)
        else:
            print("Invalid choice.")
    elif choice == '2':
        cart.view_cart()
    elif choice == '3':
        pid = int(input("Enter product ID to remove: "))
        cart.remove_product(pid)
    elif choice == '4':
        cart.save_to_file()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option.")