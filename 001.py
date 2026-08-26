comando_usuario = "AjUdA"
comando_tratado = comando_usuario.lower()

print(comando_tratado) #ajuda

comando_usuario = "IsAdOrA"
comando_tratado = comando_usuario.lower()
print(comando_tratado)#ISADORA

# 1 . Recebe a entrada do jogador
comando_usuario =  input("Digite um comando:")

# 2 . Converte para maiúsculo para ignoral varioções de letras
comando_tratado = comando_usuario.upper()

# 3 . Verifica se o comando é válido
if comando_tratado == "AJUDA":
    print("comando não reconhecido. ")
    