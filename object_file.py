"""
This is a car class with its attributes.This code's pylint score is 8.89.
"""
class Car(object):

    """
    This is a simple code showing how classes are created in Python
    """
    def __init__(self, model, cost, hq):
        self.model = model
        self.cost = cost
        self.headoffice = hq

HONDA = Car("Accord", 100000, "Tokyo")
#print(honda.headoffice)

MARUTI = Car("Swift", 750000, "Gurgaon")
AUDI = Car("Quess", "1500000", "Berlin")

print "The Cost of honda is :" + str(HONDA.cost)
