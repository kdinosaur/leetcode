name = input("please enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
elif age == 17:
    print("Please come back in {0} year".format(18-age))
else:
    print("Please come back in {0} years".format(18-age))
