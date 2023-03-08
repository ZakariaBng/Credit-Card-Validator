# Projet validateur de carte bancaire

card_number = input("Numéro de la carte bancaire : ")

# On supprime les espaces entre les chiffres saisis (si il y en a)
# On transforme la saisie en integer
card_number = card_number.replace(" ", "")
card_number = list(card_number)   
card_number = list(map(int, card_number))  

# On retire le dernier chiffre appelé 'Chiffre de contrôle' et on inverse l'ordre des chiffres restants
control_number = card_number[-1]  
card_number.pop()  
card_number.reverse()  

sum_1 = 0
sum_2 = 0
sum_odd_numbers = 0

for number in range(len(card_number)):  
    # On prend les chiffres d'indice pair et on les double
    if number % 2 == 0: 
        even_number = card_number[number]  
        double = even_number * 2  
        # Si le résultat de la multiplication par 2 est supérieur à 9, on retire 9 et on passe au chiffre suivant        
        if double > 9:                                       
            minus = double - 9
            sum_1 += minus
        # Si le résultat de la multiplication par 2 est inférieur ou égal à 9, on passe au chiffre suivant   
        if double <= 9:
            sum_2 += double
        # On additionne les deux résultats (qui sont eux-mêmes des sommes)
        sum_even_numbers = sum_1 + sum_2
    
    # On prend les chiffres d'indice impair sans les modifier et on les somme entre eux
    elif number % 2 != 0:
        odd_number = card_number[number]
        simple = odd_number * 1
        sum_odd_numbers += simple       

# On additionne les deux montants obtenus 
total = sum_even_numbers + sum_odd_numbers

# On réintègre le dernier chiffre (Numéro de contrôle) qui a été supprimé à la ligne 13
total_w_ctrl_nbr = total + control_number
print(total_w_ctrl_nbr)

# Si la somme est un multiple de 10, alors la carte est valide
if total_w_ctrl_nbr % 10 == 0:
    print("Carte valide")
# Si non, la carte est invalide
elif total_w_ctrl_nbr % 10 != 0:
    print("Carte non valide")