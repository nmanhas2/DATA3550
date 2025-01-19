#Write a scirpt to calculate the cost of shipping a package, as follows:
#$5 for packages weighing less than ten pounds,
#$10 for packages weighing ten pounds or more but less than twenty pounds,
#and $15 for packages weighing twenty pounds or more.

#if weight < 10, $5 * weight
#if weight >= 20, $15 * weight
#else $10 * weight

packageWeight = input("Enter the package weight in pounds: ")

packageWeight = float(packageWeight)
if packageWeight < 10:
    print(5)
elif packageWeight >= 20:
    print(15)
else:
    print(10)
