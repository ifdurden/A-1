import json
def get_username():
    try :
        with open("username.json") as file :
            return json.load(file)
    except FileNotFoundError: 
        return None
def greet_user():
    name = get_username()
    if name:
        print(f"Welcome back {name}")
    else :
        username = input("Enter your name: ")
        with open("username.json" , "w") as file :
            username = json.dump(username , file)
            print(f"We will remember you name when you return {username}")


greet_user()