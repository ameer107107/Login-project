import json
import bcrypt



with open("../data.json","r") as file:
    data = json.load(file)


def use_data():
    with open("../data.json", "r") as file:
        data = json.load(file)

        user_name = data["user"]["username"]
        user_password = data["user"]["password"].encode()
        user_active = data["user"]["account_status"]
        user_email = data["user"]["email"]

        # activity info
        login_failed = data["login_activity"]["failed_attempts"]
        attempts = data["login_activity"]["total_attempts"]
        return {
            "user_name":user_name,
            "user_email":user_email,
            "user_password":user_password,
            "user_active":user_active,
            "login_failed":login_failed,
            "attempts":attempts
        }


# input info


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



def calculate_risk(check_password,check_email):

    enter_flag = False
    risk = 0

    data = use_data()
    account_activ = data["user_active"]
    password_result = bcrypt.checkpw(check_password.encode(),data["user_password"])
    if account_activ:
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


def make_decision(risk,enter_flag,account_activ):
    if account_activ:
        if risk >=10:
            block()
            print("Block")
            return {
                "account_status":False,
                "risk":risk
            }

        elif enter_flag:

            faild_attempt()
            print("There is ERROR in th email or password. 🔐")
            return {
                "account_status": account_activ,
                "msg":"There is ERROR in th email or password. 🔐",
                "risk": risk
            }

        else:

            rest_attempt()
            successful_attempt()
            print("succeeded")
            return {
                "account_status": account_activ,
                "msg":"succeeded",
                "risk": risk
            }
    else:
        print("you have been Blocked")
        return {
            "account_status":account_activ
        }


#check_name="karar123"
check_password=1234567
check_password = str(check_password)
check_email="karar554@gmail.com"

def returns(check_password,check_email):
    risk,enter_flag,account_activ = calculate_risk(check_password,check_email)
    result = make_decision(risk,enter_flag,account_activ)
    return result

returns(check_password,check_email)