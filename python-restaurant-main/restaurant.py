class Table:
    def __init__(self, n):
        self.people = int(n)
        self.bill = []

    def order(self, item, price, new_quantity=1):
        #self.menu = {'item':item, 'price':price, 'quantity':quantity}
        for i in self.bill:
            if i['item'] == item:
                i['quantity'] += new_quantity
                return True
        self.bill.append(
            {'item': item, 'price': price, 'quantity': new_quantity})

    def remove(self, item, price, new_quantity=1):
        for i in self.bill:
            if i['item'] == item and i['price'] == price:
                i['quantity'] -= new_quantity
                return True
            elif i['quantity'] == 0:
                self.bill.remove(
                    {'item': item, 'price': price, 'quantity': new_quantity})
                return True
            elif i['item'] != item:
                return False

    def get_subtotal(self):
        subtotal = 0
        for i in self.bill:
            subtotal += i['price']*i['quantity']
        return subtotal

    def get_total(self, service: float(0.10)):
        sub_total = self.get_subtotal()
        service_charge = sub_total * service
        total = sub_total + service_charge
        return {'Sub Total': f'£{sub_total:02,.2f}', 'Service Charge': f'£{service_charge:02,.2f}', 'Total': f'£{total:02,.2f}'}

    def split_bill(self):
        sub_total = self.get_subtotal()
        split = float(sub_total/self.people)
        return split
