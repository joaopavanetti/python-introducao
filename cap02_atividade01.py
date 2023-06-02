from os import system
system('cls')

print("*************************")
print("Adivinhe qual é o Número!")
print("*************************")

NUMERO_SECRETO = 83 #CONSTANTE

rodada = 1
total_de_tentativas = 3

while (rodada <= total_de_tentativas):
    tentativa = input('Tente acertar o número')
    print('Voce digitou: ', tentativa) 
    rodada += 1
    
    try:
        tentativa_int = int(tentativa)
    except ValueError:
        print('Valor invalido inform o valor inteiro')
        exit()
    except Exception as e: 
        print(f'ERRO: {e}')
        exit()
    else:
        pass
        
     

    # if (NUMERO_SECRETO == tentativa_int):
    #     print("Boa sorte tentativa. ACERTOU!")
    #     # exit()
    #     break

    # else:  
    #     ('Não foi desta vez. ERROU!')   
        
    # print('GAMER OVER')    
    # print('Obrigado por participar!')

    acerto = tentativa_int == NUMERO_SECRETO
    ehmaior = tentativa_int > NUMERO_SECRETO
    ehmenor = tentativa_int < NUMERO_SECRETO

    if acerto:
        print('Boa tentativa. ACERTO!!! !')
    else:
        print('Não foi desta vez. ERROU!!!!')
        if ehmaior:
            print('Sua tentativa foi MAIOR que o número secreto.')
        if ehmenor:
            print('Sua tentativa foi MENOR que o número secreto')    
            print('GAMER OVER!')
    print('Obrigado por participar')

  
    
    








    

    

