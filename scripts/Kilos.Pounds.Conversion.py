def Kilos_to_Lbs():
    
    """Calculate the weight in kilos(kgs) into pounds (lbs)"""
    
    kilos = float(input('Weight(kgs): '))
    
    print(kilos * 2.204, 'Lbs', sep='')
    

def Lbs_to_Kilos():
    
    """Calculate the weight in pounds(lbs) to kilos(kgs)"""
    
    pounds = float(input('Weight(lbs): '))
    
    print(pounds * 0.454, 'Kgs', sep='')
    
def weight_conversion_menu():
    
    """
    The menu function to allow the user to choose what they want to convert. 
    
    For kilos (K) to pounds (Lbs) type 'P'
    For pounds (lbs) to kilos (K) type 'K'
    To quit the programme type 'Q'
    """
    
    choice = input(
        "Choose a conversion\n"
        "For Kilos to Lbs type - P\n"
        "For Lbs to Kilos type - K\n"
        "To quit the programme type - Q\n"
        'Enter your choice: '
        ).upper()
    
    if choice == "P":
        print('Convert Kilos to Lbs below:')
        Kilos_to_Lbs()
        
    elif choice == "K":
         print('Convert Lbs to Kilos below:')
         Lbs_to_Kilos()
    
    elif choice == "Q":
         print("You have quit the programme")
         return
    else:
        print('Invalid option')

if __name__ == "__main__":
    weight_conversion_menu()
