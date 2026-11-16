total = 0

tableau = [22, 22.6, 21.1, 21.9, 18.3, 18.7, 21.7, 21.1, 23.6, 27.4,
          25.1, 24.9, 23.7, 28.9, 23.2, 26.1, 26.1, 29.8, 28.2, 28.7,
          25.9, 26.7, 30.3, 25.2, 21.8, 22, 20.9, 20.7, 20.6, 19.5, 18.8]

for i in range(31):    
    total = total + tableau [i]
Moyenne = total / 31

min_temp = tableau[0]
max_temp = tableau[0]

for i in range(1, len(tableau)):
    if tableau[i] < min_temp:
        min_temp = tableau[i]
    if tableau[i] > max_temp:
        max_temp = tableau[i]

etendue = max_temp - min_temp

print("La moyenne est de " + str(Moyenne))
print("La température minimale est " + str(min_temp))
print("La température maximale est " + str(max_temp))
print("L'étendue est " + str(etendue))