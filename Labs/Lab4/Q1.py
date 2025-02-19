line = [] #The line of riders
num_vips = 0 #number of VIPs at the front of the line

menu = ( '(1) Reserve okace in line\n'
         '(2) Reserve place in VIP line.\n'
         '(3) Dispatch riders.\n'
         '(4) Print riders.\n'
         '(5) Exit.\n\n'
       )

user_input = input(menu).strip()

while user_input != '5':
    if user_input == '1':
        name = input('Enter name: ').strip()
        print(name)
        line.append(name)
    
    elif user_input == '2':
        name = input('Enter name:').strip()
        print(name)
        line.insert(num_vips, name)
        num_vips = num_vips + 1
    
    elif user_input == '3': 
        if line:
            removed_rider = line.pop(0)

            if(num_vips > 0):
                num_vips -= 1  
            
            print(f"{removed_rider} boarded the ride.")
        else:
            print("Line is empty.")
    elif user_input == '4':
        if line:
            print(f"{len(line)} person(s) waiting: {line}")
        else:
            print("Line is empty.")
    elif user_input == '5':
        continue
    else:
        print("Please enter a valid input")
    user_input = input(menu).strip()


