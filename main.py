from random import randint
import time

print("© Radical06 at Boricraft Development")
print("https://github.com/Boricraft-Developmont")


monkeAmount = int(input("How many monkey?\n"))
i = 1
color = ""
generatedMonkeys = []

while i <= monkeAmount:
    print("Generating monke number {}".format(i))
    time.sleep(3)
    i += 1
    randomColor = randint(0, 3)
    if randomColor == 0:
        color = "black"
        print("You created a {} monke".format(color))
        generatedMonkeys.append(color)
    elif randomColor == 1:
        color = "white"
        print("You created a {} monke".format(color))
        generatedMonkeys.append(color)
    elif randomColor == 2:
        color = "grey"
        print("You created a {} monke".format(color))
        generatedMonkeys.append(color)
    elif randomColor == 3:
        color = "brown"
        print("You created a {} monke".format(color))
        generatedMonkeys.append(color)
    else:
        print("A monkey got stuck in the machine.")
    print("----------------------------------------------------")
    time.sleep(2)

print("Summary:")
print("----------------------------------------------------")
print("You generated a")
for monkey in generatedMonkeys:
    print(monkey + " monkey")
print("----------------------------------------------------")
print("Total: {}".format(monkeAmount))
    