try:
    wind_speed = float(input("enter the wind speed\n->"))
    if wind_speed < 74:
        print("Tropical storm")
    elif wind_speed < 96:
        print("Category 1")
    elif wind_speed < 111:
        print("Category 2")
    elif wind_speed < 130:
            print("Category 3")
    elif wind_speed < 157:
        print("Category 4")
    else:
        print("Category 5")
    
except:
     print("please enter a valid intitger")
    

