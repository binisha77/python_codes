class Resturant:
    menu = {
        "pizza": 500,
        "burger": 600,
        "pasta": 400,
        "salat": 300
    }

    def __init__(self, customer_name):
        # objects attributes
        self.customer_name = customer_name
        self.order = []
        self.order_summary = {}
        self.discount = 0

        # order process for customer

    def place_order(self, item, quantity):
        if item in Resturant.menu:
            price = Resturant.menu[item] * quantity
            order = (item, quantity, price)
            self.order.append(order)
            print("order placed successfully")


customer1 = Resturant("sovitha")
customer1.place_order("pizza", 5)
print("test")
