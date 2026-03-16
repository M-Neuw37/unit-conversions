def centi_kelvin():
    
    """
    celcius takes temperatures in celcius from the user and puts them into a list
    using split(). The inputs must be seperated by a space.
    
    A loop iterates over the list and convernts the tempeatures in celcius to kelvin
    
    returns the values in kelvin.
    
    Example inputs is - 12 20 56 32 42
    
    Example output is -  
    The values in kelvin are:
    285.15K
    293.15K
    329.15K
    305.15K
    315.15K 
    
    """
    
    celcius = input('Enter the temperature in C (seperated by a space): ').split()
    
    celcius_list = [float(i) for i in celcius]
    
    print('The values in kelvin are:')
    
    for celcius in celcius_list:
        kelvin = celcius + 273.15
        print(kelvin,'K', sep='')
    
centi_kelvin()
