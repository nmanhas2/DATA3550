canadian = { "Red", "White" }
british = { "Red", "Blue", "White" }
italian = { "Red", "White", "Green" }

inEither = british.union(italian)
print(inEither) #contains one instance of red and white

inBoth = british.intersection(italian)
print(inBoth)

print("Colors that are in the Italian flag but not the British:")
print(italian.difference(british))
