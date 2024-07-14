# Função para mostrar as instruções de início do game.

def exibir_instrucoes():
    print("Bem-vindo ao Take Trash Now – T.T.N. Project!")
    print("Uma viagem às profundezas do mar em prol da reciclagem.")
    print("Pressione Enter para iniciar o jogo.")
    input()

# Função para exibir a charada que compõe o game.

def exibir_charadas():
    print("\nSEPARAÇÃO DO LIXO")
    print("Observe o que diz cada cor de lata de reciclagem e suas respectivas designações:")
    print("— Eu sou azulzinha, e procuro o que enxuga suas lágrimas.")
    print("— Eu sou a latinha de cerveja, e procuro a cor do sol.")
    print("— Eu sou verdinha, e procuro as janelas dos carros.")
    print("— Eu sou a sacolinha, e procuro a cor do amor.")
    print("Digite suas respostas abaixo:")

# Função para coletar as respostas do jogador e validá-las para continuação do game.

def obter_respostas():
    respostas = []
    perguntas = [
        "Digite a resposta para a azulzinha: ",
        "Digite a resposta para a latinha de cerveja: ",
        "Digite a resposta para a verdinha: ",
        "Digite a resposta para a sacolinha: "
    ]
    for i in range(4):
        resposta = input(perguntas[i])
        while not resposta.isalpha():
            print("Resposta inválida. Por favor, insira apenas letras.")
            resposta = input(perguntas[i])
        respostas.append(resposta.lower())
    return respostas

# Função para verificar se as respostas do usuário estão corretas.

def verificar_respostas(respostas):
    respostas_corretas = [
        "papel", 
        ["amarela", "amarelo"], 
        "vidro", 
        ["vermelha", "vermelho"]
    ]
    for i in range(4):
        if isinstance(respostas_corretas[i], list):
            if respostas[i] not in respostas_corretas[i]:
                return False
        else:
            if respostas[i] != respostas_corretas[i]:
                return False
    return True

# Funções para pegar a resposta do usuário e transformar na senha correta

def obter_senha(respostas):
    return ''.join([resposta[0] for resposta in respostas])

def verificar_senha(senha, senha_correta):
    return senha == senha_correta

# Função para exibir a mensagem final de falha ou sucesso

def exibir_mensagem_final(sucesso):
    if sucesso:
        print("\nParabéns, você resolveu bem as charadas e está a um passo de salvar o planeta!")
        print("Você ganhou um prêmio! Leve até um de nossos postos algum lixo da praia, diga a senha e receba um brinde reciclado!")
    else:
        print("\nInfelizmente, a senha está incorreta. Tente novamente!")

# Função chave da aplicação, funcionando como um fluxograma do app

def main():
    exibir_instrucoes()
    exibir_charadas()
    respostas = obter_respostas()

    if verificar_respostas(respostas):
        senha = obter_senha(respostas)
        print("\nTendo em mente as iniciais de cada item inserido, insira-as como senha para ganhar um reconhecimento.")
        senha_usuario = input("Digite a senha: ").lower()
        
        senha_correta = obter_senha(["papel", "amarela", "vidro", "vermelha"])
        
        if verificar_senha(senha_usuario, senha_correta):
            exibir_mensagem_final(True)
        else:
            exibir_mensagem_final(False)
    else:
        print("\nRespostas incorretas. Tente novamente!")

if __name__ == "__main__":
    main()