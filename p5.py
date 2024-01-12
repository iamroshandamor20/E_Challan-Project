#  For Checking First Name conditions
import datetime


def first_name_check(first_name):
    fname_len = len(first_name)
    fname_digit = False
    for ele in first_name:
        if ele.isdigit():
            fname_digit = True
            break

    fname_special = False
    for ele in first_name:
        if not ele.isalpha() or ele.isspace() or ele.isdigit():
            fname_special = True
            break

    if (fname_len > 3):
        if fname_digit is False or fname_special is False:
            return 1
        else:
            return 0
    else:
        return 0


#  For Checking First Name conditions

def last_name_check(last_name):
    fname_len = len(last_name)
    fname_digit = False
    for ele in last_name:
        if ele.isdigit():
            fname_digit = True
            break

    fname_special = False
    for ele in last_name:
        if not ele.isalpha() or ele.isspace() or ele.isdigit():
            fname_special = True
            break

    if fname_len > 3:
        if fname_digit is False or fname_special is False:
            return 1
        else:
            return 0
    else:
        return 0


#  For Checking Father Name conditions

def father_name_check(father_name):
    fname_len = len(father_name)
    fname_digit = False
    for ele in father_name:
        if ele.isdigit():
            fname_digit = True
            break

    fname_special = False
    for ele in father_name:
        if not ele.isalpha() or ele.isspace() or ele.isdigit():
            fname_special = True
            break

    if fname_len > 3:
        if fname_digit is False or fname_special is False:
            return 1
        else:
            return 0
    else:
        return 0


#  For Checking Mother Name conditions

def mother_name_check(mother_name):
    fname_len = len(mother_name)
    fname_digit = False
    for ele in mother_name:
        if ele.isdigit():
            fname_digit = True
            break

    fname_special = False
    for ele in mother_name:
        if not ele.isalpha() or ele.isspace() or ele.isdigit():
            fname_special = True
            break

    if fname_len > 3:
        if fname_digit is False or fname_special is False:
            return 1
        else:
            return 0
    else:
        return 0


#  For Checking Date of Birth conditions
def dob_check(date_of_birth):
    return 11


#  For Checking Mobile Number conditions
def mobile_check(mobile_number):
    mobile_len = len(mobile_number)
    mobile_digit = False
    for ele in mobile_number:
        if ele.isdigit():
            mobile_digit = True
            break
    if mobile_len == 10:
        if mobile_digit is False:
            return 1
        else:
            return 0
    else:
        return 0


#  For Checking G-Mail conditions
def gmail_check(g_mail):
    return 34


#  For Checking Address conditions
def address_check(address_inp):
    return 12


print("*********** Fill Your Personal Details ************")
condition1 = 1
while condition1 == 1:
    choice = int(input("Enter (1) for LogIn || Enter (2) for SignIn "))
    if choice == 1:
        print("pleas login na")

    elif choice == 2:

        condition2 = 1
        while condition2 == 1:
            first_name = input("Enter Your First Name :")
            last_name = input("Enter Your Last Name :")
            father_name = input("Enter Your Father Name :")
            mother_name = input("Enter Your Mother Name :")
            date_of_birth = int(input("Enter Your Date of Birth :"))
            mobile_number = int(input("Enter Your Mobile Number :"))
            g_mail = input("Enter Your G-Mail :")
            address_inp = input("Enter Your Address :")

            result1 = first_name_check(first_name)
            print(result1)
            result2 = last_name_check(last_name)
            print(result2)
            result3 = father_name_check(father_name)
            print(result3)
            result4 = mother_name_check(mother_name)
            print(result4)
            result5 = dob_check(date_of_birth)
            print(result5)
            result6 = mobile_check(mobile_number) 
            print(result6)
            result7 = gmail_check(g_mail)
            print(result7)
            result8 = address_check(address_inp)
            print(result8)
    else:
        print("Bro Chalak mat ban shi value daal le option fir se dekh andhe ^)(^ ")
