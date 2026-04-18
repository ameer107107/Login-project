import json
class User:
    users_list = []
    def __init__(self,username,email,password,account_state=True):
        self.username = username
        self.email = email
        self.password = password
        self.account_state = account_state
    @classmethod
    def email_exists(cls, email):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
        except:
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
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "account_state": self.account_state
        }

    def display_user(self):
        print(f"username: {self.username}")
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








