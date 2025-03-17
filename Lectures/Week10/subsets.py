canadian = { "Red", "White" }
british = { "Red", "Blue", "White" }
italian = { "Red", "White", "Green" }

if canadian.issubset(british)	:
  print("Subset")

french = { "Red", "White", "Blue" }
british = { "Red", "Blue", "White" }

if french == british :
  print("equal.")