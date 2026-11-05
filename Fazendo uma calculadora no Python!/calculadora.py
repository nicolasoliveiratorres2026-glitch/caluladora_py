import cmath
print("Sejam bem-vindos(a) à calculadora no Python!")
print("Operações: \n1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Potenciação \n6. Fatorial \n7. Radiciação \n8. Logaritmo")
opr = input("Selecione o número da operação que você deseja: ")
if opr == "1":
    print("Operação: Adição")
    while True:
        try:
            n1_mais = float(input("Digite o primeiro número da adição: "))
            print(f"Primeiro número: {n1_mais}")
            n2_mais = float(input("Digite o segundo número da adição: "))
            print(f"Segundo número: {n2_mais}")
            break
        except ValueError:
            print("Digite apenas números!")
            n1_mais = float(input("Digite novamente o primeiro número da adição: "))
            print(f"Primeiro número: {n1_mais}")
            n2_mais = float(input("Digite novamente o segundo número da adição: "))
            print(f"Segundo número: {n2_mais}")
            break
    r_mais = n1_mais + n2_mais
    print(f"{n1_mais} + {n2_mais} = {r_mais}")
    print("Resultado calculado com sucesso!")
elif opr == "2":
    print("Operação: Subtração")
    while True:
        try:
            n1_menos = float(input("Digite o primeiro número da subtração: "))
            print(f"Primeiro número: {n1_menos}")
            n2_menos = float(input("Digite o segundo número da subtração: "))
            print(f"Segundo número: {n2_menos}")
            break
        except ValueError:
            print("Digite apenas números!")
            n1_menos = float(input("Digite novamente o primeiro número da subtração: "))
            print(f"Primeiro número: {n1_menos}")
            n2_menos = float(input("Digite novamente o segundo número da subtração: "))
            print(f"Segundo número: {n2_menos}")
            break
    r_menos = n1_menos - n2_menos
    print(f"{n1_menos} - {n2_menos} = {r_menos}")
    print("Resultado calculado com sucesso!")
elif opr == "3":
    print("Operação: Multiplicação")
    while True:
        try:
            n1_vezes = float(input("Digite o primeiro número da multiplicação: "))
            print(f"Primeiro número: {n1_vezes}")
            n2_vezes = float(input("Digite o segundo número da multiplicação: "))
            print(f"Segundo número: {n2_vezes}")
            break
        except ValueError:
            print("Digite apenas números!")
            n1_vezes = float(input("Digite novamente o primeiro número da multiplicação: "))
            print(f"Primeiro número: {n1_vezes}")
            n2_vezes = float(input("Digite novamente o segundo número da multiplicação: "))
            print(f"Segundo número: {n2_vezes}")
            break
    r_vezes = n1_vezes * n2_vezes
    print(f"{n1_vezes} * {n2_vezes} = {r_vezes}")
    print("Resultado calculado com sucesso!")
elif opr == "4":
    print("Operação: Divisão")
    while True:
        try:
            n1_divisao = float(input("Digite o primeiro número da divisão: "))
            print(f"Primeiro número: {n1_divisao}")
            n2_divisao = float(input("Digite o segundo número da divisão: "))
            print(f"Segundo número: {n2_divisao}")
            break
        except ValueError:
            print("Digite apenas números!")
            n1_divisao = float(input("Digite novamente o primeiro número da divisão: "))
            print(f"Primeiro número: {n1_divisao}")
            n2_divisao = float(input("Digite novamente o segundo número da divisão: "))
            print(f"Segundo número: {n2_divisao}")
            break
    while True:
        try:
            r_divisao = n1_divisao / n2_divisao
            print(f"{n1_divisao} / {n2_divisao} = {r_divisao}")
            print("Resultado calculado com sucesso!")
            break
        except ZeroDivisionError:
            print("Não é possível dividir por 0!")
            n2_divisao = float(input("Digite novamente o segundo número da divisão: "))
            print(f"Segundo número: {n2_divisao}")
            r_divisao = n1_divisao / n2_divisao
            print(f"{n1_divisao} / {n2_divisao} = {r_divisao}")
            print("Resultado calculado com sucesso!")
            break
elif opr == "5":
    print("Operação: Potenciação")
    while True:
        try:
            bs_potencia = float(input("Digite a base da potenciação: "))
            print(f"Base: {bs_potencia}")
            exp = float(input("Digite o expoente da potenciação: "))
            print(f"Expoente: {exp}")
            break
        except ValueError:
            print("Digite apenas números!")
            bs_potencia = float(input("Digite novamente a base da potenciação: "))
            print(f"Base: {bs_potencia}")
            exp = float(input("Digite novamente o expoente da potenciação: "))
            print(f"Expoente: {exp}")
            break
    r_potencia = bs_potencia ** exp
    print(f"{bs_potencia} ^ {exp} = {r_potencia}")
    print("Resultado calculado com sucesso!")
elif opr == "6":
    print("Operação: Fatorial")
    while True:
        try:
            n_fatorial = float(input("Digite o número do fatorial: "))
            print(f"Número do fatorial: {n_fatorial}")
            break
        except ValueError:
            print("Digite apenas números positivos!")
            n_fatorial = float(input("Digite novamente o número do fatorial: "))
            print(f"Número do fatorial: {n_fatorial}")
            break

    r_fatorial = cmath.factorial(n_fatorial)
    print(f"{n_fatorial}! é aproximadamente {r_fatorial}")
    print("Resultado calculado com sucesso!")
elif opr == "7":
    print("Operação: Radiciação")
    while True:
        try:
                indice = float(input("Digite o índice da raíz: "))
                print(f"Índice: {indice}")
                radicando = float(input(f"Digite o radicando da raíz do índice {indice}: "))
                print(f"Radicando: {radicando}")
                break
        except ValueError:
            print("Digite apenas números!")
            indice = float(input("Digite novamente o índice da raíz: "))
            print(f"Índice: {indice}")
            radicando = float(input(f"Digite novamente o radicando da raíz do índice {indice}: "))
            print(f"Radicando: {radicando}")
            break
    while True:
        try:
            r_raiz = cmath.pow(radicando, 1 / indice)
            print(f"A raíz de {radicando} do índice {indice} = {r_raiz}")
            print("Resultado calculado com sucesso!")
            break
        except TypeError:
            print("Digite apenas números inteiros!")
            indice = float(input("Digite novamente o índice da raíz: "))
            print(f"Índice: {indice}")
            radicando = float(input(f"Digite novamente o radicando da raíz do índice {indice}: "))
            print(f"Radicando: {radicando}")
            r_raiz = cmath.pow(radicando, 1 / indice)
            print(f"A raíz de {radicando} do índice {indice} = {r_raiz}")
            print("Resultado calculado com sucesso!")
            break
elif opr == "8":
    print("Operação: Logaritmo")
    while True:
        try:
            base_log = float(input("Digite a base do logaritmo: "))
            print(f"Base: {base_log}")
            n_log = float(input("Digite o número do logaritmo: "))
            print(f"Número do logaritmo: {n_log}")
            break
        except ValueError:
            print("Digite apenas números!")
            base_log = float(input("Digite novamente a base do logaritmo: "))
            print(f"Base: {base_log}")
            n_log = float(input("Digite novamente o número do logaritmo: "))
            print(f"Número do logaritmo: {n_log}")
            break
    if base_log < 0:
        complexo_base_log = base_log + 0j
        r_log = cmath.log(n_log, complexo_base_log)
        print(f"O logaritmo de {n_log} da base {complexo_base_log} = {r_log}")
        print("Resultado calculado com sucesso!")
    elif base_log >= 0:
        r_log = cmath.log(n_log, base_log)
        print(f"O logaritmo de {n_log} da base {base_log} = {r_log}")
        print("Resultado calculado com sucesso!")
else:
    print("Ainda não temos essa operação que você digitou")
    exit()