import math

class Table:
    def __init__(self,diners):
        self.diners = diners
        self.bill = []
        
        
    def order(self,name,price,quantity=1):
        if self.bill == []:
            self.bill.append({"item":name,"price":price,"quantity":quantity})
            return


        for i in range(0,len(self.bill)):
            if self.bill[i]["item"] == str(name):
                self.bill[i]['quantity'] += quantity
                return
                    
        self.bill.append({"item":name,"price":price,"quantity":quantity})
        



        
    def remove(self,name,price,quantity):
        try:
            self.bill.remove({"item":name,"price":price,"quantity":quantity})
        except:
            for i in range(0,len(self.bill)):
                if self.bill[i]['item'] == name:
                    self.bill[i]['quantity'] -= quantity
                    pass

    

    
  
    
    def bill(self):
        print(self.bill)



    
    def get_subtotal(self):
        
        sub_total = 0
        for i in range(0,len(self.bill)):
            sub_total += self.bill[i]['price'] * self.bill[i]['quantity']
        
        return sub_total


        
    def get_total(self,service_charge_percentage=0.1):
        
        sub_total = self.get_subtotal()
        service_charge = round(sub_total * float(service_charge_percentage),2)
        
        return {"Sub Total": "£"+('%.2f' %sub_total), "Service Charge": "£"+str(service_charge), "Total": "£"+str(sub_total+service_charge)}
        


        
    def split_bill(self):
        
        sub_total = self.get_subtotal()
        split = math.ceil((sub_total / self.diners)*100)/100
        
        return split