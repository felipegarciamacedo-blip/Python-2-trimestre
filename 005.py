nome_usuario = input("Digite seu nome de usuário: ")
email = "Ana@Email.com"

#Remove espaços em branco nas pontas e padroniza o e-mail em letras minúsculas
nome_tratado = nome_usuario.strip()
email_tratado = email.lower()

#Verifica se o nome original tinha espaços extras nas ponta
if nome_tratado != nome_usuario:
    print("nome contem espaços extras ")
    #Verifica se o email original tinha letras maiúsculas 
elif email != email_tratado:
    print("email contem letras maiúsculas ")
else:
    print("Dados invalidos")


gmail = "Usuario@gamil.com"
gmail_tratado = gmail.lower()

if "@" in email_tratado:
    print("Gmail válido")
else:
    print("Gmail invalido")


senha = "12345"
tamanha = len(senha)

if tamanha < 8:
    print("Senha muito curta")
else:
    print("senha invalida")


#recebe o texto digitado pelo usuário
post = input("Digite o seu post: ")

#Verifica se o tamanho do post ultrapasssa 100 caracteres
if len(post) > 100:
    print("post muito longo!")
else:
    print("Post publicado")
    

minimo = 10
max = 280

post = input("Digite o seu post: ")

quantidade_caracteres = len(post)

if quantidade_caracteres < minimo:
    faltam = minimo - quantidade_caracteres
    print("Faltam {faltam} caracteres para atingir o mínimo.")
elif quantidade_caracteres > max:
    ultrapassa = quantidade_caracteres - max
    print("Ultrapassa {ultrapassa} caracteres do maxímo.")
else:
    print("Post publicado com sucesso!") 

    # Comentário    