import random
sentance = input("Enter a sentance containing 10 charecters long: ")
if len(sentance) == 10:
    for x in range(11):
        print(sentance[0:x])
        lsentance=list(sentance)
        random.shuffle(lsentance)
    print(("Randomised: ")+ "".join(lsentance))
elif len(sentance)>10:
    print ("String too long")
elif len(sentance)<10:
    print ("String too short")


