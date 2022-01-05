from restaurant import Table
from unittest import main

table01 = Table(5)
table01.order("Risotto", 12.50, 2)
print(table01.bill)
table01.order("Burrito", 20.43, 3)
table01.remove("Burrito", 20.43, 2)
print(table01.bill)
print(table01.get_subtotal())
print(table01.get_total(0.15))
print(table01.split_bill())

# Run unit tests automatically
#main(module='test_module', exit=False)

# Run unit tests automatically
#main(module='test_module', exit=False)

# class Table:
#
#     def __init__(self, bill):
#         self.bill = bill =[]
#         self.mu = {"item": "", "price":0.0, "quantity":1}
#
#     def order(self, item:str, price:int, quantity:int=1 ):
#         if self.mu["item"] == item and self.mu["price"] == price:
#             self.mu["quantity"] = quantity
#             self.bill.append(self.mu)
#         else:
#             self.mu["item"] = item
#             self.mu["price"] = price
#             self.mu["quantity"] = quantity
#             self.bill.append(self.mu)
#         #mu = {"item": item, "price": price, "quantity": quantity}
#         return self.bill
#
# table01 = Table(5)
# table01.order("Risotto", 12.50, 2)
# print(table01.mu)