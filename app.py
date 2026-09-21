import random

palavras = ["python", "frutas", "programacao", "computador", "teclado", "mouse", "monitor", "internet", "desenvolvimento", "linguagem"]

erro = 0

# escolha da palavra de forma aleatoria
palavra = random.randint(0, len(palavras)-1)
palavra_escolhida = palavras[palavra]


forca = ["""
       ------
       |    |
       |
       |
       |
       |
    ---------
    ""","""
       ------
       |    |
       |    o
       |
       |
       |
    ---------
    ""","""
       ------
       |    |
       |    o
       |    |
       |
       |
    ---------
    ""","""
         ------
         |    |
         |    o
         |   /|
         |   
         |   
      ---------
      ""","""
         ------
         |   |
         |   o
         |  /|\\
         |
         |
      ---------
      ""","""
         ------
         |    |
         |    o
         |   /|\\
         |   /
         |
      ---------
      ""","""
         ------
         |    |
         |    o
         |   /|\\
         |   / \\
         |
      ---------
      """]

palavra = palavra_escolhida
palavra_oculta = ("*" * len(palavra))
jogada_ja_feitas = []
inicio = True

while inicio == True:
    
    print(forca[erro])
    print(palavra_oculta)
    jogada = input("Digite uma letra: ")
    if jogada in jogada_ja_feitas:
        print("Letra já digitada.")
        continue
    jogada_ja_feitas.append(jogada)

    while True:
        lista = []
        for i in range(len(palavra)):
            if palavra[i] == jogada:
                lista.append(i)
            else:
                continue

        if lista:
            palavra_oculta = list(palavra_oculta)
            for i in lista:
                palavra_oculta[i] = jogada
            palavra_oculta = "".join(palavra_oculta)

            if palavra_oculta == palavra:
                print(f"A palavra era: '{palavra}'")
                print("Parabéns, você Acertou!")
                inicio = False
                break
            else:
                break
        else:
            erro += 1
            if erro == len(forca) - 1:
                print(forca[erro])
                print(f"A palavra era: '{palavra}'")
                print("Você perdeu!")
                inicio = False
                break
            else:
                print("Letra errada, digite outra.")
                break