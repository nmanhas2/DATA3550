# 8 = Most structures fall
# 7 = Many building destroyed
# 6 = Many buildings considerably damaged, some collapse
# 4.5 = Damage to poorly constructed buildings
# <4.5 = No destruction of buildings

#if >= 8 print most structures fall
#elif >= 7 print many buildings destroyed
#elif >= 6 print many buildings considerably damaged, some collapse
#elif  >= 4.5 print Damage to poorly constructed buildings
#else no desctruction of buildings

richter = input("Richter scale: ")


richter = float(richter)
if richter >= 8:
    print("Most structures fall.")
elif richter >= 7:
    print("Many buildings destroyed.")
elif richter >= 6:
    print("Many buildings considerably damaged, some collapse.")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings.")
else:
    print("No destruction of buildings.")
