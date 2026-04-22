import json
import atexit
class User:
    users_list = []
    def __init__(self,first_name,last_name,email,password,account_state=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.account_state = account_state
    @classmethod
    def email_exists(cls, email):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return False
        if "users"  in data:
            for user in data["users"]:
                if user["email"] == email:
                    return True

        return False

    def add_to_list(self):
        User.users_list.append(self)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "account_state": self.account_state
        }

    def display_user(self):
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"password: {self.password}")
        print(f"account state: {self.account_state}")

    @classmethod
    def save_to_json(cls):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except:
            data={'users':[]}

        if "users"  not in data:
            data["users"] = []

        for user in cls.users_list:
            data["users"].append(user.to_dict())

        with open('data.json', "w") as file:
            json.dump(data,file,indent=4)
        cls.users_list=[]

atexit.register(User.save_to_json)








