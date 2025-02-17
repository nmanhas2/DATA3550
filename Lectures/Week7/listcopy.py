#hard copy, pointing to the same list reference
values = [5, 20, 18, -3, 67, 85, 32]

prices = values

print(max(values))
print(max(prices))

#shallow copy, it's referring to a different list, but the contents are the sames
values = [5, 20, 18, -3, 67, 85, 32]

prices = list(values)

print(max(values))
print(max(prices))

#example showcasing that they are now referring to different lists
values = [5, 20, 18, -3, 67, 85, 32]

prices = list(values)

prices[3] = 50
print(values)
print(prices)