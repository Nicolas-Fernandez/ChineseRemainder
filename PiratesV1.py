# -*- coding: cp1252 -*-

import random

print ("Vous �tiez cuisinier sur un navire de sanguinaires Pirates !")
nbPirates1 = int (input ("Vous souvenez-vous de combien de Pirates y'avait il sur ce navire ?"))

print("")
print ("Apr�s leur derni�re rapille, les"), (nbPirates1), ("forbants d�cident enfin de se partager leur magot...")
print ("Le cofre contient un nombre entier inconnu de pi�ces d'or de m�me valeure.")

print("")
print ("Ils se partagent de fa�on �quitable les pi�ces, mais il en leur reste un peu.")
print ("Dans leur grande magnanimit�, ils d�cident de vous offrir ses pi�ces restantes !")
reste1 = int (input ("Combien de pi�ce aviez vous re�u ?"))

print("")
print ("Mais une mutinerie �clatte alors, faisant de nombreuses victimes...")
nbPirates2 = nbPirates1 - int (input ("Combien de Pirates sont mort lors de ce tragique �v�nement ?"))

print("")
print ("Les"), (nbPirates2), ("survivants se partagent � nouveau de fa�on �quitable TOUTES les pi�ces, mais il en leur reste encore un peu.")
print ("Dans leur grande mansu�tude, ils d�cident de vous offrir ses pi�ces restantes !")
reste2 = int (input ("Combien de pi�ce aviez vous re�u cette fois-ci ?"))

print("")
print ("Mais voil� qu'une terrible temp�te �clatte et que le vaisseau se fracasse sur des rochers...")
nbPirates3 = int (input ("Vous avez surv�cu ! Echou� sur la plage, combien de Pirates retrouvez vous � vos cot�s ?"))

print("")
print ("Les"), (nbPirates3), ("restants, se partagent une nouvelle fois de fa�on �quitable TOUTES les pi�ces, mais il en leur reste toujours un peu.")
print ("Dans leur grande bont�, ils d�cident de vous offrir ses pi�ces restantes !")
reste3 = int (input ("Combien de pi�ce aviez vous re�u apr�s ce d�rnier partage ?"))

print("")
print ("Et alors que vous pr�parer un d�licieux ragoux de tortue � la noix de coco...")
print ("Vous vous demandez combien de pi�ces d'or vous pourriez r�cup�rer au minium...")
print ("Si vous empoisogniez c'est malheureux rescap�s !")
print ("")
reponse = int (input ("C'est vrai �a... Combien de pi�ces ce myst�rieux coffre contenait-il donc ?"))


lastModulo = nbPirates1 * nbPirates2 * nbPirates3
print ("Congruance ="), (lastModulo)

inconnu1 = nbPirates2 * nbPirates3
while (inconnu1 % nbPirates1) != 1:
        inconnu1 = inconnu1 * 2
	
inconnu2 = nbPirates1 * nbPirates3
while (inconnu2 % nbPirates2) != 1:
        inconnu2 = inconnu2 * 2	

inconnu3 = nbPirates1 * nbPirates2
while (inconnu3 % nbPirates3) != 1:
        inconnu3 = inconnu3 * 2

tresor = (inconnu1 * reste1 + inconnu2 * reste2 + inconnu3 * reste3) % lastModulo

if reponse == tresor:
	print("")
	print ("F�licitation, il y avait bien au moins"), (tresor), ("pi�ces d'or dans ce coffre !")
	print ("Avez vous mis en action votre plan machiavelic ? Seul vous poss�dez la r�ponse...")
else:
	print("")
	print ("Et non, vous vous �tes tromp�... Il y avait au moins"), (tresor), ("pi�ces d'or dans ce coffre...")
	print ("Mais, avez vous mis pour autant en r�alis� votre sinistre projet ? Seul vous poss�dez la r�ponse...")

print("")
print ("Aurevoir !")
