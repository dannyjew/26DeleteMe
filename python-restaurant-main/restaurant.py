class Table:

    def __init__(self, people):
        self.bill = []
        self.people = people


    def order(self, item, price, quantity=1):

        for items in self.bill:
            if items['item'] == item and items['price'] == price:
                items['quantity'] += quantity
                return True
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

        #return self.bill

    def remove(self, item, price, new_quantity=1):
        for items in self.bill:
            if items['item'] == item and items['price'] == price:
                items['quantity'] -= new_quantity
                return True
            elif items['quantity'] == 0:
                self.bill.remove({'item':item, 'price':price, 'quantity':new_quantity})
                return True
            elif items['item'] != item:
                return False

    def get_subtotal(self):
        sub_total = 0
        for element in self.bill:
            sub_total += element['price'] *element['quantity']
        return sub_total

    def get_total(self, s:float=0.10):
        sub_total = self.get_subtotal()
        service_charge = sub_total * s
        total = sub_total + service_charge
        return {"Sub Total":f"£{sub_total:02,.2f}", "Service Charge": f"£{service_charge:02,.2f}", "Total": f"£{total:02,.2f}"}

    def split_bill(self):
        sub_total = self.get_subtotal()
        split = float(sub_total/self.people)

        return split



