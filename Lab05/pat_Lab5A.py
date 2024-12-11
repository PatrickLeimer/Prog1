#Lab 05 Patrick Leimer 2/22/2024
def hex_char_decode(digit):
    hexValdec = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15} #dictionary
    if digit.upper() in hexValdec:
        digit = hexValdec[digit]
    return int(digit)
def hex_string_decode(hex):
    if '0x'in hex:
        actualHex = hex[2:]
    else:
        actualHex = hex
    decVal = 0
    for i in range(len(actualHex)):
       decVal = decVal * 16 + hex_char_decode(actualHex[i].upper())
    return decVal
def binary_string_decode(binary):
    if '0b' in binary:
        binary = binary[2:]
    else:
        binary = list(binary)
    decVal = 0
    for i in range(len(binary) - 1, -1, -1):
        if int(binary[i]) == 1:
            decVal += 2**(len(binary)-1-i)
    return decVal
def binary_to_hex(binary):
    binary = list(binary)
    hexVal = []
    hexValdec = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15} #dictionary
    while len(binary) % 4 != 0:
        binary.insert(0, '0')

    for i in range(0, len(binary) // 4):
        tempPop = list(binary[:4])
        sum = 0
        for j in range(0, len(tempPop)):
            if tempPop[j] == '1':
                sum +=  2 ** (3-j)

        if sum >= 10:
            sum = list(hexValdec.keys())[list(hexValdec.values()).index(sum)]
            #find the index of the value of the sum, so key[index] that contains the value that matched with sum
        hexVal.append(str(sum))
        binary = binary[4:]
    return ''.join(hexVal)

if __name__ == '__main__':
    while True:
        print("\nDecoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
        choice = int(input("Please enter an option: "))
        userInp = ''
        if choice == 4:
            break
        if choice == 1:
            print("Result: ", hex_string_decode(str(input("Please enter the numeric string to convert: "))))
        if choice == 2:
            print("Result: ", binary_string_decode(str(input("Please enter the numeric string to convert: "))))
        if choice == 3:
            print("Result: ", binary_to_hex(str(input("Please enter the numeric string to convert: "))))
