class Table:

    def __init__(self, table, numOfPeople):
        self.bill = []
        self.table = table
        self.numOfPeople = numOfPeople
        self.subtotal = 0
        self.cost = []
        self.billDict = {}
        self.costPounds = []
        self.costDict = {}

    def order(self, item, price, quantity = 1):
        for x in range(len(self.bill)):

            if item in self.bill[x]: # Increase quantity of existing item
                self.bill[x][2] = self.bill[x][2] + quantity
                for x in range(len(self.bill)):  # Convert list to dictionary
                    labels = ["item", "price", "quantity"]
                    self.billDict[x] = dict(zip(labels, self.bill[x]))
                print("Bill:", self.billDict)
                return self.bill, self.billDict
        a = [] # Add new item to bill
        a.append(item)
        a.append(price)
        a.append(quantity)
        self.bill.append(a)

        for x in range(len(self.bill)): # Convert list to dictionary
            billLabels = ["item", "price", "quantity"]
            self.billDict[x] = dict(zip(billLabels, self.bill[x]))
        print("Bill:", self.billDict)

        return self.bill, self.billDict

    def remove(self, item, price, quantity=1):
        for x in range(len(self.bill)): # Remove quantity of existing item
            if item in self.bill[x]:
                self.bill[x][1] = self.bill[x][1] - price
                self.bill[x][2] = self.bill[x][2] - quantity
                if self.bill[x][2] == 0: # Remove item if quantity is zero
                    self.bill.remove(self.bill[x])
                print(self.bill)
                return self.bill

        return self.bill

    def get_subtotal(self):
        for x in range(len(self.bill)):
            subtotal = 0
            subtotal = self.bill[x][1] * self.bill[x][2] + subtotal
            self.subtotal = self.subtotal + subtotal
        return self.subtotal

    def get_total(self, serviceCharge = 0.1):
        self.cost.append(self.subtotal)
        self.cost.append(self.subtotal * serviceCharge)
        self.cost.append(self.subtotal + self.subtotal * serviceCharge)  # Total

        for x in range(len(self.cost)): # Convert floats to currency
            self.costPounds.append("£{:,.2f}".format(self.cost[x]))

        costLabels = ["Subtotal", "Service Charge", "Total"] # Convert list to dictionary
        self.costDict = dict(zip(costLabels, self.costPounds))
        print("Cost:", self.costDict)

        return self.cost, self.costDict

    def split_bill(self):
        costPerPerson = "£{:,.2f}".format(self.cost[2] / self.numOfPeople)
        print(costPerPerson, "Per Person")
        return costPerPerson


table2 = Table(2, 9)
table2.order("chips", 2, 4)
table2.order("fish", 7, 2)
table2.get_subtotal()
table2.get_total()
table2.split_bill()