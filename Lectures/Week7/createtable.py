table = []
ROWS = 5
COLUMNS = 20
for i in range(ROWS) :
 row = [0] * COLUMNS
 table.append(row)

print(table)



b = []
for i in range(3) :
 b.append([0] * (i + 1))

for i in range(len(b)) :
 for j in range(len(b[i])) :
  print(b[i][j], end=" ")
 print()

