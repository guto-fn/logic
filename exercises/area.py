import math

"""
Calculo de área
"""

while True:

    try:

        print("""

            1 - Calcular área em centímetros quadrados de um triângulo
            2 - Calcular área em centímetros quadrados de um quadrado
            3 - Calcular área em centímetros quadrados de um retãngulo
            4 - Calcular área em centímetros quadrados de um losangulo/paralelogramo
            5 - Calcular área em centímetros quadrados de um trapézio
            6 - Calular área em centímetros quadrados de um polígono
            7 - Calular área em centímetros quadrado de um círculo
              
        """)


        i = input("Escolha sua opção de calculo de área: ")

        if not i.strip():

            print("Você não digitou nada, tente novamente!")

            continue

        choice = int(i)

        if choice == 1:

            B = input("Digite a medida em centímetros da base: ")

            A = input("Digite a medida em centímetros da altura: ")

            if not B.strip() and not A.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            base = float(B)

            height = float(A)

            Area = (base * height) / 2

            print(f"A área em centímetros quadrados do triângulo é de: {Area:.2f}cm")

            break

        if choice == 2:

            L = input("Digite a medida em centímetros do lado do quadrado: ")

            if not L.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            side = float(L)

            Area = side ** 2

            print(f"A área em centímetros quadrados do quadrado é de {Area:.2f}cm")

            break

        if choice == 3:

            m = input("Digite a medida em centímetros do lado menor: ")

            M = input("Digite a medida em centímetros do lado maior: ")

            if not m.strip() and not M.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            smaller = float(m)
            bigger = float(M)

            Area = smaller * bigger

            print(f"A área em centímetros quadrados do retângulo é de {Area:.2f}cm")

            break

        if choice == 4:

            d = input("Digite a medida em centímetros da diagonal menor: ")

            D = input("Digite a medida em centímetros da diagonal maior: ")

            if not d.strip() and not D.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            smaller = float(d)

            bigger = float(D)

            Area = (smaller * bigger) / 2

            print(f"A área em centímetros quadrados do losangulo/paralelogramo é de {Area:.2f}cm")

            break

        if choice == 5:

            b = input("Digite a medida em centímetros da base menor: ")

            B = input("Digite a medida em centímetros da base maior: ")

            A = input("Digite a medida em centímetros da altura: ")

            if not b.strip() and not B.strip() and not A.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            smaller = float(b)

            bigger = float(B)

            height = float(A)

            Area = ((smaller * bigger) * height) / 2

            print(f"A área em centímetros quadrados de um trapézio é de {Area:.2f}cm")

            break

        if choice == 6:

            Q = input("Digite a quantidade de lados: ")

            B = input("Digite a medida em centímetros da base: ")

            A = input("Digite a medida em centímetros da apótema: ")

            if not Q.strip() and not B.strip() and not A.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            amount = float(Q)

            base = float(B)

            apothem = float(A)

            Area = (amount * base * apothem) / 2

            print(f"A área em centímetros quadrados de um polígono é de: {Area:.2f}cm")

            break

        if choice == 7:

            R = input("Digite a medida em centímetros do raio: ")

            if not R.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            radius = float(R)

            Area = math.pi * radius ** 2

            print(f"A medida em centímetros quadrados de um círculo é de {Area:.2f}cm")

            break

    except ValueError:
        print()