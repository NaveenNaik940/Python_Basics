'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 14:39:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 14:39:00
@Title :Temperature Conversion Program from Celsius to Fahrenheit or vice versa

'''


def temperature_conversion(temperature,unit):
    """
    Dsecription:
        function will convert temperature from celsius to fahrenheit or vice versa based unit
    Paramater:
        temperature:takes temeperature value as parameter
        unit:takes unit of temperature 
    return 
        string        
    """
    if unit in 'cC':
        fahrenhiet_temp=(temperature*9/5)+32
        return f"{temperature} °C = {fahrenhiet_temp:.2f} °F"
    elif unit in 'fF':
        celsius_temp=(temperature-32)*5/9
        return f"{temperature} °F = {celsius_temp:.2f} °C"
    else:
        return f"Enter valid unit of temperature"

def main():
    try:
        temperature=float(input("Enter temperature to convert to celsius or fahrenheit"))
        unit=input("enter the unit of temperature c/C or f/F")
        char=unit[0]
        print("after converting temperature: ",temperature_conversion(temperature,char))
    except ValueError:
        print(f"Enter the valid input float value")

if __name__=='__main__':
    main()