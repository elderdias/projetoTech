
def cifra_cesar_criptografa(mensagem,chave,operacao):
    print("Este é o software da Cifra de César!")

    status = "" #string chamada no final do programa

    while (status != "Sair"): #o programa continua rodando até que no final o usuário digite "Sair"
        print("\n")

    #as variáveis a seguir armazenam os atributos utilizados nas operações e comparações
        direcao = 'D'
        while operacao!=1 and operacao!=2:
            operacao = 1

        if operacao==1:
                operacao_frase='Criptografar'
        elif operacao==2:
                operacao_frase='Decriptografar'

        frase = mensagem.upper()
        while direcao != 'D' and direcao != 'E':
            direcao = (input(f'digite D para criptografar para a Direita e E para a Esquerda: ')) #a variável direção será usada antes dos ifs de operacao para escolher a direcao da criptografia


        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,'!?()#"
        fraseAlterada = "" #armazena a string final com o método escolhido aplicado

        for indice in range (0, len(frase)): #percorre a frase sobre a qual a operação será realizada

            indiceAlfabeto = 0 #utilizado para acessar as posições dos alfabetos minusculo e maiusculo

            if (frase[indice] not in alfabeto):
                fraseAlterada += " "
                continue

            while (frase[indice] != alfabeto[indiceAlfabeto]): #quando encontra a letra da frase correspondente nos alfabetos, a variável indiceAlfabeto armazena sua posição
                indiceAlfabeto += 1

            if direcao == 'D':

                if (operacao == 1): 
                    indiceParaTrocar = indiceAlfabeto + chave #soma a chave com o indice da letra encontrada
                    #ajusta o indice para que fique um número entre 0 e 25, caso a soma resulte em um número maior
                    while indiceParaTrocar > 43:
                        indiceParaTrocar -= 44

                #verfifica qual tipo de operação o usuário quer realizar  
                if (operacao == 2): 
                    indiceParaTrocar = indiceAlfabeto - chave #soma a chave com o indice da letra encontrada
                    #ajusta o indice para que fique um número entre 0 e 25, caso a soma resulte em um número maior
                    while indiceParaTrocar < 0:
                        indiceParaTrocar += 44

            fraseAlterada += alfabeto[indiceParaTrocar]
        print("Fechando app...")
        return fraseAlterada