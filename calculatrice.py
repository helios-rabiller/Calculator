import json
import os

# Chemin pour le fichier JSON de l'historique
FICHIER_HISTORIQUE = "historique.json"

# Exception personnalisée
class CalculatriceErreur(Exception):
    pass

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\nCalculatrice Python")
    print("1. Effectuer une opération")
    print("2. Afficher l'historique")
    print("3. Effacer l'historique")
    print("4. Quitter")

# Fonction pour effectuer une opération mathématique en fonction de l'opérateur donné
def effectuer_operation(a, b, operateur):
    if operateur == "+":
        return a + b
    elif operateur == "-":
        return a - b
    elif operateur == "*":
        return a * b
    elif operateur == "/":
        if b == 0:
            raise CalculatriceErreur("Division par zéro impossible.")
        return a / b
    elif operateur == "**":
        return a ** b
    elif operateur == "%":
        if b == 0:
            raise CalculatriceErreur("Modulo par zéro impossible.")
        return a % b
    else:
        raise CalculatriceErreur("Opérateur non valide.")

# Fonction pour demander un nombre à l'utilisateur avec validation des entrées
def demander_nombre(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Fonction pour demander un opérateur mathématique valide à l'utilisateur
def demander_operateur():
    while True:
        operateur = input("Entrez un opérateur (+, -, *, /, **, %): ")
        if operateur in ["+", "-", "*", "/", "**", "%"]:
            return operateur
        else:
            print("Opérateur invalide, veuillez réessayer.")

# Fonction pour charger l'historique depuis un fichier JSON
def charger_historique():
    if os.path.exists(FICHIER_HISTORIQUE):
        with open(FICHIER_HISTORIQUE, "r") as fichier:
            try:
                return json.load(fichier)
            except json.JSONDecodeError:
                print("Erreur: le fichier historique est corrompu. L'historique sera réinitialisé.")
                return []
    return []

# Fonction pour sauvegarder l'historique dans un fichier JSON
def sauvegarder_historique(historique):
    with open(FICHIER_HISTORIQUE, "w") as fichier:
        json.dump(historique, fichier, indent=4)

# Fonction principale qui gère le programme
def main():
    # Charger l'historique depuis le fichier JSON
    historique = charger_historique()
    
    while True:
        afficher_menu()  # Afficher le menu principal
        choix = input("\nVotre choix: ")
        
        if choix == "1":
            # Saisie des données
            a = demander_nombre("Entrez le premier nombre: ")
            operateur = demander_operateur()
            b = demander_nombre("Entrez le deuxième nombre: ")

            
            try:
                # Calcul et affichage du résultat
                resultat = effectuer_operation(a, b, operateur)
                print(f"Résultat: {a} {operateur} {b} = {resultat}")
                historique.append(f"{a} {operateur} {b} = {resultat}")
                sauvegarder_historique(historique)  # Sauvegarder l'historique
            except CalculatriceErreur as e:
                print(f"Erreur: {e}")
        
        elif choix == "2":
            # Afficher l'historique
            if historique:
                print("\nHistorique des opérations:")
                for ligne in historique:
                    print(ligne)
            else:
                print("\nAucun historique disponible.")
        
        elif choix == "3":
            # Effacer l'historique
            historique.clear()
            sauvegarder_historique(historique)  # Mettre à jour le fichier
            print("Historique effacé.")
        
        elif choix == "4":
            # Quitter le programme
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme principal
if __name__ == "__main__":
    main()

#version final4