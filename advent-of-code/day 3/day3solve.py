'''
https://adventofcode.com/2021/day/3

****
1) Check power consumption (PC) -> 
2) Generate two new binary numbers
    a) Gamma rate
    b) Epsilon rate
    c) PC == Gamma * Epsilon
****

#! Gamma Rate:
    - Most common bit in the corresponding position of all numbers in the diagnostic report
    - Will be a SINGLE binary number

#! Epsilon rate:
    - Least common bit in the corresponding position of all numbers in the diagnostic report
    - Will be a SINGLE binary number

#! Power Consumption:
    - Multiply the DECIMAL values of Gamma & Epsilon together to get power conumption
`
#! Binary numbers are 12 bits long
'''

def decimalToBinary(n): # https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ == Decimal to Binary
    return bin(n).replace("0b", "")

def binaryToDecimal(b): # https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ == Binary to Decimal
    return int(b, 2)

if __name__ == '__main__':
    gamma_digit = 0
    epsilon_digit = 0

    num_ones = 0
    num_zeros = 0

    

    stuff = list()
    with open('input.txt') as file:
        
        while True:
            fuck = file.readline()

            if not fuck:
                break
            line = "{}".format(fuck.strip())
            stuff.append(int(line))

    for num in stuff:
        

    