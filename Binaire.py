def get_value():
    print("1. Decimal")
    print("2. Hexadecimal")
    print("3. Classic Binary")
    print("4. Binary C1")
    print("5. Binary C2")
    type_start = int(input("Choose between 1/5: "))
    while type_start not in [1, 2, 3, 4, 5]:
        type_start = int(input("Invalid choice. Choose between 1/5: "))
    value = input("What do you want to convert? ")
    return value, type_start

def DecimalToHexadecimal(value):
    result = []
    quotient = value

    if value == 0:
        hexadecimal_string = "0"

    while quotient != 0:
        rest = quotient % 16
        quotient = quotient // 16
        result.append(rest)

    hexadecimal_string = ''.join([hex(digit)[2:].upper() for digit in result[::-1]])

    return hexadecimal_string

def DecimalToBinary(value):
    result = bin(value)
    return result

def HexToDecimal(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        return decimal_value
    except ValueError:
        print("Error: Please provide a valid hexadecimal number.")

def HexToBinary(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        binary_value = bin(decimal_value)[2:]
        return binary_value
    except ValueError:
        print("Error: Please provide a valid hexadecimal number.")

def BinaryToDecimal(binary):
    decimal = 0
    power = 0

    for digit in reversed(str(binary)):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

def BinaryToHex(binary):
    Hex = 0
    Hex_str = ""
    binary_list = list(binary)

    reversed(binary_list)

    for i in range(len(binary_list)):
        if binary_list[i] == "1":
            Hex += 16**i
        i += 1



    return Hex_str

def convert(type_start, value):
    match type_start:
        case 1:
            print("Hexa: ", DecimalToHexadecimal(int(value)))
            print("Binary: ", DecimalToBinary(int(value)))
        case 2:
            print("Decimal: ", HexToDecimal(value))
            print("Binary: ", HexToBinary(value))
        case 3:
            print("Decimal: ", BinaryToDecimal(int(value)))
            print("Hexa: ", BinaryToHex(value))


value, type_start = get_value()
convert(type_start, value)
