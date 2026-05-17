import bcrypt


def rest_attempt(user):

    user.total_attempts = 0
    user.failed_attempts = 0
    user.successful_attempts = 0




def faild_attempt(user):

    user.failed_attempts += 1
    user.total_attempts += 1


def successful_attempt(user):

    user.successful_attempts += 1
    user.total_attempts += 1


def block(user):

    user.account_state = False



def remove_block(user):

    user.account_state = True





def calculate_risk(user,check_password,check_email):

    enter_flag = False
    risk = 0


    if user.account_state:

        password_result = bcrypt.checkpw(
            check_password.encode(),
            user.password.encode()
        )

        if not password_result:
            risk += 4
            enter_flag = True


        if user.email != check_email:
            risk += 4
            enter_flag = True


        if user.failed_attempts <= 2:
            risk += 0

        elif user.failed_attempts <= 5:
            risk += 2

        elif user.failed_attempts <= 8:
            risk += 3

        elif user.failed_attempts <= 10:
            risk += 4

        else:
            risk += 10

        if user.total_attempts <= 3:
            risk += 0

        elif user.total_attempts <= 4:
            risk += 1

        else:
            risk += 3


    return risk,enter_flag


def make_decision(user,risk,enter_flag):
    if user.account_state:
        if risk >=10:
            block(user)
            print("Block")

            return {
                "account_state":False,
                "risk":risk
            }

        elif enter_flag:

            faild_attempt(user)

            print("There is wrong in th email or password.")

            return {
                "account_state": user.account_state,
                "msg":"There is wrong in the email or password.",
                "risk": risk
            }

        else:

            rest_attempt(user)
            successful_attempt(user)

            print("succeeded")

            return {
                "account_state": user.account_state,
                "msg":"succeeded",
                "risk": risk
            }
    else:
        print("you have been Blocked")
        return {
            "account_state":False,
            "msg":"you have been Blocked"
        }




def returns(user,check_password,check_email,):

    if not user.account_state:
        return {
            "account_state": False,
            "msg": "you have been blocked"
        }
    else:
        risk,enter_flag = calculate_risk(
            user,
            check_password,
            check_email,
        )

        result = make_decision(
            user,
            risk,
            enter_flag,
            )
    
        return result
