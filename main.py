import sys
import utils

# Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), 
# and a time, and the program will return whether or not that car can be on the road. 
# You may use any input and output method you prefer.


def main():
    #Check if the OS have passed all the parameters.
    if len(sys.argv) < 3:
        my_car = utils.Car(input("Enter the license plate of the car "))
        d,t = input("Enter the date in format MM/DD/YYYY "), input("Enter the time in format HH:MM ")
        my_date = utils.Date(d,t)
  
    else:
        my_car = utils.Car(sys.argv[1])
        my_date = utils.Date(sys.argv[2],sys.argv[3])
    #Initialize predictor object
    predictor = utils.Predictor()
    #Output:
    if(predictor.evaluate_car(my_car,my_date)):
        print('The car with license plate '+ my_car.license_plate + ' can be on the road right now. Today is ' + my_date.get_weekdayname())
    else:
        print('The car with license plate '+ my_car.license_plate + ' can not be on the road. You should wait. Today is ' + my_date.get_weekdayname())     
   
if __name__ == '__main__':
    main()