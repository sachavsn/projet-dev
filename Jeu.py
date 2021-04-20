#Projet dev

ChoixClass = False
Attack = 0
Defence = 0
Speed = 0
Health = 20
Knives = 10
Arrows = 10
inv = "a torch"

print("Il était une fois dans un passé lointain et fantastique, une bataille se déroulait entre deux grands royaumes ou nul des deux ne remporta la victoire. C’est alors que votre aventure commence !")
print("Vous vous réveillez au milieu d'un tas de cadavres. Vous n'avez aucun souvenir de qui vous êtes ni de l'endroit où vous vous trouvez. C’est alors qu’un homme vêtu d’habit blanc taché de sang s’approche de vous.")

print("Médecin : “ Qui êtes vous !?”")
Name = input('Votre Nom: ')
print(Name,': Je suis', Name)

print('Médecin : “ Mais que faites-vous ici?')
print('Choix de Classe')

print('Knight - A well rounded class with no certain advantage in any category, fights with a sword and metal armor')
print('Archer - Good with a bow and has amazing speed but wears light metal armor')
print('Mage - Can cast spells with a magic staff and can deal high amounts of damage but wears only cloth armor')
print('Rogue - A master of deception and very quick on thier feet, can deal devistating blows with a dagger and throwing knives')

while ChoixClass == False:
    Class = input('Nom de votre classe parmis les 4 proposé: ')
    #classe a mettre dans bdd ?
    if Class.lower() == "knight":
        Attack = 10
        Defence = 10
        Speed = 10
        print('Tu as choisi Knight')
        ChoixClass = True
    elif Class.lower() == "archer":
        Attack = 10
        Defence = 3
        Speed = 8
        print('Tu as choisi Archer')
        ChoixClass = True
    elif Class.lower() == "mage":
        Attack = 15
        Defence = 1
        Speed = 8
        print('Tu as choisi Mage')
        ChoixClass = True
    elif Class.lower() == "rogue":
        Attack = 10
        Defence = 2
        Speed = 15
        print('Tu as choisi Rogue')
        ChoixClass = True
    else:
        print("Ce n'est pas une classe.")


print("Médecin: “Je n’y crois pas mes yeux, vous étiez pourtant mort transpercé par une lance ! Le pays tout entier souffre de la guerre actuel, plus personne n'est la pour protéger")
print("les villages et les habitants. Je ne peux pas vous garder pour vous examiner à cause de cette guerre. Prenez ce que vous voulez dans l'armurie, ce sont tout les") 
print("équipements des soldats morts.")


#demande l'etape de jeu ou le joueur est:
#Va chercher l'étape et les possibilité de choix dans je json
#boucle while

"""while etape == 1):
    if etape == 1 :
        print("histoire dans le json lié à l'id 1")
        second = input("Qu'allez vous faire?")

        if second.lower() == ("proposition a dans le json lié à l'id 1"):
            print("---------------------------------------------------------")
            etape=+1
            print("Ce qu'il se passe en choisissant ce choix.")
        else second.lower() == ("proposition b dans le json lié à l'id 1"):
            print("---------------------------------------------------------")
            etape=+2
            print("Ce qu'il se passe en choisissant ce choix.")"""
