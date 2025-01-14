# #launching calculator 

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")

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

op=input("enter an operator: ")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if op=='+':
    r=n1+n2
    print(r)
elif op == '-':
    r=n1-n2
    print(r)
elif op == '*':
    r=n1*n2
    print(r)
else :
    r=n1/n2
    print(r)