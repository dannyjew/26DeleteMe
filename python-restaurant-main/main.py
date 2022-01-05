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


# table05 = Table(5)
# table05.order('Food1', 10.00, 3)
# table05.order('Food2', 20.00, 1)
# table05.order('Food3', 0.60, 1)
# actual = table05.get_total(0.15)


# table06 = Table(6)
# table06.order('Food1', 20.00, 3)
# table06.order('Food2', 10.00, 1)
# table06.order('Food3', 3.20, 1)
# actual2 = table06.split_bill()



# Run unit tests automatically
main(module='test_module', exit=False)