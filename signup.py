def signup(username, password):
    if not username:
        return "Username is required"
    if len(password) < 6:
        return "Password must be at least 6 characters"
    return "Signup successful!"
print("===== USER SIGNUP =====")
username = input("Enter username: ")
password = input("Enter password: ")
result = signup(username, password)
print(result)
