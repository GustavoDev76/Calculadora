print("---CALCULADORA---")

valor1 = float(input("Digite o Primeiro Valor: "))
valor2 = float(input("digite o segundo valor: "))

print("1 - Soma (+)")
print("2 - Subtracao (-)")
print("3 - Multiplicacao (*)")
print("4 - Divisao (/)")

operador = str(input("Escolha um Operador: "))

if operador == "1":
    print(f"RESULTADO: {valor1 + valor2}")
elif operador == "2":
    print(f"RESULTADO: {valor1 - valor2}")
elif operador == "3":
    print(f"RESULTADO: {valor1 * valor2}")
elif operador == "4":
    if valor2 != 0:
        print(f"RESULTADO: {valor1 / valor2}")
    else:
        print("Divisao dividido por Zero!")