#-----------début version basique------------------

#launching calculator 

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
history = []

while True:
    if operator == "+":
        result = float(num1 + num2)
        num1_str= str(num1)
        num2_str= str(num2)
        result_str= str(result)
        history.append(f'{num1_str} + {num2_str} = {result}')
        print(round(result, 3))
        print(history)
    elif operator == "-":
        result = float(num1 - num2)
        num1_str= str(num1)
        num2_str= str(num2)
        result_str= str(result)
        history.append(f'{num1_str} - {num2_str} = {result}')
        print(round(result, 3))
        print(history)
    elif operator == "*":
        result = float(num1 * num2)
        num1_str= str(num1)
        num2_str= str(num2)
        result_str= str(result)
        history.append(f'{num1_str} * {num2_str} = {result}')
        print(round(result, 3))
        print(history)
    elif operator == "/":
        result = float(num1 / num2)
        num1_str= str(num1)
        num2_str= str(num2)
        result_str= str(result)
        history.append(f'{num1_str} / {num2_str} = {result}')
        print(round(result, 3))
        print(history)
    else:
        print(f"{operator} is not a valid operator")
    break

# -----------------------Fin version basique------------------------

# -------------------------Début Version OP------------------------------
        
# def calculatrice():
#     history = []  # Liste pour stocker l'historique des calculs

#     while True:
#         print("\n--- Calculatrice ---")
#         print("1. Effectuer une opération")
#         print("2. Afficher l'historique")
#         print("3. Réinitialiser l'historique")
#         print("4. Quitter")
        
#         choix = input("Choisissez une option (1-4): ")

#         if choix == "1":  # Effectuer une opération
#             operator = input("Entrez un opérateur (+, -, *, /): ")
#             try:
#                 num1 = float(input("Entrez le 1er nombre: "))
#                 num2 = float(input("Entrez le 2ème nombre: "))
                
#                 if operator == "+":
#                     result = num1 + num2
#                     history.append(f"{num1} + {num2} = {result}")
#                     print(f"Résultat: {result}")
#                 elif operator == "-":
#                     result = num1 - num2
#                     history.append(f"{num1} - {num2} = {result}")
#                     print(f"Résultat: {result}")
#                 elif operator == "*":
#                     result = num1 * num2
#                     history.append(f"{num1} * {num2} = {result}")
#                     print(f"Résultat: {result}")
#                 elif operator == "/":
#                     if num2 != 0:
#                         result = num1 / num2
#                         history.append(f"{num1} / {num2} = {result}")
#                         print(f"Résultat: {result}")
#                     else:
#                         print("Erreur: Division par zéro.")
#                 else:
#                     print("Opérateur invalide.")
#             except ValueError:
#                 print("Erreur: Veuillez entrer des nombres valides.")

#         elif choix == "2":  # Afficher l'historique
#             print("\n--- Historique des opérations ---")
#             if history:
#                 for entry in history:
#                     print(entry)
#             else:
#                 print("L'historique est vide.")

#         elif choix == "3":  # Réinitialiser l'historique
#             history.clear()
#             print("L'historique a été réinitialisé.")

#         elif choix == "4":  # Quitter
#             print("Au revoir!")
#             break

#         else:
#             print("Choix invalide. Veuillez réessayer.")

# # Appel de la fonction principale
# calculatrice()

# ------------Fin Version OP --------------------------------

# --------------Premiers essais-----------------------------

# A = float(input("Veuilez saisir la valeur de A : "))
# op = input("Veuilez saisir l'opérateur : ")
# B = float(input("Veuilez saisir la valeur de B : "))
# if op == "+" :
#     print("A + B = ", A+B )
# elif op == "-" :
#     print("A - B = ", A-B )
# elif op == "/" :
#     if B != 0 :
#         print("A / B = ", A/B )
#     else :
#         print("La division par 0 est impossible")
# elif op == "*" :
#     print(" A * B = ", A*B)

# else:
#     print("L'opérateur est incorrect")

# ------ fin des premiers essais ------------

# ---------------début version 1 ----------

# op=input("enter an operator: ")
# n1=int(input("Enter the first number: "))
# n2=int(input("Enter the second number: "))
# if op=='+':
#     r=n1+n2
#     print(r)
# elif op == '-':
#     r=n1-n2
#     print(r)
# elif op == '*':
#     r=n1*n2
#     print(r)
# else :
#     r=n1/n2
#     print(r)