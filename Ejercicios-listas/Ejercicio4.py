def solution(a):
    equipo_1 = 0
    equipo_2 = 0
    for i in range(len(a)):
        if i % 2 == 0:
            equipo_1 += a[i]
        else:
            equipo_2 += a[i]
    return [equipo_1, equipo_2]

entrada = input("Ingrese los números separados por espacios (ej: 50 60 60 45 70): ")
a = [int(x) for x in entrada.split()]
print(solution(a))