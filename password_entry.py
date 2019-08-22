"""Matthew Nielsen"""
min_length = 5
password = input("Enter Password: ")
password_length = len(password)
while password_length < min_length:
    print("Error password must be at least 5 characters long")
    password = input("Enter Password: ")
for letter in range(0, password):
    print("*")
