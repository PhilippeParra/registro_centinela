
n = int(input("Digite el numero a evaluar: "))

par = 0
impar = 0
if n != 0:
    while n != 0:
        r = n % 2

        if r == 0:
            par = par + 1
        else:
            impar = impar + 1

        n = int(input("Digite el numero a evaluar: "))

print("Numeros impares:" , impar)
print("Numeros pares:" , par)