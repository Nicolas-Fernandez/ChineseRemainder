# -*- coding: cp1252 -*-

import random

print ("Vous étiez cuisinier sur un navire de sanguinaires Pirates !")
nbPirates1 = int (input ("Vous souvenez-vous de combien de Pirates y'avait il sur ce navire ?"))

print("")
print ("Après leur dernière rapille, les"), (nbPirates1), ("forbants décident enfin de se partager leur magot...")
print ("Le cofre contient un nombre entier inconnu de pièces d'or de même valeure.")

print("")
print ("Ils se partagent de façon équitable les pièces, mais il en leur reste un peu.")
print ("Dans leur grande magnanimité, ils décident de vous offrir ses pièces restantes !")
reste1 = int (input ("Combien de pièce aviez vous reçu ?"))

print("")
print ("Mais une mutinerie éclatte alors, faisant de nombreuses victimes...")
nbPirates2 = nbPirates1 - int (input ("Combien de Pirates sont mort lors de ce tragique évènement ?"))

print("")
print ("Les"), (nbPirates2), ("survivants se partagent à nouveau de façon équitable TOUTES les pièces, mais il en leur reste encore un peu.")
print ("Dans leur grande mansuétude, ils décident de vous offrir ses pièces restantes !")
reste2 = int (input ("Combien de pièce aviez vous reçu cette fois-ci ?"))

print("")
print ("Mais voilà qu'une terrible tempête éclatte et que le vaisseau se fracasse sur des rochers...")
nbPirates3 = int (input ("Vous avez survécu ! Echoué sur la plage, combien de Pirates retrouvez vous à vos cotés ?"))

print("")
print ("Les"), (nbPirates3), ("restants, se partagent une nouvelle fois de façon équitable TOUTES les pièces, mais il en leur reste toujours un peu.")
print ("Dans leur grande bonté, ils décident de vous offrir ses pièces restantes !")
reste3 = int (input ("Combien de pièce aviez vous reçu après ce dérnier partage ?"))

print("")
print ("Et alors que vous préparer un délicieux ragoux de tortue à la noix de coco...")
print ("Vous vous demandez combien de pièces d'or vous pourriez récupérer au minium...")
print ("Si vous empoisogniez c'est malheureux rescapés !")
print ("")
reponse = int (input ("C'est vrai ça... Combien de pièces ce mystérieux coffre contenait-il donc ?"))


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
	print ("Félicitation, il y avait bien au moins"), (tresor), ("pièces d'or dans ce coffre !")
	print ("Avez vous mis en action votre plan machiavelic ? Seul vous possédez la réponse...")
else:
	print("")
	print ("Et non, vous vous êtes trompé... Il y avait au moins"), (tresor), ("pièces d'or dans ce coffre...")
	print ("Mais, avez vous mis pour autant en réalisé votre sinistre projet ? Seul vous possédez la réponse...")

print("")
print ("Aurevoir !")
