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
            print("Utiliser les symboles +,/,* ou - pour réaliser un calcul")
            return None
    while True:
        try:
            a = float(input("valeur a = "))
            c = input("nature de l'opération = ")
            b = float(input("Valeur b = "))
            result = calcul(a,b,c)
            if result is not None:
                print(f"Résultat : {result}")
                break
        except ValueError:
            print("Veuillez rentrer des nombres entier ou décimaux !")
verif_calcul()