#you can append elements to a list, this adds the element to the end of the list
mylist = []
mylist.append(4)
print(mylist)

#you can also insert at a specific position, which will push the element at that
#position, if it exists, to the right of the list
names = []
names.append("Amy")
names.append("Bob")
names.append("Peg")
names[1] = "John"
names.insert(2, "Paul")

print(names)

names = []
names.append("Amy")
names.append("Bob")
names.append("Peg")
names[0] = "Cy"
names.insert(0, "Ravi")
names.insert(4, "Savannah")

print(names)

