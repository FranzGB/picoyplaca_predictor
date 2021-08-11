# picoyplaca_predictor
"Pico y Placa" predictor. The inputs should be a license plate number (the full number, not the last digit), a date (as a String), and a time, and the program will return whether or not that car can be on the road.
This are the rules for circulation:    
    -Valid from 07:00 to 09:30 and from 16:00 to 19:30.
    -Monday: Cars which its license plate last digit is 1 or 2.
    -Tuesday: Cars which its license plate last digit is 3 or 4.
    -Wednesday: Cars which its license plate last digit is 5 or 6.
    -Thursday: Cars which its license plate last digit is 7 or 8.
    -Friday: Cars which its license plate last digit is 9 or 0.
    -Saturday and Sunday: Free circulation.

The rules used are not the vigent law but rather an iteration from 2019 in Quito before the pandemic. 
### For example:
Let the car license plate be "PBY-0825" and the current date and time be "08/11/2021" and "08:15" respectively. Then we proceed to take the last digit of the license plate which is "4". We have that in that date it is Wednesday and the given time is between the restricted time frame. Then we have that that car could not be on the road because of ``pico y placa´´.

## How to run
To test this program you should run the folowing command on the terminal:
```
python main.py [license_plate string] [MM/DD/YYYY] [HH:MM]
```
You can also run it without arguments. The program will requiere that you input the paramaters manually via console.
```
python main.py
```
## Some guide lines to develop this project

    - [x] Good object-oriented code, avoiding repetition and favoring a consistent organization. You should stick to your chosen language’s semantics, and try to be as consistent as possible.
    - [x] Correct usage of version control tools, with a good commit history and incremental software delivery practices.
    - []  Automated testing with any framework or tool of your choice.
    - [x] We value candidates that love clean, well-structured code, and that can solve problems in a creative way.

