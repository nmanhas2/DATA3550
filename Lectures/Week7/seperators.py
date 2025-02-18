students = ["Harry", "Cindy", "Emily"]
result = ""
for i in range(len(students)) :
	if i > 0 :
	   result = result + ", "
result = result + students[i]

print(result)

#if we want to print values without adding
#them to a string, we need to adapt the
#algorithm slightly
values = [18, 21, 24, 28, 33, 39, 40, 39, 36, 30, 22, 18]
result = 0.0
for element in values :
   result = result + element

print(result)