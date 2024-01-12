# E-chaallan Project
# Below Function is for Input

print("Enter Below Your Vehicle Like Car, Bike")
vhicalType = input("Which Vehicle You Driving :  ")

if vhicalType == "Car" or vhicalType == "CAR" or vhicalType == "car":

    print("Press (1) for violating No Seatbelt Rule // Else press anything :  ")
    seatBelt = input("Enter Your choice :  ")

    print("Press (1) for violating Over speeding Rule // Else press anything  :  ")
    overSpeed = input("Enter Your choice :  ")

    print("Press (1) for violating No Driving license Rule // Else press anything :  ")
    driveLicense = input("Enter Your choice :  ")

    print("Press (1) for violating No Insurance Rule // Else press anything:  ")
    insuranceOp = input("Enter Your choice :  ")

    print("Press (1) for violating No PUC Rule // Else press anything:  ")
    pucOp = input("Enter Your choice :  ")

    print(" ")

    totalChalan = 0

    if seatBelt == "1":
        print("You've Violated No Seat belt Rule ")
        chalan = 200
        totalChalan = totalChalan+chalan

    if overSpeed == "1":
        print("You've Violated Over Speeding Rule ")
        chalan = 500
        totalChalan = totalChalan+chalan
    if driveLicense == "1":
        print("You've Violated No License Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if insuranceOp == "1":
        print("You've Violated No Insurance Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if pucOp == 1:
        print("You've Violated No PUC Rule")
        chalan = 500
        totalChalan = totalChalan+chalan
    print(" ")
    print("You've Guilty Your Total fine is : ", totalChalan)

# for inputing for Bike

elif vhicalType == "Bike" or vhicalType == "bike" or vhicalType == "BIKE":

    print("Press (1) for violating No RC Rule // Else press anything :  ")
    noRc = input("Enter Your choice :  ")

    print("Press (1) for violating Over speeding Rule // Else press anything  :  ")
    overSpeed = input("Enter Your choice :  ")

    print("Press (1) for violating No Driving license Rule // Else press anything :  ")
    noDriveing = input("Enter Your choice :  ")

    print("Press (1) for violating No Insurance Rule // Else press anything:  ")
    noInsurance = input("Enter Your choice :  ")

    print("Press (1) for violating No Helmet Rule // Else press anything:  ")
    noHelmet = input("Enter Your choice :  ")

    print(" ")

    totalChalan = 0

    if noRc == "1":
        print("You've Violated No RC Rule ")
        chalan = 200
        totalChalan = totalChalan+chalan

    if ov == "1":
        print("You've Violated Over Speeding Rule ")
        chalan = 500
        totalChalan = totalChalan+chalan
    if noDriveing == "1":
        print("You've Violated No License Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if noInsurance == "1":
        print("You've Violated No Insurance Rule")
        chalan = 1000
        totalChalan = totalChalan+chalan
    if noHelmet == "1":
        print("You've Violated No Insurance Rule")
        chalan = 300
        totalChalan = totalChalan + chalan

    print(" ")
    print("You've Guilty Your Total fine is : ", totalChalan)

else:
    print("Your Entered somthin wrong !!")
