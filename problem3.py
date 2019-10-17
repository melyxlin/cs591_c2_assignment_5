def s2i(s):
    """
        takes in a string s and returns the string representation of the integer i
    """
    returnint = 0
    for digit in s:
        digitint = ord(digit) - ord('0')
        returnint = returnint*10 + digitint
    return returnint

def i2s(i):
    """
        takes in an integer i and returns the string representation of the integer s
    """
    returnstr = ""
    while i != 0:
        remainder = i%10
        i = i//10
        returnstr = chr(ord('0')+ remainder) + returnstr
    return returnstr

def multiplystr(num1, num2):
    """
        takes a string representation of 2 integers, num1 and num2, and returns a string presentation of the product of num1 and num2
    """
    if num1 == "0" or num2 == "0":
        return "0"
    int1 = s2i(num1)
    int2 = s2i(num2)
    product = int1*int2
    return i2s(product)


def main():
    num1 = str(input("Enter a number: "))
    num2 = str(input("Enter another number: "))
    product = multiplystr(num1, num2)
    print("Product is:", product)

if __name__ == '__main__': 
    main()