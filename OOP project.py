class ProductType:
    def __init__(self, type_id, type_name):
        self.type_id = type_id
        self.type_name = type_name

class Brand:
    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name

class Product:
    def __init__(self, product_id, product_name, price, product_type, brand):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_type = product_type
        self.brand = brand

class Stock:
    def __init__(self, stock_id, stock_quantitity, product):
        self.stock_id = stock_id
        self.stock_quantity = stock_quantitity
        self.product = product

    def set_stock_quantity(self, quantity):
        self.stock_quantity = quantity1

class Inventory:
    def __init__(self, inventory_id, location):
        self.inventory_id = inventory_id
        self.location = location
        self.stocks = []

    def add_stock(self, item):
        self.stocks.append(item)

    def remove_stock(self, item):
        self.stocks.remove(item)

    def check_stock(self):
        for stock in self.stocks:
            print(f"Stock ID: {stock.stock_id}")
            print(f"Quantity in Stock: {stock.stock_quantity}")
            print(f"Product ID: {stock.product.product_id}")
            print(f"Product Name: {stock.product.product_name}")
            print(f"Price: {stock.product.price}")
            print(f"Product Type: {stock.product.product_type.type_name}")
            print(f"Brand: {stock.product.brand.brand_name}")
            print("______")

inventory = Inventory(1, "Main Warehouse")

while True:
    print("\nMenu:")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Check Stock")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        product_type = input("Enter product type (i.e., Electronics, Phones, Utensils, etc.): ")
        brand_name = input("Enter brand name: ")
        product_name = input("Enter product name (i.e., toothbrush, phone, mouse, etc.): ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product_type_obj = ProductType(len(inventory.stocks) + 1, product_type)
        brand_obj = Brand(len(inventory.stocks) + 1, brand_name)
        product_obj = Product(len(inventory.stocks) + 1, product_name, price, product_type_obj, brand_obj)
        stock_item = Stock(len(inventory.stocks) + 1, quantity, product_obj)
        inventory.add_stock(stock_item)
        print("Stock added successfully.")

    elif choice == "2":
        stock_id = int(input("Enter the Stock ID you want to remove: "))
        for stock in inventory.stocks:
            if stock.stock_id == stock_id:
                inventory.remove_stock(stock)
                print(f"Stock ID {stock_id} removed.")
                break
            else:
                print(f"Stock ID {stock_id} not found in inventory.")

    elif choice == "3":
        inventory.check_stock()
    
    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")