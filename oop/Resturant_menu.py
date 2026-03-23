class Resturant:
    # class variable
    menu ={
        "pizza" :500,
        "burger":600,
        "pasta": 400,
        "salat": 300
    }

    def __init__(self, customer_name):
        # objects attributes
        self.customer_name = customer_name
        self.order =[]
        self.order_summary ={}
        self.discount =0

        # order process for customer
    def place_order(self,item,quantity):
      if item in Resturant.menu:
         price = Resturant.menu[item] * quantity
         order =(item,quantity,price)
         self.order.append(order)
         self.order_summary[item] = self.order_summary[item] + 1
         print("order placed successfully")


    def show_summary(self):
        print(" order summary")
        print(self.order_summary)
customer1 = Resturant("sovitha")
customer1.place_order("pizza",5)
print("test")


