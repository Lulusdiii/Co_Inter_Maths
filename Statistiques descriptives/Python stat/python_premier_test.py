#La Variable est écrite sans espace sans accent en camelCase
# Elle commence par une lettre minuscule et chaque mot suivant commence par une majuscule 

 

jeSuisUneVariable1  = input("Veuillez saisir votre nom : "    )

 

# une variable peut contenir un nombre 

 

#afficher une variable
print("La valeur est : " + str(jeSuisUneVariable1))
jeSuisUneVariable1 = 11
print("La valeur est : " + str(jeSuisUneVariable1))
# Une variable peut contenir une chaîne de caractères
jeSuisUneVariable2 = "Coucou"
# Une variable peut contenir un booléen
jeSuisUneVariable3 = True
# Une variable peut contenir un flottant
jeSuisUneVariableFlotante1 = 3.14   
# une variable peut contenir un tableau , une liste 
jeSuisUneVariableTableau1 = ["Eleve1", 12, 1.2, True, "Eleve5",["Eleve6", 12, 1.2, True, "Eleve10"]]
# une variable peut contenir un objet 
jeSuisUneVariableObjet1 = {"Nom":"Dupont", "Prenom":"Jean", "Age":33, "Adresse":{"Rue":"1 rue de la Paix", "Ville":"Paris", "CodePostal":75000}}
age = 33 
#Constante est écrite en majuscule
PI = 3.14

 

#les op&érateurs arithmétiques sont : +, -, *, /, %, **, //
uneVariable1 = 10
uneVariable2 = 3
total = uneVariable1 + uneVariable2
print("Le total est : " + str(total))

 

#résultat de 13//2
print("Le résultat de 13//2 est : " + str(13//2))

 

print("Le résultat de 13/2 est : " + str(13/2))

 

#comparer 2 variables
#les test sont : ==, !=, <, >, <=, >=
# /!\ on met == pour tester une égalité 
# if (Condition):
if uneVariable1 == uneVariable2:
    #si vrai
    print("Les deux variables sont égales")
else:
    #si faux
    print("Les deux variables sont différentes")   