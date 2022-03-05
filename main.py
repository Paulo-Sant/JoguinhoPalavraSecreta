nome_secreto = 'python'          # a palavra secreta
letras_digitadas = []            # Armazena as letras digitadas
tentativas = 3                   # numero de tentativas Restantes

while True:
    if tentativas <= 0:
        print('Infelizmente você perdeu')
        break

    letra = input('Digite uma Letra: ')

    if len(letra) > 1:
        print('Digite apenas um Letra.')
        continue
    letras_digitadas.append(letra)  # cada letra digitada é adicionada ao vetor letras_digitadas

    if letra in nome_secreto:
        print('Letra Correta!')
    else:
        print('Letra Incorreta')  # remove a letra incorreta do vetor letras_digitadas
        letras_digitadas.pop()

    secreto = ''
    for letra_secreta in nome_secreto:
        if letra_secreta in letras_digitadas:  # incrementa as letras corretas na variável secreto
            secreto += letra_secreta
        else:
            secreto += '*'

    if secreto == nome_secreto:
        print('--------------------------')
        print('PARABÉNS!! Você acertou!')
        print(f'A palavra era {secreto}')
        print('--------------------------')
        break
    else:
        print(f'A palavra secreta está assim: {secreto}')  # informa o estado atual do jogo

    if letra not in nome_secreto:  # caso erre a letra, você perde uma tentativa
        tentativas -= 1

    print(f'Número restantes de tentativas: {tentativas}\n')
