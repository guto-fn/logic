"""

Conversão de temperatura

"""

while True:

    try:

        print("""

            1 - Celsius para Fahrenheit
            2 - Fahrenehit para Celsius
            3 - Celsius para Kelvin
            4 - Kelvin para Celsius
            5 - Celsius para Rankine
            6 - Rankine para Celsius
            7 - Fahrenheit para Kelvin
            8 - Kelvin para Fahrenheit
            9 - Fahrenheit para Rankine
            10 - Rankine para Fahrenheit
            11 - Kelvin para Rankine
            12 - Rankine para Kelvin

        """)
    
        i = input("Digite sua opção de conversão: ")

        if not i.strip(): # função strip, verifica sem na var i tem (tabs, espaços em branco e enter direto, sem nenhum valor)

            print("Você não digitou nada, tente novamente!")

            break

        choice = int(i) # definindo como inteiro

        if choice < 1 or choice > 12:

            print("As opções são de 1 a 12 apenas. Tente novamente!")

            break

        # Celsius para Fahrenheit
        if choice == 1:

            temp = input("Digite a temperatura em Celsius a ser convertida para Fahrenheit: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue # continua o ciclo

            C = float(temp)

            F = (C * 9 / 5) + 32

            print(f"A temperatura em Fahrenheit é de: {F:.2f}")

        # Fahrenheit para Celsius
        if choice == 2:

            temp = input("Digite a temperatura em Fahrenheit a ser convertida para Celsius: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            F = float(temp)

            C = (F - 32) * 5 / 9

            print(f"A temperatura em Celsius é de: {C:.2f}")

        # Celsius para Kelvin
        if choice == 3:

            temp = input("Digite a temperatura em Celsius a ser convertida para Kelvin: ")

            if not temp.strip():
                
                print("Você não digitou nada, tente novamente!")

                continue

            C = float(temp)

            K = C + 273.15

            print(f"A temperatura em Kelvin é de: {K:.2f}")

        # Kelvin para Celsius
        if choice == 4:

            temp = input("Digite a temperatura em Kelvin a ser convertida para Celsius: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            K = float(temp)

            C = K - 273.15

            print(f"A temperatura em Celsius é de: {C:.2f}")

        # Celsius para Rankine
        if choice == 5:

            temp = input("Digite a temperatura em Celsius a ser convertida para Rankine: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            C = float(temp)

            R = C * 9 / 5 + 491.67

            print(f"A temperatura em Rankine é de: {R:.2f}")

        # Rankine para Celsius
        if choice == 6:

            temp = input("Digite a temperatura em Rankine a ser convertida para Celsius: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            R = float(temp)

            C = (R - 491.67) * 5 / 9

            print(f"A temperatura em Celsius é de {C:.2f}")

        # Fahrenheit para Kelvin
        if choice == 7:

            temp = input("Digite a temperatura em Fahrenheit a ser convertida para Kelvin: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            F = float(temp)

            K = (F - 32) * 5 / 9 + 273.15

            print(f"A temperatura em Kelvin é de: {K:.2f}")

        # Kelvin para Fahrenheit
        if choice == 8:

            temp = input("Digite a temperatura em Kelvin a ser convertida para Fahrenheit: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            K = float(temp)

            F = (K - 273.15) * 9 / 5 + 32

            print(f"A temperatura em Fahrenheit é de: {F:.2f}")

        # Fahrenheit para Rankine
        if choice == 9:

            temp = input("Digite a temperatura em Fahrenheit a ser convertida para Rankine: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            F = float(temp)

            R = F + 459.67

            print(f"A temperatura em Rankine é de: {R:.2f}")

        # Rankine para Fahrenheit
        if choice == 10:

            temp = input("Digite a temperatura em Rankine a ser convertida para Fahrenheit: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            R = float(temp)

            F = R - 459.67

            print(f"A temperatura em Fahrenheit é de: {F:.2f}")

        # Kelvin para Rankine
        if choice == 11:

            temp = input("Digite a temperatura em Kelvin a ser convertida para Rankine: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            K = float(temp)

            R = K * 1.8

            print(f"A temperatura em Rankine é de: {R:.2f}")

        # Rankine para Kelvin
        if choice == 12:

            temp = input("Digite a temperatura em Rankine a ser convertida para Celsius: ")

            if not temp.strip():

                print("Você não digitou nada, tente novamente!")

                continue

            R = float(temp)

            K = R * 5 / 9

            print(f"A temperatura em Kelvin é de: {K:.2f}")

        break
    
    except ValueError:

        print("Erro!, digite um valor inteiro válido")