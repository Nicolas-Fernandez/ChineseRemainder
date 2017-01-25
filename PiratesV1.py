import random

print ("")
print ("You are a poor chinese slave cook on a bloodthirsty pirates ship.")
NBPIRATES1 = int (input ("How many pirates on this ship?   "))

print("")
print ("After their last ritual,", (NBPIRATES1), "the forbans finally decided to share their magot ...")
print ("The chest contains an integer x of gold coins.")
print ("They share these coins fairly, but there is a little left.")
print ("In their great magnanimity, they decide to offer you his remaining pieces!")
REMAIN1 = int (input ("How many coins did you receive?"))

print("")
print ("But a mutiny broke out then, making many victims ...")
NBPIRATES2 = NBPIRATES1 - int (input ("How many pirates died in this tragic event?   "))

print("")
print ("The"), (NBPIRATES2), ("survivors again share fairly ALL the coins, but they still have a few more.")
print ("In their great mansuetude, they decide to offer you again this remaining pieces!")
REMAIN2 = int (input ("How many coins did you receive this time?   "))

print("")
print ("But now a terrible storm breaks out and the ship crashes on rocks ...")
NBPIRATES3 = int (input ("You survived! Stranded on the beach, how many pirates find you by your side?"))

print("")
print ("The"), (NBPIRATES3), ("remaining pirates, again share fairly ALL the pieces, but they still have a little bit of them.")
print ("In their great kindness, they decide to offer you again this remaining pieces!")
REMAIN3 = int (input ("How many coins did you receive after this last disbursement?   "))

print("")
print ("And while you prepare a delicious coconut turtle ragout ...")
print ("you wonder how many gold coins you can get at least ... ")
print ("if you poison this unfortunate survivors!")
print ("")
ANSWER = int (input ("Is that true ... How many pieces does this mysterious chest contain?"))


LASTMODULO = NBPIRATES1 * NBPIRATES2 * NBPIRATES3
print ("Congruance ="), (LASTMODULO)

UNKNOW1 = NBPIRATES2 * NBPIRATES3
while (UNKNOW1 % NBPIRATES1) != 1:
        UNKNOW1 = UNKNOW1 * 2
	
UNKNOW2 = NBPIRATES1 * NBPIRATES3
while (UNKNOW2 % NBPIRATES2) != 1:
        UNKNOW2 = UNKNOW2 * 2	

UNKNOW3 = NBPIRATES1 * NBPIRATES2
while (UNKNOW3 % NBPIRATES3) != 1:
        UNKNOW3 = UNKNOW3 * 2

TREASURE = (UNKNOW1 * REMAIN1 + UNKNOW2 * REMAIN2 + UNKNOW3 * REMAIN3) % LASTMODULO

if ANSWER == TREASURE:
	print("")
	print ("Congratulations, there was at least"), (TREASURE), ("gold coins in this chest!")
	print ("Have you put into action your machiavelic plan? Only you have the answer ...")
else:
	print("")
	print ("And no, you were wrong ... There was at least"), (TREASURE), ("gold coins in this chest ...")
	print ("But, do you have to realize your sinister project? Only you have the answer ...")

print("")
print("Press enter key to close this game.")
print ("Bye!")
CLOSE = input ()
