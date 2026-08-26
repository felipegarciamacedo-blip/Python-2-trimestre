palavra = input("Digite uma palavra:")
palavra_normal = palavra.strip().lower()

if palavra_normal == "python":
    print("Palavra está certa!")
else:
    print("Palavra está errada!")

entrada = "   "
entrada_limpa = entrada.strip()


if entrada_limpa == "":
    print("Erro: entrada inválida")


texto = input(" Digite um texto ")
texto = texto.strip().lower()


if texto == "python":
    print(" Texto correto! ")
else:
    print("Texto diferente.")




mensagem = "URGENTE: precisamos do relatório o mais rápido possível!"


# Usando comparação exata ((if)sem usar ==) # False
if mensagem == ["URGENTE"]:   #não usar operador matemático
    print("Comando reconhecido com if")
else:
    print("Comando NÃO reconhecido")


# Usando o operador de associação in na string # True
if "URGENTE" in mensagem:
    print("Palavra encontrada com in")
else:
    print("Palavra NÃO encontrada com in")




# 1. Definindo o texto digitado pelo usuário
mensagem = " Gostaria de  saber mais sobre Python e programação"
" 2. Verificamos se a palavra 'python' está presente no texto"
# Dica: Convertemos o texto para minúsculas (.lower()) para evitar prblemas
# de diferença entre maiísculas e minúsculas ("Python" vs "python").
if "python" in mensagem.lower():
    print("O texto contém a palavra 'python'!")
else:
    print("A palavra 'python' não foi encontrada no texto.")


# 1. Entrada de texto do usuário
mensagem = input("Digite a sua mensagem:")


# 2. Trata o texto pra minúculas e verifica se a palavra 'python' está presente
if "python" in mensagem.lower():
    print("tema identificado")
else:
    print("tema não identificado")
