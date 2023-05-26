'''
☻ »      This program took about a minute, if that      « ☻
☻ »                      09/05/2023                     « ☻
'''
valid = ["cool", "yes", "no u", "this is boring", "this", "took", "less", "than", "60", "seconds"]
def userCheck(username):
    if username in valid: return "valid"
    else: return "invalid"

print(userCheck(input("username\n-> ")))