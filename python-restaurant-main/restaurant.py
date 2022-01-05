class Table:

    def __init__(self, people):
        self.bill = []
        self.people = people

    def order(self, item:str, price:int, quantity:int=1 ):
        menu = {"item": item, "price": price, "quantity": quantity}
        if not self.bill:
            self.bill.append(menu)
        else:
            for item in self.bill:
                exist = False
                # lets check if items already exisit
                if menu["item"] == item['item'] and menu["price"] == item['price']:
                    item['quantity'] += menu['quantity']
                    exist = True
                if exist:
                    break
                else:
                    self.bill.append(menu)

        return self.bill

    def remove(self, item, price, quantity=1):
        menu = {"item": item, "price": price, "quantity": quantity}
        check = False
        for item in self.bill:
            if item["item"] == menu['item'] and item["price"] == menu['price']:
                if ((item['quantity'] - menu["quantity"]) <= 0):
                    del item
                    check = False
                    break # lets come out.
                else:
                    item['quantity'] -= menu["quantity"] # otherwise remove quantity
                    check = True
        return check

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



