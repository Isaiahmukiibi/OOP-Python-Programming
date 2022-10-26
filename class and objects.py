class Phone:
    def __init__ (self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    def call (self, phone_number):
        print(f"{self.brand} is calling {phone_number}")
    def __str__(self) ->str:
        return f"Brand = {self.brand}\nprice = {self.price}\ncolor = {self.color}" #str overriding

Iphone = Phone("Iphone 13 pro", 800, "Black")
Nokia = Phone("Nokia 11 pro", 200, "Red")
Sumsung = Phone("Sumsung 20", 300,"Silver")

print(Iphone)
Iphone.call("0708206315")
print(Nokia)
Nokia.call("0781211311")
print(Sumsung)
Sumsung.call("0788206318")



#print(Iphone.brand)
#print(Iphone.price)
#print(Iphone.color)
#Iphone.call("0708206315")

#print(Nokia.brand)
#print(Nokia.price)
#print(Nokia.color)
#Nokia.call("0781211311")

#print(Sumsung.brand)
#print(Sumsung.price)
#print(Sumsung.color)
#Sumsung.call("0788206318")
