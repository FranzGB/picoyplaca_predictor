class Car:
    '''This is a car class'''   
    def __init__(self,var):
        self.license_plate = var

#Create a new object of Date class
rojo = Car("PBY-0168")

class Date:
    '''This is a date class. It holds the date in format MM/DD/YYYY and hour'''
    def __init__(self):
        self.date = '01/01/1999'
        self.hour = '00:00'

#Create a new object of Date class
current_date = Date()