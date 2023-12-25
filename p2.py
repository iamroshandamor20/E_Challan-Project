print("Enter Below Your Vehicle Like Car, Bike")
op1 = input("Which Vehicle You Driving :  ")

if op1 == "Car" or op1 == "CAR" or op1 == "car":
    print("Press (1) for violating No Seatbelt Rule // Else press anything :  ")
    onp1 = input("Enter Your choice :  ")
    print("Press (1) for violating Over speeding Rule // Else press anything  :  ")
    onp2 = input("Enter Your choice :  ")
    print("Press (1) for violating No Driving license Rule // Else press anything :  ")
    onp3 = input("Enter Your choice :  ")
    print("Press (1) for violating No Insurance Rule // Else press anything:  ")
    onp4 = input("Enter Your choice :  ")
    print("Press (1) for violating No PUC Rule // Else press anything:  ")
    onp5 = input("Enter Your choice :  ")
    print(" ")

    totalChalan = 0

    if onp1 == "1":
        print("You've Violated No Seat belt Rule ")
        chalan = 200
        totalChalan = totalChalan+chalan

    if onp2 == "1":
        print("You've Violated Over Speeding Rule ")
        chalan = 500
        totalChalan = totalChalan+chalan
    if onp3 == "1":
        print("You've Violated No License Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if onp4 == "1":
        print("You've Violated No Insurance Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if onp5 == 1:
        print("You've Violated No PUC Rule")
        chalan = 500
        totalChalan = totalChalan+chalan
    print(" ")
    print("You've Guilty Your Total fine is : ", totalChalan)
elif op1 == "Bike" or op1 == "bike" or op1 == "BIKE":
    print("Press (1) for violating No RC Rule // Else press anything :  ")
    onp1 = input("Enter Your choice :  ")
    print("Press (1) for violating Over speeding Rule // Else press anything  :  ")
    onp2 = input("Enter Your choice :  ")
    print("Press (1) for violating No Driving license Rule // Else press anything :  ")
    onp3 = input("Enter Your choice :  ")
    print("Press (1) for violating No Insurance Rule // Else press anything:  ")
    onp4 = input("Enter Your choice :  ")

    print(" ")

    totalChalan = 0

    if onp1 == "1":
        print("You've Violated No RC Rule ")
        chalan = 200
        totalChalan = totalChalan+chalan

    if onp2 == "1":
        print("You've Violated Over Speeding Rule ")
        chalan = 500
        totalChalan = totalChalan+chalan
    if onp3 == "1":
        print("You've Violated No License Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if onp4 == "1":
        print("You've Violated No Insurance Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    print(" ")
    print("You've Guilty Your Total fine is : ", totalChalan)
