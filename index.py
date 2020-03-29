import sys
import requests
import hashlib
import random
import json

print("\nRetorno da API:\n{\nnumero_casas: 1\ntoken: b1c78eeadf977279a257799be2ca7842c5360cef \ncifrado: gpdvt po xiz jotufbe pg xibu jo zpvs dpef xjmm nblf zpv b cfuufs efwfmpqfs kpsej cphhjbop \ndecifrado: \nresumo_criptografico: \n}")

print("\nEsse programa codifica e decodifica palavras!")

alfabeto = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

casas = int(
    input("\nQuantas casas você quer alterar conforme a cifra de César?: "))

tipo = int(input(
    "\nQual operação iremos realizar?\n \n1 - Criptografia\n2 - Descriptografia\n\nDigite a operação desejada: "))

if tipo != 1 and tipo != 2:
    print("Insira uma opção válida!")
else:
    message = str(input("\nInsira o texto: "))

message = message.lower()

if tipo == 1:
    m = ''
    # Chamo de c o caracter, ou seja cada letra da frase
    for c in message:
        if c in alfabeto:
            c_index = alfabeto.index(c)
            # utilizando MOD para fechar o círculo, assim de z retorna pra a!
            m += alfabeto[(c_index + casas) % len(alfabeto)]
        else:
            m += c
        cifrado = m
    print("\nA mensagem cifrada é: {}".format(cifrado))
    resumo_criptografico = hashlib.sha1(cifrado.encode('utf-8')).hexdigest()
    print("\nO resumo criptografico é: {}\n".format(resumo_criptografico))

if tipo == 2:
    m = ''
    for c in message:
        if c in alfabeto:
            c_index = alfabeto.index(c)
            m += alfabeto[(c_index - casas) % len(alfabeto)]
        else:
            m += c
        decifrado = m
    print("A mensagem decifrada é: {}\n".format(decifrado))
    resumo_criptografico = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()
    print("\nO resumo criptografico é: {}\n".format(resumo_criptografico))

    # decifrado: focus on why instead of what in your code will make you a better developer jordi boggiano
    # resumo_criptografico: da39a3ee5e6b4b0d3255bfef95601890afd80709

resumo = str(input("Valide o resumo criptografico, insira a palavra para validação:"))
resumo=hashlib.sha1(resumo.encode('utf-8')).hexdigest()
print("")
print(resumo)
