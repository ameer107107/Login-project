import json


with open("../data.json","r") as file:
    data = json.load(file)


# user info from the UI
input_User={
    "user_name":"karar123",
    "user_email":"karar554@gmail.com",
    "user_phone":"+9647779830399",
    "user_password":"1234567",
}

suspect = 0

# input info
check_name = input_User["user_name"]
check_email = input_User["user_email"]
check_phone = input_User["user_phone"]
check_password = input_User["user_password"]

# data info
user_name = data["user"]["username"]
user_email = data["user"]["email"]
user_phone = data["user"]["phone"]
user_password = data["user"]["password"]
user_active = data["user"]["account_status"]

# activity info
login_attempts = data["login_activity"]["successful_attempts"]
login_failed = data["login_activity"]["failed_attempts"]
attempts = data["login_activity"]["total_attempts"]
# info test
if user_active:
    if user_name != check_name:
        suspect +=15
    if user_email != check_email:
        suspect +=20
    if user_phone != check_phone:
        suspect +=25
    if user_password != check_password:
        suspect +=30
    if login_failed > 2:
        suspect +=40
    if attempts > 3:
        suspect +=10

    # The decisions
    if suspect >=80:
        data["user"]["account_status"] = False
        with open("../data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Blocked ⛔")

    elif suspect >=50:
        print("The account has been suspected OTP 🔐")

    else:
        print("Normal ✅")
else:
    print("you have been blocked contact support 🔐")