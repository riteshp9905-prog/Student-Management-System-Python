USERNAME = "admin"
PASSWORD = "1234"

MAX_ATTEMPTS = 3


def login():

    print("\n========== LOGIN ==========")

    attempts = MAX_ATTEMPTS

    while attempts > 0:

        username = input("Username : ")
        password = input("Password : ")

        if username == USERNAME and password == PASSWORD:
            print("\n✅ Login Successful!\n")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"\n❌ Invalid Username or Password!")
            print(f"Attempts Left : {attempts}\n")

    print("\n🚫 Too many failed attempts!")
    print("Program Closed.\n")

    return False