#pop will return the value that was returned, and accepts the index of the element
#that you want to remove
friends = ["Harry", "Cindy", "Emily", "Bob", "Cari", "Bill"]
#friends.pop(1)

print("The removed item is", friends.pop(1))

#calling pop without an argument removes and returns the last element of the list
friends = ["Harry", "Cindy", "Emily", "Bob", "Cari", "Bill"]
print("The removed item is", friends.pop())

#remove allows you to eemove an element by its value instead of its index. it removes
#the first appearance of the element
friends = ["Harry", "Cindy", "Emily", "Bob", "Cari", "Bill", "Cari"]
friends.remove("Cari")

print(friends)