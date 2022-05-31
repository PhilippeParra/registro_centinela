print("-*****************************************-")
cod = int(input("Digite el codigo del estudiante: "))
print("-------------------------------------")
nombre = input("Digite el nombre del estudiante: ")
print("-------------------------------------")

if cod != 0:
   nota1 = float(input("Digite la nota #1: "))
   print("-------------------------------------")
   nota2 = float(input("Digite la nota #2: "))
   print("-------------------------------------")
   nota3 = float(input("Digite la nota #3: "))
   print("-*****************************************-")
else: 
    print("Fin de los datos de entrada.")

reprobados = 0

while cod != 0:
    notafin = (nota1 + nota2 + nota3) / 3
    print("Codigo del estudiante:" , cod , "\nNota del estudiante:" , notafin)

    if notafin < 3.0:
        reprobados = reprobados + 1
        
    print("-*****************************************-")
    cod = int(input("Digite el codigo del estudiante: "))
    print("-------------------------------------")
    nombre = input("Digite el nombre del estudiante: ")
    print("-------------------------------------")

    if cod != 0:
        nota1 = float(input("Digite la nota #1: "))
        print("-------------------------------------")
        nota2 = float(input("Digite la nota #2: "))
        print("-------------------------------------")
        nota3 = float(input("Digite la nota #3: "))
        print("-*****************************************-")
    else: 
        print("Fin de los datos de entrada.")

if reprobados >= 1:
    print("El numero de estudiantes que perdieron la materia fue: " , reprobados)
else:
    print("Ningun estudiante perdio la materia.")