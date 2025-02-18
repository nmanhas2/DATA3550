COUNTRIES = 8
MEDALS = 3


counts = [
   [ 0, 3, 0 ],
   [ 0, 0, 1 ],
   [ 0, 0, 1 ],
   [ 1, 0, 0 ],
   [ 0, 0, 1 ],
   [ 3, 1, 1 ],
   [ 0, 1, 0 ],
   [ 1, 0, 1 ]
]

# Print the table header.
print("  Gold  Silver  Bronze ")



#To access all elements in a table, you use two nested loops.

for i in range(COUNTRIES) :

    # Process the ith row.
 for j in range(MEDALS) :
    # Process the jth column in the ith row.
  print("%8d" % counts[i][j], end="")

 print()