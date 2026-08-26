
'''
comando = "EQUIPAR Arco"

partes = comando.split()

acao = partes[0]
item = partes[1]

print("Ação:", acao)
print("Item:", item)
'''

#desafio 2

#solicitando o comando de RPG para o usuario
comando_total = input("Digite um comando de RPG (ex: EQUIPAR Arco): ")

#1. separando a ação e o Nome do Item usando o .split()
#0 split() divide o texto por padrão em cada esoaço encontrado
partes = comando_total.split(maxsplit=1)

  #verificando se o comando possui pelo menos duas partes (Ação e Item)
if len(partes) < 2:
    ação = partes[0]
    item = partes[0]
 #exibindo os dados tratados de forma organizada
    print(f"\n--- Comando Analisado ---")
    print(f"Ação detectada: {ação}")
    print(f"Item alvo: {item}")
else:
    print("\nErro: O comando deve conter uma Ação e o Nome do Item separados por espaço.")
g