import json
import atexit
import bcrypt




class User:
    users_list = []
    def __init__(self,firstname,lastname,email,password,account_state=True):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.account_state = account_state
    @classmethod
    def email_exists(cls, email):
        for user in cls.users_list:
            if user.email == email:
                return True
        return False

    @classmethod
    def verify_credentials(cls, email, password):
        for user in cls.users_list:
            if user.email == email and user.password == password:
                return True
        return False

    def add_to_list(self):
        User.users_list.append(self)

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "account_state": self.account_state
        }

    def display_user(self):
        print(f"firstname: {self.firstname}")
        print(f"lastname: {self.lastname}")
        print(f"email: {self.email}")
        print(f"password: hash password: {self.password}")
        print(f"account state: {self.account_state}")

    @classmethod
    def save_to_json(cls):
        data = {"users": []}
        for user in cls.users_list:
            data["users"].append(user.to_dict())

        with open('data.json', "w") as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_json(cls):
        cls.users_list = []
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                if "users" in data:
                    for u in data["users"]:
                        user = cls(u["firstname"], u["lastname"], u["email"], u["password"], u.get("account_state", True))
                        cls.users_list.append(user)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
 

User.load_from_json()
print("عدد المستخدين في القائمة بعد التحميل من الملف:", len(User.users_list))
atexit.register(User.save_to_json)

for user in User.users_list:
    user.display_user()