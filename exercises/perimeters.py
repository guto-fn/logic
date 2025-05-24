import math

"""
Calculo de perimetros
"""


while True:

    try:

        print("""

            1 - Calcular o perimetro em centímetros de um triângulo
            2 - Calcular o perimetro em centímetros de um quadrado/losangulo
            3 - Calcular o perimetro em centímetros de um retangulo
            4 - Calcular o perimetro em centímetros de um trapézio
            5 - Calcular o perimetro em centímetros de um circulo


        """)


        i = input("Digite sua opção de perimetro: ")

        if not i.strip():

            print("Você não digitou nada, tente novamente!")

        
        choice = int(i)

        if choice == 1:

            A = input("Digite a medida em centímetros do lado A: ")

            B = input("Digite a medida em centímetros do lado B: ")

            C = input("Digite a medida em centímetros do lado C: ")


            if not A.strip() and not B.strip() and not C.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            measure = float(A + B + C)

            P = measure

            print(f"A medida em centímetros do triângulo é de: {P:.2f}cm")

            break

        if choice == 2:

            L = input("Digite a medida em centíemtros dos lados do quadrado: ")

            if not L.strip():

                print("Você não digitou nada, tente novamente!")

                continue


            measure = float(L)

            P = 4 * measure

            print(f"A medida em centíemtros do quadrado é de {P:.2f}cm")

            break

        if choice == 3:

            m = input("Digite a medida em centímetros do lado menor: ")

            M = input("Digite a medida em centímetros do lado maior: ")

            if not m.strip() and not M.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            m = float(m)

            M = float(M)

            measure = m + M

            P = measure * 2

            print(f"A medida em centímetros do retangulo é de {P:.2f}cm")

            break

        if choice == 4:

            m = input("Digite a medida em centímetros do lado menor: ")

            M = input("Digite a medida em centímetros do lado maior: ")

            O = input("Digite a medida em centímetros do outro lado: ")

            if not m.strip() and not M.strip() and not O.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            m = float(m)

            M = float(M)

            O = float(O)

            P = m + M + 2 * O

            print(f"A medida em centímetros do trapézio é de: {P:.2f}cm")

            break

        if choice == 5:

            R = input("Digite a medida em centímetros do raio: ")

            if not R.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            measure = float(R)

            P = 2 * math.pi * measure

            print(f"A medida em centímetros do circulo é de {P:.2f}cm")

    except ValueError:
        print("Erro!, digite um valor válido")