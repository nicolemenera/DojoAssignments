class Car(object):
  def __init__(self, price=None, speed=None, fuel=None, mileage=None):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if price > "$10,000":
      self.tax = "15%"
    else:
      self.tax = "12%"
    self.display_all()
  def display_all(self):
    print "Price:{}; Speed:{}; Fuel:{}; Mileage:{}; Tax:{}" .format (self.price, self.speed, self.fuel, self.mileage, self.tax)

hyundai = Car("$24,000", "20mph", "Full", "5mpg")
mazda = Car("$12,000", "60mph", "1/4 Full", "60mpg")
honda = Car("$6,500", "10mph", "Empty", "19mpg")
toyota = Car("$58,000", "18mph", "1/2 Full", "21mpg")
volkswagon = Car("$9,999", "36mph", "Full", "30mpg")
chevrolet = Car("$31,000", "37mph", "4/5 Full", "12mpg")

