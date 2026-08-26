texto = "A viagem foi massa"


texto_alterado = texto.replace("massa", "incrível")


print(texto_alterado)


#atividade 1


texto_original = "eu Acho PYTHON muito legal"
texto_limpo = " ".join(texto_original.split())
texto_padronizado = texto_limpo.lower()


print("texto padronizado: '{texto_padronizado}'")


#Desafio
texto_original = " Eu acho PYTHON muito legal "
texto_tratado = texto_original.strip()
texto_tratado = texto_tratado.lower()
texto_tratado = texto_tratado.replace("python", "Python")

