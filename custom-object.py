import math

class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0

    def calculateTipInWholeDollarsOver20Percent(self, tipPercent):
        return math.ceil(self.amount * tipPercent/100.0)

    def calculateTotalInWholeDollarsOver20Percent(self, tipPercent, taxPercent):
        # return self.amount * (1 + taxPercent/100.0 + math.ceil(tipPercent/100.0)) 
        return self.amount * (1 + taxPercent/100.0) + math.ceil(self.amount * tipPercent/100.0) 

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)  
    
purchase = Purchase(100.0)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)
tipWholeDollars = purchase.calculateTipInWholeDollarsOver20Percent(tipPercent)

print("tax: ", tax)
print("tip: ", tip)
print("total: ", purchase.calculateTotal(taxPercent, tipPercent))
print("\n")


purchase_2 = Purchase(11.0)
tipWholeDollars = purchase_2.calculateTipInWholeDollarsOver20Percent(tipPercent)
print("tip whole dollars: ", tipWholeDollars)
print("total when tip with whole dollars: ", purchase_2.calculateTotalInWholeDollarsOver20Percent(taxPercent, tipPercent))