# A class representing a restaurant
class Table:

    # Initialize the table
    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []

    # Get the order and add to bill
    def order(self, item, price, quantity = 1):
        self.item = item
        self.price = round(price, 3)
        self.quantity = quantity
        for i in self.bill:
            if self.item == i['item'] and self.price == i['price']:
                i['quantity'] += self.quantity
                return self.bill
        self.bill.append({"item": self.item, "price": self.price, "quantity": self.quantity})
        return self.bill

    # Remove order from bill
    def remove(self, item, price, quantity = 1):
        self.item = item
        self.price = float(price)
        self.quantity = quantity
        for i in self.bill:
            if self.item == i['item'] and self.price == i['price']:
                i['quantity'] -= self.quantity
                if i['quantity'] == 0:
                    self.bill.pop()
                return True
        self.bill.append({"item": self.item, "price": self.price, "quantity": self.quantity})
        return False

    # Get total cost of bill on table
    def get_subtotal(self):
        tot = 0.00
        for i in self.bill:
            cost = i['price'] * i['quantity']
            tot = tot + cost
        return tot


    # Get total plus service charge
    def get_total(self, service_charge = 0.10):
        self.service_charge = service_charge * float(self.get_subtotal())
        return {"Sub Total": "£" + str(self.get_subtotal()),
                "Service Charge":"£" + str(self.service_charge),
                "Total": "£" + str(self.service_charge + float(self.get_subtotal()))}

    def split_bill(self):
        tot = 0
        for i in self.bill:
            cost = i['price'] * i['quantity']
            tot = tot + cost
        return round(tot / float(self.number_of_people),2)

# Create a table for sengo with details required
sengo = Table(6)


print(sengo.order('Food1', 10.00, 3))
print(sengo.order('Food2', 20.00, 1))
print(sengo.order('Food3', 0.60, 1))
print(sengo.get_total(0.15))
