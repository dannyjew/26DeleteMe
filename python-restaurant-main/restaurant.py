import math
class Table:
    def __init__(self,no_diners):
        self.no_diners = no_diners
        self.bill = []

    def order(self,item, price, quantity=1):
        '''Adds any new order to the bill.
                If a quantity is not provided, it will default to 1
                if the item is already in the bill it will increase quantity instead of adding it again'''
        for i in self.bill:
            if i["item"] == item:
                i["quantity"]+=quantity
                return
        self.bill.append({"item":item, "price":price, "quantity":quantity})
        return

    def remove(self,item, price, quantity=1): #Price is redundant, but included so test_module works
        '''Removes any amount of items from the bill
                If quantity is not provided, it will default to 1
                If new quantity is below 0 it will be removed from the bill
                Returns True if item is on bill after process, False otherwise'''
        for i in range(len(self.bill)):
            if self.bill[i]["item"]==item:
                self.bill[i]["quantity"]-=quantity
                if self.bill[i]["quantity"]<=0:
                    self.bill.pop(i)
                    return(False)
                return(True)
        return(False)

    def get_subtotal(self):
        '''Returns the sum total of all items on the bill'''
        subtotal = 0
        for item in self.bill:
            subtotal += item["quantity"]*item["price"]
        return(subtotal)

    def format_as_price(self,value):
        '''Returns any value formatted as British Sterling'''
        value = "£"+str(round(value,2))
        if value.index('.')>=len(value)-2:
            value+='0'
        return(value)

    def get_total(self, tip=0.1):
        '''Returns a dictionary containing information about the bill'''
        sub_total = Table.get_subtotal(self)
        bill = {"Sub Total":"", "Service Charge":"", "Total": ""}
        bill["Sub Total"] = Table.format_as_price(self,sub_total) #Cost of items on bill
        bill["Service Charge"] = Table.format_as_price(self,sub_total*tip) #Cost of tip
        bill["Total"] = Table.format_as_price(self,sub_total*(1+tip)) #Total cost
        return(bill)

    def split_bill(self):
        '''Returns a float showing the cost per diner of the items on the bill'''
        cost_per_diner = Table.get_subtotal(self) / self.no_diners
        cost_per_diner = round(cost_per_diner,5) #To remove very small float pieces that cause errors

        if cost_per_diner - round(cost_per_diner,2) > 0: #Ensures values are always rounded up.
            cost_per_diner += 0.005

        cost_per_diner = round(cost_per_diner,2)
        return(cost_per_diner)
    pass