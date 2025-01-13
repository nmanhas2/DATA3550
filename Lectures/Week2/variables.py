#Testing different tpyes in the same variable
taxRate = 5 #int
print(taxRate)
taxRate = 5.5 #float
print(taxRate)
taxRate = "Non-taxable" #string
print(taxRate)
#print(taxRate + 5) #TypeError: can only concatenate str (not "int") to str
print(taxRate + "??") #+ operator with strings, the second argument is concatenated to the end of the first

