tmp = float(input('Please enter temperature: ')) # get user input on the temperature value to be converted as a float
unit = input('Please enter temperature unit: ').upper() # get user input on the the temperature unit of tmp, converts string to upper case

def temp_converter(tmp, unit): # create function accepting the above user inputs as arguments
    if unit == 'F':
        c = round(((tmp - 32) * 5/9),1) # if the user enters the temperature in Fahrenheit it's converted to Celcius and vice versa
        print(c, '°C')
    # (-17.22°C × 9/5) + 32 = 1°F
    elif unit == 'C':
        f = round(((tmp * 9/5) + 32),1) 
        print(f, '°F')
    

temp_converter(tmp, unit) # calling the function
