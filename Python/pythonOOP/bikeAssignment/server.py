class Bike(object):
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def displayInfo(self):
    print "Bike price:{}; Maximum Speed:{}; Total Miles {}" .format (self.price, self.max_speed, self.miles)
  def ride(self):
    print "Riding"
    self.miles = self.miles + 10
  def reverse(self):
    print "Reversing"
    if self.miles >= 5:
      self.miles = self.miles - 5
    
giant = Bike("$3200", "24mph")
trek = Bike("$1800", "20mph")
huffy = Bike("$120", "12mph")

giant.ride()
giant.ride()
giant.ride()
giant.reverse()
giant.displayInfo()

trek.ride()
trek.ride()
trek.reverse()
trek.reverse()
trek.displayInfo()

huffy.reverse()
huffy.reverse()
huffy.reverse()
huffy.displayInfo()