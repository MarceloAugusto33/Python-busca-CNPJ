Opção 1: Script Python Busca CNPJ
Objetivo: Codifique um script python que realize a consulta do CNPJ de uma empresa na API do receitaws. O script deve receber como entrada um cnpj e exibir na tela os dados no formtado do JSON abaixo:

Requisitos
- O Script deve receber uma string via input [ x ]
```python
    cnpj = str(input("Digite o CNPJ: "))
```

- O Script deve tratar o input antes de fazer a requisição [ x ]
```python
    def filtrar_numeros(cnpj):
        numeros = re.sub(r'\D', '', cnpj)
        return str(numeros)
```

- O Script deve validar o input e somente realzar a requisição se o input estiver no formtado de CNPJ válido [ x ]

```python
    def validaCNPJ(cnpj):
        padrao_cnpj_regex = r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'

        if re.match(padrao_cnpj_regex, cnpj):
            return True
        else:
            return False
```



- O Script deve utilizar a biblioteca Python requests para realizar a requisição [ x ]
```python
    import requests
```

- O Script deve validar o status code da requisição [ x ]
```python
        if request.status_code == 200:
            ...Codigos
        else:
            print("Failed request")
```

- O Script deve validar a resposta da requisição e indicar se o CNPJ foi localizado na API ou não. [ x ]
```python
        if(requestJSON['status'] == 'ERROR'): 
            return "Esse CNPJ não existe na api"
        else:
            print("Dados Encontrados na API")
```

- O Script deve exibir os dados no formato JSON acima [ x ]
```python
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

```

        

## EXECUTE NO CMD CASO NÃO TENHA A BIBLIOTECA REQUESTS
    pip install requests





