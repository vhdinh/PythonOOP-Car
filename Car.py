class Car(object):
    def __init__(self,price,speed,fuel,mileage,tax = 0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10000:
           self.tax = 1.15
        else:
            self.tax = 1.12
    def display_all(self):
        print 'Price:', self.price, '\n Speed: ', self.speed, '\n Fuel: ', self.fuel, '\n Mileage: ', self.mileage, '\n Tax: ', self.tax

car1 = Car(2000,"35mph","Full","15mpg")
car2 = Car(2000,"5mph","Not Full","105mpg")
car3 = Car(2000,"15mph","Kind of Full","95mpg")
car4 = Car(2000,"45mph","Empty","25mpg")
car5 = Car(2000000,"35mph","Empty","15mpg")

print "car1"
print car1.display_all()
print "car2"
print car2.display_all()
print "car3"
print car3.display_all()
print "car4"
print car4.display_all()
print "car5"
print car5.display_all()

