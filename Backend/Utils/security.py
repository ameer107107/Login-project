import json
import bcrypt

with open("../data.json","r") as file:
    data = json.load(file)

risk = 0

# function
def Block():
    data["user"]["account_status"] = False
    with open("../data.json", "w") as file:
        json.dump(data, file, indent=4)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def save_user(user, file_path):
    with open(file_path, "w") as f:
        json.dump(user, f, indent=4)


def create_user(username, email, phone, password, file_path):
    user = {
        "username": username,
        "email": email,
        "phone": phone,
        "password": hash_password(password),
        "account_status": True
    }

    save_user({"user": user}, file_path)


def calculate_risk(risk,user_name,check_name,login_failed,attempts):
    if not bcrypt.checkpw(check_password, user_password):
        risk += 3

    if user_name != check_name:
        risk += 2

    if login_failed >= 3:
        risk += 1

    if attempts >= 5:
        risk += 1
    return risk


def make_decision(risk):

    if risk >=10:
        print("Blocked ⛔")
        Block()

    elif risk >=5:
        print("OTP Required 🔐")

    else:
        print("Normal ✅")



# user info from the UI
input_User={

    "user_name":"karar123",
    "user_email":"karar554@gmail.com",
    "user_phone":"+9647779830399",
    "user_password":"1234567",

}


# input info
check_name = input_User["user_name"]
check_password = input_User["user_password"].encode()



# data info
user_name = data["user"]["username"]
user_password = data["user"]["password"].encode()
user_active = data["user"]["account_status"]



# activity info
login_failed = data["login_activity"]["failed_attempts"]
attempts = data["login_activity"]["total_attempts"]



# info test
if user_active:

    risk = calculate_risk(risk,user_name,check_name,login_failed,attempts)
    make_decision(risk)

else:
    print("you have been blocked contact support for help 🔐")
