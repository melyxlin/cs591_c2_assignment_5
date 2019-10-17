def s2i(s):
    """
        takes in a string s and returns the string representation of the integer i
    """
    #return integer
    returnint = 0 
    #loop to interate through all the characters in s
    for digit in s:
        #changing digit c to the integer representation of it
        digitint = ord(digit) - ord('0') 
        #updating returnint with added digit c
        returnint = returnint*10 + digitint
    return returnint

def i2s(i):
    """
        takes in an integer i and returns the string representation of the integer s
    """
    returnstr = ""
    #case if i is 0
    if i == 0:
        return "0"
    #loop to interate all digits of i
    while i != 0:
        #getting digit at the position corresponding to the number of times the loop has run
        remainder = i%10
        #decrementing i in respect to the loop
        i = i//10
        #adding digit to the string
        returnstr = chr(ord('0')+ remainder) + returnstr
    return returnstr

def multiplystr(num1, num2):
    """
        takes a string representation of 2 integers, num1 and num2, and returns a string presentation of the product of num1 and num2
    """
    #getting integer representation of num1
    int1 = s2i(num1)
    #getting integer representation of num2
    int2 = s2i(num2)
    #getting product of num1 and num2
    product = int1*int2
    #returning integer representation of product
    return i2s(product)


def main():
    num1 = str(input("Enter a number: "))
    num2 = str(input("Enter another number: "))
    product = multiplystr(num1, num2)
    print("Product is:", product)

if __name__ == '__main__': 
    main()