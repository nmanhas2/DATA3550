def main():

    while 1:
        myInput = input("Enter text or type 'done', 'Done', or 'd' to exit: ")

        if myInput.lower() in ["done", "d"]:
            break
        
        myOutput = myInput[::-1]
        
        print(myOutput)

main()
