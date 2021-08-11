import datetime 


class Car:
    '''This is a car class'''   
    def __init__(self,var):
        self.license_plate = var
    
    def get_lastdigit(self):
        lastdigit = self.license_plate[-1]
        return lastdigit


class Date:
    '''This is a date class. It holds the date in format MM/DD/YYYY and time in format HH:MM '''
    def __init__(self,d,t):
        self.date = d
        self.time = t
    
    def get_weekday(self):
        '''This method returns the day number that corresponds to that date'''
        return (datetime.datetime.strptime(self.date, '%m/%d/%Y').weekday())
    
    def is_in_between(self):
        '''This method returns whether the time is between the restricted time range or not'''
        ON_TIME_1 = datetime.time(7,00)
        OFF_TIME_1 = datetime.time(9,30)
        ON_TIME_2 = datetime.time(16,00)
        OFF_TIME_2 = datetime.time(19,30)
        
        
        split_time = self.time.split(':') #Useful variable to split the strig into two numbers.
        
        current_time = datetime.time(int(split_time[0]),int(split_time[1]))
        return( (ON_TIME_1 <= current_time <= OFF_TIME_1) or (ON_TIME_2 <= current_time <= OFF_TIME_2))

  


def evaluate_car(car,date):
    '''
    evaluate_car function recives as input the Car and the Date objects. It evaluate the following conditions and return wheter or not the car can be on the road.
    The rules used are not the vigent law but rather an iteration from 2019 in Quito before the pandemic. 
    Rules:
    -Valid from 07:00 to 09:30 and from 16:00 to 19:30.
    -Monday: Cars which it's license plate last digit is 1 or 2.
    -Tuesday: Cars which it's license plate last digit is 3 or 4.
    -Wednesday: Cars which it's license plate last digit is 5 or 6.
    -Thursday: Cars which it's license plate last digit is 7 or 8.
    -Friday: Cars which it's license plate last digit is 9 or 0.
    '''
    lastdigit = car.get_lastdigit()
    
    #First let us check if the rule applies on the time range
    #if
    
