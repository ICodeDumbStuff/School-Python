'''
not_my_list = [1,2,3,4,5,6,7,8,9,10]
half = len(not_my_list)//2
midpoint = not_my_list[half]
split1 = midpoint[0:half]
split2 = midpoint[half:]
print(split1, split2)

find = 7

if midpoint != find:
    pass
else:
    print("Correct")
'''

def cool(yes=6,):
    """
    Testing Text
    yes is nullable
    """
    return yes
print(cool(4))