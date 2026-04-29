import json
import bcrypt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data.json")

with open(DATA_PATH, "r") as file:
    data = json.load(file)


def use_data(check_email):
    with open(DATA_PATH, "r") as file:
        data = json.load(file)

        for user in data["users"]:
            if user["email"] == check_email:
                return {
                    "user_name": user["firstname"],
                    "user_email": user["email"],
                    "user_password": user["password"].encode(),
                    "user_active": user["account_state"],
                    "login_failed": user.get("failed_attempts", 0),
                    "attempts": user.get("total_attempts", 0)
                }
    return None



def save_data():
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)


def rest_attempt(email):
    for user in data["users"]:
        if user["email"] == email:
            user["total_attempts"] = 0
            user["failed_attempts"] = 0
            user["successful_attempts"] = 0
            break
    save_data()


def faild_attempt(email):
    for user in data["users"]:
        if user["email"] == email:
            user["failed_attempts"] += 1
            user["total_attempts"] += 1
            break
    save_data()

def successful_attempt(email):
    for user in data["users"]:
        if user["email"] == email:
            user["successful_attempts"] += 1
            user["total_attempts"] += 1
            break
    save_data()


def block(email):
    for user in data["users"]:
        if user["email"] == email:
            user["account_state"] = False
            break
    save_data()
    return {
        "account_state":False

            }

def remove_block(email):
    for user in data["users"]:
        if user["email"] == email:
            user["account_state"] = True
            break
    save_data()
    rest_attempt(email)
    return {"account_state": True}

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def calculate_risk(input_password,check_email):

    enter_flag = False
    risk = 0

    data = use_data(check_email)

    account_activ = data["user_active"]


    if account_activ:

        password_result = bcrypt.checkpw(input_password.encode(), data["user_password"])

        if not password_result:
            risk += 4
            enter_flag = True


        if data["user_email"] != check_email:
            risk += 3
            enter_flag = True


        if data["login_failed"] <= 2:
            risk += 0

        elif data["login_failed"] <= 5:
            risk += 2

        elif data["login_failed"] <= 8:
            risk += 3

        elif data["login_failed"] <= 10:
            risk += 4

        else:
            risk += 10

        if data["attempts"] <= 3:
            risk += 0

        elif data["attempts"] <= 4:
            risk += 1

        else:
            risk += 3


    return risk,enter_flag,account_activ


def make_decision(risk,enter_flag,account_activ,email):
    if account_activ:
        if risk >=10:
            block(email)
            print("Block")
            return {
                "account_state":False,
                "risk":risk
            }

        elif enter_flag:

            faild_attempt(email)
            print("There is ERROR in th email or password. 🔐")
            return {
                "account_state": account_activ,
                "msg":"There is ERROR in th email or password. 🔐",
                "risk": risk
            }

        else:

            rest_attempt(email)
            successful_attempt(email)
            print("succeeded")
            return {
                "account_state": account_activ,
                "msg":"succeeded",
                "risk": risk
            }
    else:
        print("you have been Blocked")
        return {
            "account_state":account_activ
        }


#check_name="karar123"
check_password=1234567
check_password = str(check_password)
check_email="karar554@gmail.com"

def returns(check_password,check_email):
    risk,enter_flag,account_activ = calculate_risk(check_password,check_email)
    result = make_decision(risk,enter_flag,account_activ,check_email)
    return result

returns(check_password,check_email)