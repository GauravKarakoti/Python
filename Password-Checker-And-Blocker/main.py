our_password = "pass1234"
your_answer = ""
number_of_try = 0
max_number_of_try = 8
Max_try = "Not Reached"
while your_answer != our_password and Max_try != "Reached":
    if number_of_try < max_number_of_try:
        your_answer = input("What is the Password?\n")
        number_of_try = number_of_try + 1
        if your_answer != our_password:
            print("Wrong!!")
    else:
        Max_try = "Reached"
if Max_try == "Reached":
    print("Account Blocked")
else:
    print("Access Granted")