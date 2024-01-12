fullName = 'Roshan Damor'
userName = 'roshan_damor18'
userPass = 'Roshan@1310'
print(userPass)
print(userName)
print(fullName)
pp = 1
while pp == 1:
    op = int(input("Enter (1) for LogIn || Enter (2) for SignIn :  "))
    # It is signup page code here \\\\
    if op == 2:

        # It is for checking Name Validation

        x = 5
        while x == 5:
            fullName = input("Enter Your Name :  ")
            length = len(fullName)

            resi1 = False
            for ele in fullName:
                if ele.isdigit():
                    resi1 = True
                    break

            resi2 = False
            for c in fullName:
                if not (c.isalpha() or c.isdigit() or c == ' '):
                    resi2 = True
                    break

            if length > 3:
                print("Invalid Name (Name has less than 2 later)")
            else:
                x = 7
            if resi1 is True:
                print("Invalid Name ( name has number in it)")
                fullName = ''
            else:
                x = 7

            if resi2 is True:
                print("Invalid Name (name is containing special special) ")
                fullName = ''
            else:
                x = 7

        # It's for checking username validation

        x = 5
        while x == 5:
            userName = input("Choose User Name : ")
            tes4 = len(userName)

            tes1 = False
            for ele in userName:
                if ele.isupper():
                    tes1 = True
                    break

            tes2 = False
            for c in userName:
                if not (c.isalpha() or c.isdigit() or c == ' '):
                    tes2 = True
                    break

            tes3 = False
            for ele in userName:
                if ele.isspace():
                    tes3 = True
                    break

            if tes1 is True:
                print("Username should not be in Uppercase ")
                userName = ''

            if tes2 is True:
                print("Username should not contain special characters")
                userName = ''

            if tes3 is True:
                print("Username should not contain space")
                userName = ''

            if tes4 < 8:
                print("Username should be contain more than 8 character")
                userName = ''
            x = 7

        # It is for checking password validation

        x = 5
        while x == 5:
            userPass = input("Choose Password : ")
            lent = len(userPass)

            res1 = False
            for ele in userPass:
                if ele.isupper():
                    res1 = True
                    break

            res2 = False
            for ele in userPass:
                if ele.islower():
                    res2 = True
                    break

            res3 = False
            for c in userPass:
                if not (c.isalpha() or c.isdigit() or c == ' '):
                    res3 = True
                    break

            res4 = False
            for ele in userPass:
                if ele.isspace():
                    res4 = True
                    break

            res5 = False
            for ele in userPass:
                if ele.isdigit():
                    res5 = True
                    break

            if lent < 7:
                print("Your Password is too short")
                userPass = ''
            else:
                x = 7

            if res1 is False:
                print("Your Password has no Uppercase")
                userPass = ''
            else:
                x = 7

            if res2 is False:
                print("Your Password has no Lowercase")
                userPass = ''
            else:
                x = 7

            if res3 is False:
                print("Your Password has no Special Character")
                userPass = ''
            else:
                x = 7

            if res4 is True:
                print("Your Password has a Space")
                userPass = ''
            else:
                x = 7

            if res5 is False:
                print("Your Password has no Digits")
                userPass = ''
            else:
                x = 7
    print(userName)
    print(userPass)
    print(fullName)

    # It is login page code below here ///

    if op == 1:
        # It is for Login page
        print("")

        user = input("Enter User Name : ")
        pass_ = input("Enter Password : ")

        if user == userName:
            if pass_ == userPass:

                print(fullName)
                print("Your Result is down below :")
                print("Maths == 67%")
                print("Maths == 67%")
                print("Maths == 67%")
                print("Maths == 67%")
            else:
                print("Do you want to Reset Password")
                passReset = "Say 'Yes' or 'No'"
                if passReset == 'yes' or passReset == 'Yes' or passReset == 'YES':
                    studentId1 = input("Enter your Student ID : ")
                    if studentId1 == studentId:
                        otpValidation = input("Enter the otp : ")
                        if otpValidation == otp:
                            userPass = input("Enter your new pass word")
                        else:
                            print("OTP wrong !!")
                    else:
                        print("wrong Student ID")
                else:
                    print("Want Hint ??")
                    pasHint = input("Say 'Yes'")
                    if pasHint == 'Yes' or pasHint == 'yes' or pasHint == 'YES':
                        print("Hnt")

        else:
            print("Do you want to Reset Username :")

print("Press (10 ) to Exit : ")
