# Tiago Vieira da Silva - aluno no. 99335

# funcoes de validacao de argumentos:
def eh_tabuleiro(tab):  # universal -> booleano
    """
    Analisa se o argumento que foi introduzido satisfaz as condicoes para ser considerardo um tabuleiro (ser um tuplo
    constituido por 3 tuplos, cada um deles constituido por 3 elementos, sendo que estes elementos terao que ser 1, -1
    ou 0)

    Argumentos:
        tab - Argumento que sera analisado.
    Retorno:
        True - O argumento e um tabuleiro.
        False - O argumento e um tabuleiro.
    """
    if not isinstance(tab, tuple):
        return False
    if len(tab) != 3:
        return False
    for elemts in tab:
        if type(elemts) != tuple:
            return False
        if len(elemts) != 3:
            return False
        for elemt in elemts:
            if type(elemt) != int:
                return False
            if elemt != 1 and elemt != 0 and elemt != -1:
                return False
    return True


def eh_posicao(pos):    # universal -> booleano
    """
    Indica se o argumento introduzido e uma posicao de um tabuleiro 3x3.

    Argumentos:
        pos - Argumento que sera analisado.
    Retorno:
        True - O argumento for uma posicao de um tabuleiro 3x3.
        False - O argumento nao e uma posicao de um tabuleiro 3x3.
    """
    if type(pos) == int and 1 <= pos <= 9:
        return True
    else:
        return False


def eh_posicao_livre(tab, pos):     # tabuleiro x posicao -> booleano
    """
    Indica se certa posicao do tabuleiro se encontra livre.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro).
        pos - posicao
    Retorno:
        True se a posicao esta livre.
        False se a posicao esta ocupada.
    """
    if not eh_tabuleiro(tab):   # verifica se o tabuleiro inserido e valido
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if not eh_posicao(pos):   # verifica se a posicao inserida e valido
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    elemts = eh_elementos(tab)

    return eh_elemt_livre(pos, elemts)


# funcoes de obtencao de elementos do tabuleiro:
def obter_coluna(tab, num_coluna):      # tabuleiro x inteiro -> vector
    """
    Permite obter uma coluna do tabuleiro.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro )
        num_coluna - O numero da coluna pretendida.
    Retorno:
        Coluna pretendida.
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    if type(num_coluna) != int or num_coluna > len(tab) or num_coluna <= 0:  # len(tab) = lado do tabuleiro = 3
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    # funcao
    coluna = ()

    for linha in tab:
        coluna = coluna + (linha[num_coluna - 1], )  # "num_coluna - 1" ira ser o indice do elemento pretendido na linha

    return coluna


def obter_linha(tab, num_linha):    # tabuleiro x inteiro -> vector
    """
    Permite obter uma linha do tabuleiro.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro )
        num_linha - O numero da linha pretendida.
    Retorno:
        Linha pretendida.
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    if type(num_linha) != int or num_linha > len(tab) or num_linha <= 0:     # len(tab) = lado do tabuleiro = 3
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    # funcao
    linha = tab[num_linha - 1]      # num_linha - 1 = indice da linha no tuplo do tabuleiro

    return linha


def obter_diagonal(tab, num_diagonal):  # len(tab) = lado do tabuleiro = 3
    """
    Permite obter uma diagonal do tabuleiro.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro)
        num_diagonal - 1 para obter a diagonal do canto superior esquerdo -> canto inferior direito
                       2 para obter a diagonal do canto inferior esquerdo -> canto superior direito
    Retorno:
        Diagonal pretendida.
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if type(num_diagonal) != int or num_diagonal < 1 or num_diagonal > 2:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')

    # funcao
    diagonal = ()

    if num_diagonal == 1:
        i = 0
        for linha in tab:
            diagonal = diagonal + (linha[i], )
            i += 1
    elif num_diagonal == 2:
        i = 2
        for linha in tab:
            diagonal = (linha[i],) + diagonal
            i -= 1

    return diagonal


def obter_posicoes_livres(tab):     # tabuleiro -> vector
    """
    Indica as posicoes livres num tabuleiro.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro).
    Retorno:
        Tuplo com as posicoes livres do tabuleiro.
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    # funcao
    pos_livres = ()

    elemts = eh_elementos(tab)

    for pos in range(1, 10, 1):
        if eh_elemt_livre(pos, elemts):
            pos_livres = pos_livres + (pos, )

    return pos_livres


# funcoes de analise e interacao com o tabuleiro:
def tabuleiro_str(tab):     # tabuleiro -> cad. carateres
    """
    Representa graficamente o tabuleiro atraves de uma cadeia de caracteres

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro)
    Retorno:
        Cadeia de caracteres que dando "print" representa graficamente o tabuleiro
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    # funcao
    rep = ''
    cont = 1
    for linha in tab:
        num_elemt = 1
        for elemt in linha:
            if elemt == 0:
                rep += '   '
            if elemt == 1:
                rep += ' X '
            if elemt == -1:
                rep += ' O '
            if num_elemt == 3 and cont != 9:    # trocar de linha e adicionar separador de linha
                rep += '\n-----------\n'
            elif num_elemt != 3:    # adicionar separador de coluna
                rep += '|'
            num_elemt += 1
            cont += 1
    return rep


def jogador_ganhador(tab):      # tabuleiro -> inteiro
    """
    Indica se ha algum jogador que ganhou com base no tabuleiro fornecido.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro).
    Retorno:
        1 - o jogador "X" ganhou o jogo
        -1 - o jogador "O" ganhou o jogo
        0 - ninguem ganhou o jogo
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')

    # funcao

    # verificar se o jogo esta ganho pelas diagonais
    for i in range(1, 3, 1):
        analise = obter_diagonal(tab, i)
        if analise == (1, 1, 1):
            return 1
        if analise == (-1, -1, -1):
            return -1

    # verificar se o jogo esta ganho pelas linhas
    for linha in tab:
        if linha == (1, 1, 1):
            return 1
        if linha == (-1, -1, -1):
            return -1

    # verificar se o jogo esta ganho pelas colunas
    for i in range(len(tab)):
        coluna = obter_coluna(tab, i+1)
        if coluna == (1, 1, 1):
            return 1
        if coluna == (-1, -1, -1):
            return -1

    # retorna 0 porque ninguem ganhou
    return 0


def marcar_posicao(tab, jogador, pos):  # tabuleiro x inteiro x posicao -> tabuleiro
    """
    Marca a posicao de um jogador no tabuleiro.

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro).
        jogador - "1" para o jogador "X"
                  "-1" para o jogador "O"
    Retorno:
        Tuplo do tabuleiro com a posicao pretendida marcada.

    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not eh_posicao(pos):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not eh_posicao_livre(tab, pos):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if not eh_jogador(jogador):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')

    # funcao
    novo_tab = ()
    novo_tuplo = ()

    for i in range(len(tab)):   # len(tab) = 3 = lado do tabuleiro
        if i == (pos-1) // len(tab):    # o quociente desta divisao vai dar o indice do tuplo de tab que ira ser marcado
            temp_tuple = tab[i]
            for k in range(len(tab)):
                if k == (pos-1) % len(tab):     # o resto desta divisao ira dar o indice do elemento no tuplo que
                    novo_tuplo = novo_tuplo + (jogador, )                                       # queremos marcar
                else:
                    novo_tuplo = novo_tuplo + (temp_tuple[k], )
            novo_tab = novo_tab + (novo_tuplo, )
        else:
            novo_tab = novo_tab + (tab[i], )

    return novo_tab


def escolher_posicao_manual(tab):
    """
    Le a posicao do tabuleiro introduzida pelo utilizador e devolve a posicao

    Argumento:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro).
    Retorno:
        Inteiro correspondente a posicao escolhida pelo utilizador
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):  # verifica se o tabuleiro inserido e valido
        raise ValueError('escolher_posicao_manual: o argumento e invalido')

    # funcao
    print('Turno do jogador. Escolha uma posicao livre:', end='')
    pos = eval(input(' '))

    # validacao do input
    if not isinstance(pos, int):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    if not eh_posicao(pos):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    if not eh_posicao_livre(tab, pos):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

    return pos


def escolher_posicao_auto(tab, jogador, modo_jogo):
    """
    Devolve uma posicao livre no tabuleiro para o qual se deve jogar com base no modo de jogo

    Argumentos:
        tab - Tabuleiro ( help(eh_tabuleiro) para saber as condicoes para ser um tabuleiro)
        jogador - "1" para o jogador "X"
                  "-1" para o jogador "O"
        modo_jogo - Modo de jogo (basico, normal, perfeito)
    Retorno:
        Inteiro correspondente a posicao ideal para o computador jogar.
    """
    # validacao de argumentos
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if not eh_jogador(jogador):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if not eh_modo_jogo(modo_jogo):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')

    # selecao do modo de jogo
    if modo_jogo == 'basico':
        return modo_basico(tab)
    if modo_jogo == 'normal':
        return modo_normal(tab, jogador)
    if modo_jogo == 'perfeito':
        return modo_perfeito(tab, jogador)


# modos de jogo: tab (x jogador) -> posicao
def modo_basico(tab):
    if centro(tab) != 0:
        return centro(tab)
    if canto_vazio(tab) != 0:
        return canto_vazio(tab)
    if lateral_vazia(tab) != 0:
        return lateral_vazia(tab)
    return 0


def modo_normal(tab, jogador):
    if vitoria(tab, jogador) != 0:
        return vitoria(tab, jogador)
    if bloqueio(tab, jogador) != 0:
        return bloqueio(tab, jogador)
    if centro(tab) != 0:
        return centro(tab)
    if canto_oposto(tab, jogador) != 0:
        return canto_oposto(tab, jogador)
    if canto_vazio(tab) != 0:
        return canto_vazio(tab)
    if lateral_vazia(tab) != 0:
        return lateral_vazia(tab)
    return 0


def modo_perfeito(tab, jogador):
    if vitoria(tab, jogador) != 0:
        return vitoria(tab, jogador)
    if bloqueio(tab, jogador) != 0:
        return bloqueio(tab, jogador)
    if bifurcacao(tab, jogador) != 0:
        posis = bifurcacao(tab, jogador)
        pos = posis[0]
        return pos
    if bloq_bifurcacao(tab, jogador) != 0:
        return bloq_bifurcacao(tab, jogador)
    if centro(tab) != 0:
        return centro(tab)
    if canto_oposto(tab, jogador) != 0:
        return canto_oposto(tab, jogador)
    if canto_vazio(tab) != 0:
        return canto_vazio(tab)
    if lateral_vazia(tab) != 0:
        return lateral_vazia(tab)
    return 0


# funcoes auxiliares
def eh_elementos(tab):  # tabuleiro -> elementos do tabuleiro
    elemts = ()
    for linha in tab:
        for elem in linha:
            elemts = elemts + (elem,)

    return elemts


def jogador_contador(tuplo, jogador):   # tuplo x jogador -> numero de vezes que o jogador aparece no tuplo
    cont = 0
    for elemt in tuplo:
        if elemt == jogador:
            cont += 1
    return cont


def index_linha(pos):   # posicao -> indice da linha onde se encontra essa posicao
    if 0 < pos <= 3:
        return 1
    elif 3 < pos <= 6:
        return 2
    elif 6 < pos <= 9:
        return 3


def index_coluna(pos):  # posicao -> indice da coluna onde se encontra essa posicao
    if pos == 1 or pos == 4 or pos == 7:
        return 1
    elif pos == 2 or pos == 5 or pos == 8:
        return 2
    elif pos == 3 or pos == 6 or pos == 9:
        return 3


def index_diagonal(pos):    # posicao -> inteiro (indice da diagonal onde se encontra essa posicao (1 ou 2))
    if pos == 1 or pos == 9:
        return 1,
    elif pos == 3 or pos == 7:
        return 2,
    elif pos == 5:
        return 1, 2
    return 0


def eh_elemt_livre(pos, elemts):   # posicao x tuplo -> Booleano (se certa posicao esta livre)
    if elemts[pos-1] == 0:
        return True
    else:
        return False


def eh_jogador(jogador):    # inteiro -> Booleano (se o inteiro e ou nao um jogador)
    if jogador == 1 and type(jogador) == int:
        return True
    elif jogador == -1 and type(jogador) == int:
        return True
    else:
        return False


def eh_modo_jogo(modo_jogo):    # string -> Booleano (se a string e ou nao um modo de jogo)
    if modo_jogo == 'basico' or modo_jogo == 'normal' or modo_jogo == 'perfeito':
        return True
    else:
        return False


def eh_x_o(x_o):    # string -> Booleano (se a string e um X ou um O)
    if x_o == 'X' or x_o == 'O':
        return True
    else:
        return False


# funcoes de decisao de jogada:
def vitoria(tab, jogador):
    """
    Deteta uma posicao onde possa haver uma possivel vitoria, retornando essa mesma posicao
    """
    elemts = eh_elementos(tab)
    for i in range(len(elemts)):
        pos = i+1
        if elemts[i] == 0:
            linha = obter_linha(tab, index_linha(pos))
            coluna = obter_coluna(tab, index_coluna(pos))
            if jogador_contador(linha, jogador) == 2:
                return pos
            if jogador_contador(coluna, jogador) == 2:
                return pos
            if pos == 1 or pos == 3 or pos == 5 or pos == 7 or pos == 9:
                for k in index_diagonal(pos):
                    diagonal = obter_diagonal(tab, k)
                    if jogador_contador(diagonal, jogador) == 2:
                        return pos
    return 0


def bloqueio(tab, jogador):
    """
    Retorna a posicao onde podera existir uma vitoria do adversario, bloqueando-a
    """
    pos = vitoria(tab, -jogador)
    return pos


def bifurcacao(tab, jogador):
    """
    Deteta se ha uma bifurcacao, e retorna a posicao desta.
    """
    posis = ()
    elemts = eh_elementos(tab)
    for i in range(len(elemts)):
        pos = i + 1
        if elemts[i] == 0:  # analisa-se a posicao onde pode haver biforcacao
            linha = obter_linha(tab, index_linha(pos))
            coluna = obter_coluna(tab, index_coluna(pos))
            if jogador_contador(linha, jogador) == 1 and jogador_contador(coluna, jogador) == 1:
                if jogador_contador(linha, -jogador) == 0 and jogador_contador(coluna, -jogador) == 0:
                    posis = posis + (pos, )     # linha e a coluna que biforcam tem cada uma apenas um elemento do
            if pos == 1 or pos == 9:                                                                     # jogador
                diagonal = obter_diagonal(tab, 1)
                posis = aux_bifurcacao(diagonal, jogador, linha, coluna, posis, pos)
            if pos == 3 or pos == 7:
                diagonal = obter_diagonal(tab, 2)
                posis = aux_bifurcacao(diagonal, jogador, linha, coluna, posis, pos)
            if pos == 5:
                return 0
    if len(posis) >= 1:
        return posis
    else:
        return 0


def aux_bifurcacao(diagonal, jogador, linha, coluna, posis, pos):
    for k in range(len(diagonal)):
        if jogador_contador(diagonal, jogador) == 1 and jogador_contador(linha, jogador) == 1:
            if jogador_contador(diagonal, -jogador) == 0 and jogador_contador(linha, -jogador) == 0:
                posis = posis + (pos,)
                # linha e a diagonal que biforcam tem cada uma apenas um elemento do jogador
                break
        if jogador_contador(diagonal, jogador) == 1 and jogador_contador(coluna, jogador) == 1:
            if jogador_contador(diagonal, -jogador) == 0 and jogador_contador(coluna, -jogador) == 0:
                posis = posis + (pos,)
                # coluna e a diagonal que biforcam tem cada uma apenas um elemento do jogador
                break
    return posis


def bloq_bifurcacao(tab, jogador):
    """
    Faz o bloqueio da bifurcacao do adversario.
    """
    posis = bifurcacao(tab, -jogador)
    if posis == 0:
        return 0
    if len(posis) == 1:
        return posis[0]
    elif 1 < len(posis):    # se o numero de bifurcacoes for maior que 1, joga-se para forcar o adversario a bloquear
        elemts = eh_elementos(tab)
        for i in range(len(elemts)):
            if elemts[i] == 0:
                pos = i + 1
                temp_tab = marcar_posicao(tab, jogador, pos)
                if vitoria(temp_tab, jogador) != 0 and vitoria(temp_tab, jogador) not in posis:
                    return pos

    return 0


def centro(tab):
    """
    Retorna a posicao central se esta estiver vazia
    """
    elemts = eh_elementos(tab)
    pos = 5
    if elemts[pos-1] == 0:
        return pos
    else:
        return 0


def canto_oposto(tab, jogador):
    """
    Retorna a posicao de um canto oposto a um canto onde o adversario tenha jogado.
    """
    adversario = -jogador
    elemts = eh_elementos(tab)
    if elemts[0] == 0 and elemts[8] == adversario:
        return 1
    if elemts[8] == 0 and elemts[0] == adversario:
        return 9
    if elemts[2] == 0 and elemts[6] == adversario:
        return 3
    if elemts[6] == 0 and elemts[2] == adversario:
        return 7
    return 0


def canto_vazio(tab):
    """
    Retorna a posicao de um canto que esteja vazio.
    """
    elemts = eh_elementos(tab)
    for i in range(len(elemts)):
        if (i + 1) % 2 != 0 and (i + 1) != 5:
            if elemts[i] == 0:
                pos = i + 1
                return pos

    return 0


def lateral_vazia(tab):
    """
    Retorna a posicao de uma lateral do tabuleiro que esteja vazia.
    """
    elemts = eh_elementos(tab)
    for i in range(len(elemts)):
        if (i + 1) % 2 == 0:
            if elemts[i] == 0:
                pos = i + 1
                return pos

    return 0


# jogo do galo
def jogo_do_galo(x_o, modo_jogo):
    """
    Executa o jogo do galo:

    Argumentos:
        x_o - Escolha do jogador entre "X" e "O"
        modo_jogo - Escolha do jogador do modo de jogo
    Retorno:
        Vencedor do jogo.
    """
    if not eh_modo_jogo(modo_jogo):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    if not eh_x_o(x_o):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.')
    print('O jogador joga com ' + "'" + x_o + "'" + '.')
    if x_o == 'O':
        jogador = -1
    elif x_o == 'X':
        jogador = 1
    jogadas = 0
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    if jogador == -1:
        print('Turno do computador (' + modo_jogo + '):')
        pos = escolher_posicao_auto(tab, -jogador, modo_jogo)
        tab = marcar_posicao(tab, -jogador, pos)
        print(tabuleiro_str(tab))
        jogadas += 1
    while jogadas < 9:
        pos = escolher_posicao_manual(tab)
        tab = marcar_posicao(tab, jogador, pos)
        print(tabuleiro_str(tab))
        if jogador_ganhador(tab) == -1:
            return 'O'
        if jogador_ganhador(tab) == 1:
            return 'X'
        jogadas += 1
        if jogadas >= 9:
            break
        print('Turno do computador (' + modo_jogo + '):')
        pos = escolher_posicao_auto(tab, -jogador, modo_jogo)
        tab = marcar_posicao(tab, -jogador, pos)    # nao uso uma funcao para o codigo repetido porque
        print(tabuleiro_str(tab))                   # envolveria tornar o codigo mais complexo e
        if jogador_ganhador(tab) == -1:             # a leitura mais dificl
            return 'O'                              # as linhas que se poupariam sao muito poucas
        if jogador_ganhador(tab) == 1:
            return 'X'
        jogadas += 1
    return 'EMPATE'
