# Número de testes a ser realizado
numero_linhas = int(input("Insira quantos testes seram realizado: "))


for i in range(1, numero_linhas + 1): # Criar a quantidade de testes digitada em "número_lihas"
    nivel_de_poder = int(input("Insira o nível de poder a ser verificado: ")) 
    if nivel_de_poder <= 8000:
        resultado = "Inseto!"
    else:
        resultado = "Mais de 8000!"
    
    print(resultado)