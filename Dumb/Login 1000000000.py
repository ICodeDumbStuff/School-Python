#imports
import time
import random

#Login Data place
login_data = {"hi":"hi","lo":"lo"}

#Grab Files
songs = {"":"", "":""}


#functions
def login(user, password):
    if user in login_data:
        print(True)

login_un = input("Please Login,\nUsername: ")
login_ps = input("Password: ")
login(login_un, login_ps)
login_data.update({"lo":"lo2"})