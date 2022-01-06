class Table:

    def __init__(self, numOfPeople):
        self.bill = []
        self.numOfPeople = numOfPeople
        self.cost = []
        self.billDict = {}
        self.costPounds = []
        self.costDict = {}

# {"item": "apple", "price": 2, "quantity": 3}
    def order(self, item, price, quantity = 1):
        for x in self.bill:
            if x["item"] == item and x["price"] == price: # Increase quantity of existing item
                x["quantity"] += quantity
                return True
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for x in self.bill: # Remove quantity of existing item
            if x["item"] == item and x["price"] == price and quantity <= x["quantity"]:
                x["quantity"] -= quantity
                if x["quantity"] == 0:
                    self.bill.remove(x)
                return True
        return False

    def get_subtotal(self):
        self.subtotal = 0
        for i in self.bill:
            self.subtotal += i["quantity"]*i["price"]
        return self.subtotal


    def get_total(self, serviceCharge = 0.1):
        subtotal = self.get_subtotal()
        subtotal_2dp = float(format(subtotal, '.2f'))
        subtotal_str = "£" + format(subtotal, '.2f')
        service_charge = subtotal_2dp*serviceCharge
        service_charge_2dp = float(format(service_charge, '.2f'))
        service_str = "£" + format(service_charge, '.2f')
        return {"Sub Total": subtotal_str, "Service Charge": service_str,
                "Total": "£"+ str(subtotal_2dp+service_charge_2dp)}

    def split_bill(self):
        return self.get_subtotal()/self.numOfPeople


table2 = Table(2)
table2.order("chips", 2, 4)
table2.order("fish", 7, 2)
table2.get_subtotal()
table2.get_total()
table2.split_bill()