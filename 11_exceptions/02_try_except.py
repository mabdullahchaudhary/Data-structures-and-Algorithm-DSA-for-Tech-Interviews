menu = {"salad": 30, "rice": 400, "Qima Rice": 500, "Biryani": 360}

# try:
#     print(menu["Kabab"])
# except KeyError as e:
#     print("Sorry this Item not found in our database",e)
# finally:
#     print("Next Customer")

# print("Hello this text comes after all happend")

print(menu.get("Kabab","Item not found there"))