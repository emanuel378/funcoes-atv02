## Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def verificar_paridade (n):
    
    if n%2==0:
        return "Par"
    else:
        return "iMPAR"
    
numero = int(input("Digite seu numero:"))
verifica =verificar_paridade(numero)
print(verifica)