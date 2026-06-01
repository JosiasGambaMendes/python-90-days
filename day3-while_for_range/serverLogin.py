while True:
    admin = input("Who Are You? ")
    if admin != "josias":
        continue
    password = input("Hello, josias. What's the Password? (It's a fish) ")
    if password == "nemo":
        break
print("Access Granted!")
