contact_info = {"name": "Mary", "LastName": "Smith"}
print(contact_info)

#can also use tuple pairs and cast them to dict
data = [("name", "Mary"), ("LastName", "Smith")]
contact_info = dict(data)
contact_info 

#accessing values
fruits = {"apple": 1.00, "banana": 0.67, "orange" : 2.99}
print(fruits["apple"])
print(min(fruits.values()))

lowest_price = min(fruits.values())
for fruit, price in fruits.items() :
  if price  == lowest_price :
    print("The lowest price is: " + str(lowest_price) + " for " + fruit)

#adding KVPs
fruits["Pineapple"] = 3.99
print(fruits)

#adding/replacing value at existing key
fruits["banana"] = 1.56
print(fruits)

#value/key types
stupid_dict = {
    123: "blabla",
    True: 123.456,
    "key": False,
    (123, "abc"): 1000,
    34.5: [0, 1, 1, 2, 3, 5],
}
print(stupid_dict)

#keys are immutable
new_phone_book = {("Paul", "McCartney"): 123456}
print(new_phone_book)
try:
    new_phone_book = {["Paul", "McCartney"]: 123456}
    print(new_phone_book)
except TypeError as e:
   print(e)

#looking up an item
# look up an item
hashes = {
    "a1b2c3d4e5f6g7h8i9j0", "file1.txt"
    "b2c3d4e5f6g7h8i9j0a1", "file2.txt"
    "c3d4e5f6g7h8i9j0a1b2", "file3.txt"
}

key1 = "b2c3d4e5f6g7h8i9j0a1"
key2 = "b2c3d4e5f6g7h8i9j0a3"

if key1 in hashes:
    print("yes")