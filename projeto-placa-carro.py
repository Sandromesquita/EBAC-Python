from datetime import datetime

mes_atual = datetime.now().month
#mes_atual = 4
contador = 0
#licenciamento=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#licenciamento = ["Dezembro", "Abril", "Maio", "Junho", "Julho",
#                 "Agosto", "Agosto", "Setembro", "Outubro", "Novembro"]

licenciamento = {
                "1": "Abril",
                "2": "Maio",
                "3": "Junho",
                "4": "Julho",
                "5": "Agosto",
                "6": "Agosto",
                "7": "Setembro",
                "8": "Outubro",
                "9": "Novembro",
                "0": "Dezembro"
}

"""
imposto = {
        2022 : 3000
        2021 : 2500
        2020 : 2000
}
"""
#valor_carro = 60.000
"""
imposto = {
        2022 : 0.10
        2021 : 0.09
        2020 : 0.08
}
"""

while input("Deseja consultar outra placa? (s/n)").upper() == "S":
    contador+=1
    placa = input("Digite sua placa: ")
    ultimo_numero = int(placa[len(placa)-1])

    #print("A placa tem ", len(placa), "caracteres")
    #print("O ultimo caracter e:", placa[len(placa)-1])
    #print(type(ultimo_numero))

    print("Placa", placa, "com final", ultimo_numero)
    #print("Seu licenciamento vence em ", licenciamento[ultimo_numero])

    if  ultimo_numero == 0:
        mes = 12
    elif ultimo_numero >= 6:
        mes = ultimo_numero + 2
    else:
        mes = ultimo_numero + 3

    tempo_vencer = mes - mes_atual

    print("Faltam", tempo_vencer, "meses para vencer")

    if tempo_vencer == 0:
        print("Seu vencimento e neste mes")
        #perguntar o ano do carro
        #ano = 2022
        #valor=imposto[ano]
        #O seu boleto e de: valor .
        #nivel 2 valor_carro*valor
        #nivel 3 surpreenda-me


    #metodo 1
    """
    cont = input("Deseja consultar outra placa? (s/n)").upper()
    if cont == "N":
        break
    """

    # metodo 2
    """
    if input("Deseja consultar outra placa? (s/n)").upper() == "N":
        break
    """
print("Obrigado pro usar nosso sistema")
print("Voce ralizou", contador, "consultas")