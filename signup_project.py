# Signup Page Project

# Function For Checking credentials velidaty
def validate_cred(adminname, adminnumber):
    namelen = len(adminname)
    numberlen = len(adminnumber)
    condi = True
    while condi is True:
        resname = False
        for ele in adminname:
            if ele.isdigit():
                resname = True
                break
            if not (ele.isdigit() or ele.isalpha() or ele == ' '):
                resname = True
                break


        resnum = False
        for ele in adminnumber:
            if not ele.isdigit():
                resname = True

        if resnum and resname is True :
            return True
        else :
            return False

def validate_cred2(username, userpass):
    userlen = len(username)
    passlen = len(userpass)
    condi = True
    while condi is True:
        resuser = False
        for ele in  username:
            if ele.isdigit():
                resuser = True
                break
            if ele.isalpha():
                resuser = True
                break
            if not (ele.isdigit() or ele.isalpha() or ele == ' '):
                resuser = True
                break




# For Input Values
adminname = input("Enter Your Name :")
adminnumber = input("Enter Your 10 Digit Mobile Number :")

cond = validate_cred(adminname, adminnumber)
if cond is True:
    print("Hiii")
else:
    print("Byee")