import collections

class Table:

    def __init__(self, people_number):
        self.people = people_number
        self.bill = []

    def search_bill(self, item, price):
        if len(self.bill) != 0:
            for i in range(len(self.bill)):
                if item == self.bill[i]['item'] and price == self.bill[i]['price']:
                    return i
        else:
            return

    def order(self, item, price, quantity = 1):

        order_index = self.search_bill(item, price)
        if order_index is not None:
            self.bill[order_index]['quantity'] += quantity
            return self.bill

        new_order = collections.defaultdict(list)
        new_order['item'] = item
        new_order['price'] = price
        new_order['quantity'] = quantity

        self.bill.append(new_order)
        return self.bill

    def remove(self, item, price, quantity):

        order_index = self.search_bill(item, price)
        if order_index is not None:
            self.bill[order_index]['quantity'] -= quantity

            if self.bill[order_index]['quantity'] <= 0:
                self.bill.remove(order_index)
            return True
        else:
            return False

    def get_subtotal(self):

        subtotal = 0
        for orders in self.bill:
            subtotal = subtotal + (orders['price'] * orders['quantity'])
        return subtotal

    def get_total(self, charge_percentage = 0.10):

        subtotal = self.get_subtotal()
        service_charge = round(subtotal * charge_percentage, 2)
        total = subtotal + service_charge

        subtotal = "£" + str(subtotal)
        service_charge = "£" + str(service_charge)
        total = "£" + str(total)

        invoice = {
            "Sub Total": subtotal,
            "Service Charge": service_charge,
            "Total": total
        }
        return invoice

    def split_bill(self):

        split = round(self.get_subtotal() / self.people, 2)
        return split

