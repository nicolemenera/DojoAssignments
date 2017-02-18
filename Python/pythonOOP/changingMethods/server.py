class Bike(object):
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def displayInfo(self):
    print "Bike price:{}; Maximum Speed:{}; Total Miles {}" .format (self.price, self.max_speed, self.miles)
    return self
  def ride(self):
    print "Riding"
    self.miles = self.miles + 10
    return self
  def reverse(self):
    print "Reversing"
    if self.miles >= 5:
      self.miles = self.miles - 5
    return self
    
giant = Bike("$3200", "24mph")
trek = Bike("$1800", "20mph")
huffy = Bike("$120", "12mph")

giant.ride().ride().ride().reverse().displayInfo()
trek.ride().ride().reverse().reverse().displayInfo()
huffy.reverse().reverse().reverse().displayInfo()

