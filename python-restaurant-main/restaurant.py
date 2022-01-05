class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item, price, quantity = 1):
        o = {"item": item, "price": price, "quantity": quantity}
        j = 0
        for i in self.bill:
            if o["item"] == i["item"] and o["price"] == i["price"]:
                i["quantity"] += o["quantity"]
                break
            else:
                j += 1

        if j == len(self.bill):
            self.bill.append(o)

    def remove(self, item, price, quantity=1):
        o = {"item": item, "price": price, "quantity": quantity}
        j = 0
        for i in self.bill:
            if o["item"] == i["item"] and o["price"] == i["price"]:
                if o["quantity"] > i["quantity"]:
                    return False
                else:
                    i["quantity"] -= o["quantity"]
                    break
            else:
                j += 1

        if j == len(self.bill):

            return False

        for i in self.bill:
            if i["quantity"] == 0:
                self.bill.remove(i)

        return True

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += (i["price"] * i["quantity"])
        subtotal = round(subtotal, 2)

        return subtotal

    def get_total(self, discount = 0.1):
        total = {
            "Sub Total" : f"£{format(self.get_subtotal(), ',.2f')}",
            "Service Charge" : f"£{format(self.get_subtotal() * discount, ',.2f')}",
            "Total" : f"£{format(self.get_subtotal() * (1 + discount), ',.2f')}"
        }
        return total

    def split_bill(self):
        split = round(self.get_subtotal() / self.diners, 2)

        return split