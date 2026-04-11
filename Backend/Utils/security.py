import json
import bcrypt

with open("../data.json","r") as file:
    data = json.load(file)



# function
def Block():
    data["user"]["account_status"] = False
    with open("../data.json", "w") as file:
        json.dump(data, file, indent=4)


# user info from the UI
input_User={
    "user_name":"karar123",
    "user_email":"karar554@gmail.com",
    "user_phone":"+9647779830399",
    "user_password":"1234567",
}

risk = 0

# input info
check_name = input_User["user_name"]
check_password = input_User["user_password"]

# data info
user_name = data["user"]["username"]
user_password = data["user"]["password"].encode()
user_active = data["user"]["account_status"]

# activity info
login_failed = data["login_activity"]["failed_attempts"]
attempts = data["login_activity"]["total_attempts"]

# info test
if user_active:

    if user_name != check_name:
        risk +=0.1

    if not bcrypt.checkpw(check_password.encode(), user_password.encode()):
        risk +=0.2

    if login_failed > 2:
        risk +=0.5

    if attempts > 3:
        risk +=0.3

    # The decisions
    if login_failed >= 5:
        print("you have blocked ⛔ (Too many failed attempts)")
        Block()

    elif user_name != check_name and login_failed >= 3 :
        print("you have blocked ⛔ (Suspicious behavior)")
        Block()

    elif risk >=0.8:
        print("Blocked ⛔")
        Block()

    elif risk >=0.5:
        print("OTP Required 🔐")


    else:
        print("Normal ✅")
else:
    print("you have been blocked contact support for help 🔐")
