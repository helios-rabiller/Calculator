history = []  # List created to store history of operation
def verif_calcul():
    
    def calcul(a, b, c):
        if c == "+":
            return a + b
        elif c == "-":
            return a - b
        elif c == "*":
            return a * b
        elif c == "/":
            if b != 0:
                return a / b
            else:
                print("Erreur : Division par zéro!")
                return None
        else:
            print("Erreur : Opération non reconnue!")
            print("Utiliser les symboles +, /, * ou - pour réaliser un calcul")
            return None

    while True:
        try:
            a = float(input("valeur a = "))
            c = input("nature de l'opération = ")
            b = float(input("Valeur b = "))
            result = calcul(a, b, c)


            if result is not None:
                print(f"Résultat : {result}")
                # Add to history
                history.append((a, c, b, result))
                print("Historique des calculs :")

                for calc in history:
                    print(f"{calc[0]} {calc[1]} {calc[2]} = {calc[3]}")  # Display history

                while True:
                    replay = input("voulez-vous faire un autre calcul ? (oui/non) = ")
                    replay = replay.lower()
                    if replay == "oui":
                        break
                    elif replay == "non":
                        print("À bientôt !")
                        return  # Quit Main function
                    else:
                        print("Veuillez rentrer uniquement (oui) ou (non)")

        except ValueError:
            print("Veuillez rentrer des nombres entiers ou décimaux !")

verif_calcul()