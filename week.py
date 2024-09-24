s = input("What day of the week is it?: " )
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in week:
    if i == s:
        print(f" Happy {s} !")
        break
    else:
        print("That is not a valid Day of the week")

