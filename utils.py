import datetime 


class Car:
    '''This is a car class. It holds the entire license plate string.'''   
    #Constructor
    def __init__(self,var):
        self.license_plate = var
    
    def get_lastdigit(self):
        lastdigit = self.license_plate[-1]
        return lastdigit


class Date:
    '''This is a date class. It holds the date in format MM/DD/YYYY and time in format HH:MM '''
    #Constructor
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

    def get_weekdayname(self):
        weekdays={ 1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
        }
        return(weekdays[datetime.datetime.strptime(self.date, '%m/%d/%Y').weekday()])



class Predictor:
    ''' This is the predictor class. '''
    
    def evaluate_car(car,date):
            '''
            evaluate_car method recives as input the Car and the Date objects. It evaluate the following conditions and return wheter or not the car can be on the road.
            The rules used are not the vigent law but rather an iteration from 2019 in Quito before the pandemic. 
            Rules:
            -Valid from 07:00 to 09:30 and from 16:00 to 19:30.
            -Monday: Cars which its license plate last digit is 1 or 2.
            -Tuesday: Cars which its license plate last digit is 3 or 4.
            -Wednesday: Cars which its license plate last digit is 5 or 6.
            -Thursday: Cars which its license plate last digit is 7 or 8.
            -Friday: Cars which its license plate last digit is 9 or 0.
            -Saturday and Sunday: Free circulation.
            '''
            lastdigit = car.get_lastdigit()
            lastdigit = int(lastdigit)

            #First let us check if the rule applies on the time range:
            if (not date.is_in_between()):
                return True
            else:
                #If not then we should check if the rules apply to that car in that day.
                if(date.get_weekday()==1 and lastdigit in (1,2) ):
                    return False
                elif(date.get_weekday()==2 and lastdigit in (3,4)):
                    return False
                elif(date.get_weekday()==3 and lastdigit in (5,6)):
                    return False
                elif(date.get_weekday()==4 and lastdigit in (7,8)):
                    return False
                elif(date.get_weekday()==5 and lastdigit in (9,0)):
                    return False
                else:
                    return True
        
