income = int(input("Enter your income: "))

TAX_BRACKET1 = int(input("Enter the first tax bracket: ")) 
TAX_BRACKET2 = int(input("Enter the second tax bracket: ")) 
TAX_BRACKET3 = int(input("Enter the third tax bracket: ")) 
TAX_BRACKET4 = int(input("Enter the fourth tax bracket: ")) 

total_tax = 0
temp = 0

if income <= TAX_BRACKET1:

    temp = income
    total_tax = temp * 0.1

elif income <= (TAX_BRACKET2 + TAX_BRACKET2):

    temp = income - TAX_BRACKET1
    total_tax = temp * 0.12 + TAX_BRACKET1 * 0.1

elif income <= (TAX_BRACKET1 + TAX_BRACKET2 + TAX_BRACKET3):

    temp = income - TAX_BRACKET1 - TAX_BRACKET2
    total_tax = temp * 0.13 + TAX_BRACKET2 * 0.12 + TAX_BRACKET1 * 0.1

elif income <= (TAX_BRACKET1 + TAX_BRACKET2 + TAX_BRACKET3 + TAX_BRACKET4):

    temp = income - TAX_BRACKET1 - TAX_BRACKET2 - TAX_BRACKET3 
    total_tax = temp * 0.14 + TAX_BRACKET3 * 0.13 + TAX_BRACKET2 * 0.12 + TAX_BRACKET1 * 0.1

else:
    
    temp = income - TAX_BRACKET1 - TAX_BRACKET2 - TAX_BRACKET3 - TAX_BRACKET4
    total_tax = temp * 0.15 + TAX_BRACKET4 * 0.14 +  TAX_BRACKET3 * 0.13 + TAX_BRACKET2 * 0.12 + TAX_BRACKET1 * 0.1
