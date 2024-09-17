on_off = True

while on_off:
    year = float(input("What's the year?\n>"))
    if year % 100 != 0 and year % 4 == 0:
        print("It's a leap year.")
    elif year % 100 == 0 and year % 400 == 0:
        print("It's a leap year.")
    else:
        print("It's not a leap year.")

    op = input("Do you want to continue, write either 'y' or 'n'\n>")
    if op == "y":
        on_off = True
    elif op == "n":
        on_off = False
    else:
        print("Be a good person 😝😒")
        on_off = False





# Which year do you want to check?
# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")