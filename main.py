def temperature_converter():
    switchOfKelvin = 273.15
    inp = input('Ready to listen. ').split()
    if inp[0].lower() == 'k':
        celsius = float(inp[1]) - switchOfKelvin
        to_print(inp[1], str(celsius), inp[0], inp[2])
    else:
        kelvin = float(inp[1]) + switchOfKelvin
        to_print(inp[1], str(kelvin), inp[0], inp[2])


def to_print(inpTemp, outTemp, inpStr, outStr):
    return print(inpTemp + "° " + inpStr + " equals " + outTemp + "° " + outStr)




if __name__ == '__main__':
    temperature_converter()
