#Pas de base de données, pas de fichier !
#Le programme va :
#Demander le nom de la personne ( s'arrête avec Enter )
#Demander sa taille ( en centimètre )
#Demander son poids ( en kilo )
#Demander son sexe ( H / F )
#Ensuite le programme va :
#Calculer de l'IMC : formule = Poids / Taille2 de toutes les personnes
#Afficher la liste des personnes regroupée dans l'ordre de l'interprétation de l'IMC ( voir tableau suivant )
#IMC Interprétation
#+ de 40 obésité morbide ou massive
#35 à 40 obésité sévère
#30 à 35 obésité modérée
#25 à 30 surpoids
#18.5 à 25 corpulence normale
#16.5 à 18.5 maigreur
#- de 16.5 famine
#Un titre par catégorie
#Vous tester toutes les erreurs possibles d'encodage !
def askInfo() :
    global name, patients
    name = input("Entrez un nom : ")
    if name != "":
        size = input("Entrez la taille en cm : ")
        while not size.isdigit() or int(size) == 0 or int(size) < 100 or int(size) > 240:
            size = input("Entrez la taille en cm : ")
        weight = input("Entrez le poids en kg : ")
        while not weight.isdigit() or int(weight) < 20 or int(weight) > 200 :
            weight = input("Entrez le poids : ")
        sex = input("Entrez le sexe : ")
        while sex.lower() not in ('f', 'm'):
            sex = input("Entrez le sexe : ")
        imc = calcIMC(size, weight)
        categoryId, categoryName = categorize(imc)
        patients.update({name : [categoryId, categoryName]})
        return True
    else:
        return False



def calcIMC(size, weight) :
    s = int(size)/100
    imc = float(weight)/s**2
    return imc


def categorize(imc) :
    if imc > 40 :
        return "1", "Obésité morbide"
    elif imc > 35 :
        return "2", "Obésité sévère"
    elif imc > 30 :
        return "3", "Obésité modérée"
    elif imc > 25 :
        return "4", "Surpoids"
    elif imc > 18.5 :
        return "5", "Corpulence normale"
    elif imc > 16.5 :
        return "6", "Maigreur"
    else :
        return "7", "Famine"


def showByCat():
    global patients
    patients = sorted(patients.items(), key=lambda t: t[1][0])
    print(patients)
    cat = False
    for patient in patients:
        if patient[1][1] != cat:
            cat = patient[1][1]
            print(cat)
        print("\t"+patient[0])

name = "nan"
patients = {}
while len(name) > 0:
    askInfo()
showByCat()
