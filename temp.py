def convert_temp() :
    tf = eval(input("Enter a temperature in Fahrenheit:"))
    print("The temperature in Fahrenheit is:", tf)
    convert_to_celcius(tf)   

def convert_to_celcius(tf,tc):
    tc = 5/9(tf-32)
    print("The temperature in Celsius is:",tc)
    return    

def convert_to_kelvin(tc,tk):
    tk = (tc+273.15)
    print("The temperature in Kelvin is:",tk)
    


