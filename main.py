import sys
import utils
#Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), 
# and a time, and the program will return whether or not that car can be on the road. 
# You may use any input and output method you prefer.


    
    
#Create a new object of Date class
#rojo = Car("PBY-0168")



#Create a new object of Date class
#current_date = Date('01/01/1111','00:00')

def main():
    mycar = utils.Car(sys.argv[1])
    mydate = utils.Date(sys.argv[2],sys.argv[3])
    print(1)
   
main()