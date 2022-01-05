class Table:

    def __init__(self, num_diners):
        self.bill = []
        self.num_diners = num_diners
        self.service_charge_percentage = 0

    def order(self, item, price, quantity=1):
        menu_item = {"item": item, "price": price, "quantity": quantity}
        already_exists = False
        for i in range(len(self.bill)):
            if self.bill[i]["item"] == menu_item["item"] and self.bill[i]["price"] == menu_item["price"]:
                self.bill[i]["quantity"] += menu_item["quantity"]
                already_exists = True

        if not already_exists:
            self.bill.append(menu_item)

    def remove(self, item, price, quantity):
        menu_item = {"item": item, "price": price, "quantity": quantity}

        for i in range(len(self.bill)):
            if self.bill[i]["item"] == menu_item["item"] and self.bill[i]["price"] == menu_item["price"]:
                self.bill[i]["quantity"] -= menu_item["quantity"]

    def get_subtotal(self):
        subtotal = 0

        for item in self.bill:
            subtotal += (item["price"]*item["quantity"])

        return subtotal

    def get_total(self, service_charge_percentage=0.1):

        self.service_charge_percentage = service_charge_percentage

        subtotal = self.get_subtotal()
        subtotal_str = f"£{subtotal:.2f}"

        service_charge = (service_charge_percentage*subtotal)
        service_charge_str = f"£{service_charge:.2f}"

        total = subtotal + service_charge
        total_str = f"£{total:.2f}"

        return {"Sub Total": subtotal_str, "Service Charge": service_charge_str, "Total": total_str}

    def split_bill(self):
        total = float(self.get_total(self.service_charge_percentage)["Total"][1:])
        return float(round(total/self.num_diners, 2))




