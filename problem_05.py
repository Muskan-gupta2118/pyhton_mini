temp_value=int(input("Entr the value of temperature"));
unit=input("Enter the unit of temperature");

def temperature_change(temp_value,unit):
    if unit=='c':
        newtemp_value=(temp_value*9/5)+32;
        print(f"the temperature for{temp_value} deg celsius is fahrenhite is :{newtemp_value}");
    elif unit=='f':
        newtemp_value=(temp_value*5/9)+32;
        print(f"the temperature for{temp_value} deg fahrenhite is celcius {newtemp_value}");
    else:
        print("you enter a wrong unit");    
temperature_change(temp_value,unit);
          
        