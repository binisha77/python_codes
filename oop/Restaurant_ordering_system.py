class Restaurant:

    menu = {
        "pizza":500,
        "Burger":200,
        "Pasta": 300,
        "Salad":150,
        "Ice Cream": 100
    }

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.orders = []
        self.order_summary = {}
        self.discount = 0

    def place_order(self, item, quantity):
     if item in Restaurant.menu:
         price = Restaurant.menu[item] * quantity
         order = (item,quantity,price)
         self.orders.append(order)
         self.order_summary[item] = self.order_summary.get(item, 0) + quantity
         print(f"{self.customer_name} ordered {quantity} x {item}")
     else:
      print(f"Sorry, {item} is not available in the menu.")

    def apply_discount(self, percent):
        self.discount = percent
        print(f"A discount of {percent}% has been applied for {self.customer_name}")

    def calculate_total(self):
        total_func = lambda order: order[2]  # Lambda function to get price
        total = sum(total_func(order) for order in self.orders)  # Loop + sum
        if self.discount > 0:
            total = total - (total * self.discount / 100)  # Apply discount
        return total

    def unique_items_ordered(self):
        return set(item[0] for item in self.orders)

    def show_summary(self):
        print("\n------ Order Summary for", self.customer_name, "------")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):", self.unique_items_ordered())
        print("Discount applied:", self.discount, "%")
        print("Total bill after discount:", self.calculate_total(), "INR")
        print("--------------------------------------\n")

        customer1 = Restaurant("sovitha ")
        customer2 = Restaurant("binisha")
        # Place orders

        customer1.place_order("Pizza", 2)
        customer1.place_order("Burger", 3)
        customer1.place_order("Salad", 1)
        customer1.apply_discount(10)  # Apply 10% discount

        customer2.place_order("Pasta", 2)
        customer2.place_order("Pizza", 1)
        customer2.place_order("Ice Cream", 2)
        customer2.apply_discount(5)  # Apply 5% discount

        # Show summaries
        customer1.show_summary()
        customer2.show_summary()

