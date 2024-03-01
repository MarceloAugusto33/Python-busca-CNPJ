import requests
import re

def display():
    print(" ")
    print("|                        |")
    print("|  BUSCA DADOS POR CNPJ  |")
    print("|                        |")
    print("|  OPÇÕES                |")
    print("|  |0| SAIR              |")
    print("|  |1| BUSCAR POR CNPJ   |")
    print("|                        |")
    print(" ")

def getDataApi(cnpj):

    request = requests.get('https://receitaws.com.br/v1/cnpj/'+cnpj)

    if request.status_code == 200:

        requestJSON = request.json()

        if(requestJSON['status'] == 'ERROR'): 
            print(" ")
            return "Esse CNPJ não existe na api"
        
        print("Dados Encontrados na API")

        result = {
            "razao_social": requestJSON['nome'],
            "codigo_atividade_principal": requestJSON['atividade_principal'][0]['code'],
            "endereco": {
                "numero": requestJSON['numero'],
                "cep": requestJSON['cep'],
                "municipio": requestJSON['municipio'],
                "estado": requestJSON['uf'],
            }

        }

        return result
    else:
        print("Failed request")

def validaCNPJ(cnpj):
    padrao_cnpj_regex = r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'

    if re.match(padrao_cnpj_regex, cnpj):
        return True
    else:
        return False

def filtrar_numeros(cnpj):
    numeros = re.sub(r'\D', '', cnpj)
    return str(numeros)


while True:
    display()
    try:
        option = int(input("Digite uma opção: "))

        while option != 0 and option != 1:
            print(" ")
            option = int(input("Digite uma opção valida!: "))

        if option == 0:
            break
        elif option == 1:
            print("Digite o CNPJ NO SEGUINTE MODELO: 12.123.123/1234-12")
            cnpj = str(input("Digite o CNPJ: "))

            if(validaCNPJ(cnpj)):
                print(getDataApi(filtrar_numeros(cnpj)))
            else: 
                print("CNPJ INVALIDO!")
                print("")
    except ValueError:
        print(" ")
        print("DIGITE SOMENTE NUMEROS")
        print(" ")


print("Programa finalizado!")