class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] += quantity
                return self.bill
        self.bill.append({"item": item, "price": price, "quantity": quantity})
        return self.bill

    def remove(self, item, price, quantity):
        for order in self.bill:
            if order["item"] == item and order["price"] == price:
                order["quantity"] -= quantity
                if order["quantity"] <= 0:
                    self.bill.remove(order)
                    return True
                return True
            else:
                return False

    def get_subtotal(self):
        sub_total = 0
        for order in self.bill:
            item_total = order["price"] * order["quantity"]
            sub_total += item_total
            sub_total = round(sub_total, 2)
        return sub_total

    def get_total(self, service_charge=0.10):
        sub_total = self.get_subtotal()
        service_cost = sub_total * service_charge
        total = sub_total + service_cost
        sub_total = "£{:.2f}".format(sub_total)
        service_cost = "£{:.2f}".format(service_cost)
        total = "£{:.2f}".format(total)
        total_breakdown = {"Sub Total": sub_total, "Service Charge": service_cost, "Total": total}
        return total_breakdown

    def split_bill(self):
        sub_total = self.get_subtotal()
        split = round(sub_total / self.diners, 2)
        return split


# table02 = Table(2)
#
# table02.order("Pizza", 15.99, 1)
# table02.order("Pasta", 11.20, 2)
# table02.order("Pizza", 15.99, 3)
# table02.order("Pasta", 11.20, 4)
# print(table02.bill)
# table02.remove("Pizza", 15.99, 3)
# print(table02.remove("Cake", 15.99, 4))
# print(table02.bill)
# print(table02.get_subtotal())
# print(table02.get_total(0.2))
# print(table02.split_bill())