cast = {"Luigi", "Gumbys", "Spiny"} #1
cast.add("Arthur") #2
cast.add("Luigi") #3 (nothing happens)
print(cast)

cast.discard("Arthur")
print(cast)

try:
    cast.remove("Arthur")
except Exception as e:
    print(e)

cast.clear()

print(cast)