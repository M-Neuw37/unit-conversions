# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:55:17 2026

@author: micha
"""

def choose_speed():
    
    choice  =input(
        '\n----------'
        '\nMph -> Kph - K\n'
        'Kph -> Mph - M\n'
        'Return to the main menu - R\n'
        'Enter your choice: ').upper()
    
    if choice == "K":
        print('\n----------')
        print('Convert miles an hour (Mph) to\nkilometers per hour (Kph) below')
        mph_kph()
    elif choice == "M":
        print('\n----------')
        print('Convert kilometers per hour (Kph) to\nmiles an hour (Mph) below')
        kph_mph()
    elif choice == "R":
        MS_KM_conversion_menu()
    else:
        print('Invalid option')
        return

def mph_kph():
    
    miles_an_hour = float(input('Enter the speed in Mph: '))
    
    Kilometers_an_hour = miles_an_hour * 1.60934
    
    print(f'{miles_an_hour}Mph is {Kilometers_an_hour:.2f}Km/h')
    
def kph_mph():
    
    Kilometers_an_hour = float(input('Enter the speed in Km/h: '))
    
    miles_an_hour = Kilometers_an_hour * 0.6124
    
    print(f'{Kilometers_an_hour}Km/h is {miles_an_hour:.2f}Mph')
    
def choose_distance():
    
    choice  =input(
        '\n----------'
        '\nMiles -> Kilometers - K\n'
        'Kilometers -> Miles - M\n'
        'Return to the main menu - R\n'
        'Enter your choice: ').upper()
    
    if choice == "K":
        print('\n----------')
        print('Convert miles (m) to kilometers (k) below')
        miles_km()
    elif choice == "M":
        print('\n----------')
        print('Convert kilometers (k) to miles (m) below')
        km_miles()
    elif choice == "R":
        MS_KM_conversion_menu()
    else:
        print('Invalid option')
        return

def miles_km():
    
    miles = float(input('Enter the distance in miles: '))
    
    kilometers = miles * 1.60934
    
    print(f'{miles} miles in kilometers is {kilometers:.2f} kilometers')
    
def km_miles():
    
    kilometers = float(input('Enter the distance in kilometers: '))
    
    miles = kilometers * 0.6124
    
    print(f'{kilometers} kilometers in miles is {miles:.2f} miles')
    
def MS_KM_conversion_menu():
    
    """
    The main menu to this programme that allows you to convert miles per hour (Mph)
    to kilometers per hour (Kph) and the other way around and miles to kilometers and also
    vice versa. 
    
    The input determines if the user wants to convert speed (i.e. Mph -> Kph) or 
    distance (miles -> kilometers) adn takes them to the appropriate menu where they 
    choose whether it is miles to kilometers or kilometers to miles, for example. 
    """
    
    choice = input(
        "\n"
        "Choose what you want to convert:\n"
        "Speed - S\n"
        "Distance - D\n"
        "Quit - Q\n"
        "Enter your choice: "
        ).upper()
    
    if choice == "S":
        choose_speed()
        
    elif choice == "D":
         choose_distance()
    
    elif choice == "Q":
         print("You have quit the programme")
         return
    else:
        print('Invalid option')

if __name__ == "__main__":
    MS_KM_conversion_menu()