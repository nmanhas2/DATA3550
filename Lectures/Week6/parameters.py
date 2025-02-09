def main():
    x = 3
    print(computeResult(x + 1))
    print(totalCents(2, 10))
    print(addTax(100, 5))

def computeResult(value):
    result = value ** 2
    result = result + 3
    return result

def totalCents(dollars, cents):
    #Modifies parameter variable
    cents = dollars * 100 + cents
    return cents

"""
This would also work
def totalCents(dollars, cents):
    result = dollars * 100 + cents
    return result
"""

def addTax(price, rate):
    tax = price * rate / 100
    price = price + tax
    return tax

main()
