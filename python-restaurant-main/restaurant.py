class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item, price, quantity=1):
        orders = {'item': item, 'price': price, 'quantity': quantity}
        Flag = True
        for items in self.bill:
            if orders['item'] == items['item'] and orders['price'] == items['price']:
                items['quantity'] += orders['quantity']
                Flag = False
        if Flag:
            self.bill.append(orders)

    def remove(self, item, price, quantity=1):
        orders = {'item': item, 'price': price, 'quantity': quantity}
        Flag = False
        for items in self.bill:
            if orders['item'] == items['item'] and orders['price'] == items['price']:
                if items['quantity'] - orders['quantity'] <0:
                    break
                elif items['quantity'] - orders['quantity'] == 0:
                    del items
                    Flag = True
                    break
                else:
                    items['quantity'] -= orders['quantity']
                    Flag = True
                    break
        if not Flag:
            return False
        else:
            return True

    def get_subtotal(self):
        subtotal = 0
        for each in self.bill:
            subtotal += each['price']*each['quantity']
        return subtotal

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        service_charge_amount = subtotal*service_charge
        total = subtotal + service_charge_amount
        return {"Sub Total": "£" + str(format(float(subtotal), '.2f')),
                "Service Charge": "£" + str(format(float(service_charge_amount), '.2f')),
                "Total": "£" + str(format(float(total), '.2f'))}

    def split_bill(self):
        subtotal = self.get_subtotal()
        split_amount = round(float(subtotal/self.diners), 2)
        return split_amount