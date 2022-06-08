import random
from random import shuffle

name = input("Enter a name: ")
kwc = int(input("Enter your keyword count: "))
kwlist = []
spchar = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', '+'])
spchar2 = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', '+'])
num = random.randint(0, 9)
num = str(num)
num2 = random.randint(0, 9)
num2 = str(num2)
passs = ""

if kwc in range(6):
    while kwc != 0:
        kw = input("Enter a unique keyword below 10 characters: ")
        if len(kw) < 11:
            kwlist.append(kw)
            kwc -= 1
        else:
            print("Keyword", kw, "not added in password because of too many characters")
    kbstick = len(kwlist) - 1
    while kbstick >= 0:
        kwlist[kbstick] = str.upper(kwlist[kbstick])
        kbstick = kbstick - 2
    spcharint = str.upper(input("Would you like to input special character?(y/n): "))
    if spcharint[0] == "Y":
        userspchar = input("Enter a special character: ")
        kwlist.append(userspchar[0])
    else:
        kwlist.extend(spchar)
        kwlist.extend(spchar2)
    kwlist.append(num)
    kwlist.append(num2)
    shuffle(kwlist)
    for i in range(0, len(kwlist)):
        passs = passs + kwlist[i]
    pass_limit = int(input("Enter the password length: "))
    if 0 < pass_limit <= 99:
        while len(passs) != pass_limit:
            if len(passs) > pass_limit:
                passs = passs.rstrip(passs[-1])
            else:
                adds = random.randint(0, 9)
                adds = str(adds)
                passs = passs + adds
    else:
        print("Password limit is set to 16 as password cannot be too high or too low")
        pass_limit = 16
        while len(passs) != pass_limit:
            if len(passs) > pass_limit:
                passs = passs.rstrip(passs[-1])
            else:
                adds = random.randint(0, 9)
                adds = str(adds)
                passs = passs + adds
    print("Your Freshly generated password: ", passs)
    with open("history.txt", "a") as o:
        o.write("\n")
        o.write(str.upper(name))
        o.write(" has generated password: ")
        o.write(passs)
else:
    print("Invalid keyword count, Try again")