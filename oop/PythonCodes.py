class FoodOrder:
    def __init__(self, customer_name, item, price):
        self.customer_name = customer_name
        self.item = item
        self.price = price

    def show_order(self):
        print("customer_Name : {}".format(self.customer_name))
        print("Item : {}".format(self.item))


order1 = FoodOrder("sovitha",  "pizza",100)
order2 = FoodOrder( "sovitha","cheese", 100)
print(order1.customer_name, order1.price, order1.item)
print(order2.customer_name,  order2.item)
order1.show_order()

#