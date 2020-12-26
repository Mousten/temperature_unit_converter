tmp = float(input('Please enter temperature: '))
unit = input('Please enter temperature unit: ').upper()

def temp_converter(tmp, unit):
    if unit == 'F':
        c = round(((tmp - 32) * 5/9),1)
        print(c, '°C')
    # (-17.22°C × 9/5) + 32 = 1°F
    elif unit == 'C':
        f = round(((tmp * 9/5) + 32),1)
        print(f, '°F')
    

temp_converter(tmp, unit)