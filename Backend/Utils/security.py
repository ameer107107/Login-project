import json
import bcrypt
import security_utilss as ut


with open("../data.json","r") as file:
    data = json.load(file)

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
check_email = input_User["user_email"]
check_phone = input_User["user_phone"]

with open("../data.json","r") as file:
    data = json.load(file)


def save_data():
    with open("../data.json","w") as file:
        json.dump(data, file, indent=4)


def rest_attempt():
    data["login_activity"]["total_attempts"] = 0
    data["login_activity"]["failed_attempts"] = 0
    data["login_activity"]["successful_attempts"] = 0
    save_data()


def faild_attempt():
    data["login_activity"]["failed_attempts"] += 1
    data["login_activity"]["total_attempts"] += 1
    save_data()

def successful_attempt():
    data["login_activity"]["successful_attempts"] += 1
    data["login_activity"]["total_attempts"] += 1
    save_data()


def block():
    data["user"]["account_status"] = False
    save_data()
    return {
        "account_status":data["user"]["account_status"]

            }

def remove_block():
    data["user"]["account_status"] = True
    save_data()
    rest_attempt()
    return {
        "account_status": data["user"]["account_status"]

    }

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()



def calculate_risk(user_name,check_name,password_result
                   ,login_failed,attempts):
    risk = 0
    if not password_result:
        risk += 5


    elif user_name != check_name:
        risk += 1


    if check_email != user_email:
        risk += 5


    if login_failed <= 2:
        risk += 0

    elif login_failed <= 5:
        risk += 2

    elif login_failed <= 8:
        risk += 3

    elif login_failed <= 10:
        risk += 4

    else:
        risk += 10

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
        print("There is ERROR in th email or password. 🔐")
        faild_attempt()

    else:
        print("succeeded ✅")
        rest_attempt()
        successful_attempt()



# data info
user_name = data["user"]["username"]
user_password = data["user"]["password"].encode()
user_active = data["user"]["account_status"]
user_email = data["user"]["email"]

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

