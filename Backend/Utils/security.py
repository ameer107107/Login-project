import json
import bcrypt

with open("../data.json","r") as file:
    data = json.load(file)


# function
def block():
    data["user"]["account_status"] = False
    with open("../data.json", "w") as file:
        json.dump(data, file, indent=4)

def remove_block():
    data["user"]["account_status"] = True
    with open("../data.json", "w") as file:
        json.dump(data, file, indent=4)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def save_user(user):
    with open("../data.json", "w") as f:
        json.dump(user, f, indent=4)


def create_user(username, email, phone, password):
    user = {
        "username": username,
        "email": email,
        "phone": phone,
        "password": hash_password(password),
        "account_status": True
    }

    save_user({"user": user})


def calculate_risk(user_name,check_name,password_result
                   ,login_failed,attempts):
    risk = 0
    if not password_result:
        risk += 5

    if user_name != check_name:
        risk += 1

    if login_failed <= 2:
        risk += 0

    elif login_failed <= 5:
        risk += 2

    else:
        risk += 4

    if attempts <= 3:
        risk += 0

    elif attempts <= 4:
        risk += 1

    else:
        risk += 3


    return risk


def make_decision(risk):

    if risk >=8:
        print("Blocked ⛔")
        block()

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

password_result = bcrypt.checkpw(check_password, user_password)

# info test
if not user_active:
    print("you have been blocked contact support for help 🔐")

else:
    risk = calculate_risk(user_name, check_name, password_result, login_failed, attempts)
    make_decision(risk)
    print(risk)
