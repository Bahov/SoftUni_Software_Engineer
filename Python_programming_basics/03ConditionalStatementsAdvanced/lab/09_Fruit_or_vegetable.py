
product = str(input())

fruit_list = ["banana","apple","kiwi","cherry","lemon","grapes"]
vegetable_list = ["tomato","cucumber","pepper","carrot"]

if product in fruit_list:
    print("fruit")
elif product in vegetable_list:
    print("vegetable")
else:
    print("unknown")