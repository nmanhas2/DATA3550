num = 1
mylist = [1, 2, 3, 4]

#call by value
def add_one(a) :
    return a + 1

#similar to call by reference, but again
#it's not quite call by reference since
#you can't replace the list by assigning
#it to another list
#this is called CALL BY OBJECT
def add_more(l) :
    l.append(5)

#We can try to assign the list to an empty one
def clean_it(l) :
 #we can see that the memory address is actually 
 #different than the original list
 print(id(l))
 l = []
 print(id(l))

def main():

    add_one(num)

    print("After the add_one function: ", add_one(num))

    print("The num is still ", num)

    add_more(mylist)

    print(mylist)

    print("After the function: ", clean_it(mylist))

    print("mylist: ", mylist)
main()