import sys

class Car:
    '''This is a car class'''   
    def __init__(self,var):
        self.license_plate = var
    
    
#Create a new object of Date class
#rojo = Car("PBY-0168")

class Date:
    '''This is a date class. It holds the date in format MM/DD/YYYY and hour'''
    def __init__(self,d,h):
        self.date = d
        self.hour = h

#Create a new object of Date class
#current_date = Date('01/01/1111','00:00')

def main():
    mycar = Car(sys.argv[1])
    mydate = Date(sys.argv[2],sys.argv[3])
   
main()