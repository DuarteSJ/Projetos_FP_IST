"""Duarte São José nº 103708
este programa contém cinco tarefas independentes para identificar e corrigir os
problemas de uma base de dados (Buggy Data Base, BDB) que ficou corrompida por
causas desconhecidas."""


def corrigir_palavra(palavra):
    """corrigir_palavra: cad. caracteres -> cad. caracteres
    Retira as combinações entre letras minúsculas e maiúsculas
    iguais (ex "aA", "bB", "Aa) existentes na palavra e devolve-a
    em seguida"""

    contador = 0
    while contador < len(palavra):
        if contador != len(palavra) - 1:
            if palavra[contador].lower() == palavra[contador + 1].lower() \
                    and palavra[contador] != palavra[contador + 1]:
                letras_a_remover = palavra[contador] + palavra[contador + 1]
                palavra = palavra.replace(letras_a_remover, '')
                contador = 0
            else:
                contador += 1
        else:
            contador += 1
    return palavra


def eh_anagrama(palavra_1, palavra_2):
    """eh_anagrama: cad. carateres x cad. carateres -> booleano
    Recebe duas cadeias de carateres correspondentes a duas palavras e devolve
    True se e só se estas forem anagramas e não corresponderem à mesma palavra"""

    palavra_1 = sorted(palavra_1.lower())
    palavra_2 = sorted(palavra_2.lower())
    if palavra_1 == palavra_2:
        return True
    return False


def corrigir_doc(texto):
    """ corrigir_doc: cad. carateres -> cad. carateres
    Recebe o texto corrompido e devolve-o corrigido"""

    if type(texto) != str:
        raise ValueError('corrigir_doc: argumento invalido')

    if texto == '' or texto == ' ' or '  ' in texto:
        raise ValueError('corrigir_doc: argumento invalido')

    for caracter in texto:
        if caracter not in 'QWERTYUIOPÇLKJHGFDSAZXCVBNM qwertyuiopçlkjhgfdsazxcvbnm':
            raise ValueError('corrigir_doc: argumento invalido')
    else:
        texto = corrigir_palavra(texto)
        texto = texto.split()
        contador_1 = 0
        while contador_1 < len(texto):
            contador_2 = contador_1 + 1
            while contador_2 < len(texto):
                if texto[contador_1].lower() != texto[contador_2].lower():
                    if eh_anagrama(texto[contador_1], texto[contador_2]):
                        texto.remove(texto[contador_2])
                        contador_2 = 0
                contador_2 += 1
            contador_1 += 1
        texto = " ".join(texto)
        return texto


def obter_posicao(direcao, posicao_inicial):
    """obter_posicao: cad. carateres x inteiro
    Recebe uma cadeia de carateres (com apenas um carácter) e um inteiro.
    A cadeia de caracteres representa a direção de um único movimento
    (‘C’ (movimento para cima), ‘B’(movimento para baixo),‘E’(movimento para
    a esquerda) ou ‘D’(movimento para a direita)). O inteiro representa a
    posicao inicial (previa ao movimento).Esta função devolve o inteiro
    correspondente à posição final, ou seja, a posição pós-movimento."""

    if posicao_inicial != 1 and posicao_inicial != 2 and posicao_inicial != 3 and direcao == 'C':
        return posicao_inicial - 3
    elif direcao == 'C':
        return posicao_inicial
    if posicao_inicial != 3 and posicao_inicial != 6 and posicao_inicial != 9 and direcao == 'D':
        return posicao_inicial + 1
    elif direcao == 'D':
        return posicao_inicial
    if posicao_inicial != 7 and posicao_inicial != 8 and posicao_inicial != 9 and direcao == 'B':
        return posicao_inicial + 3
    elif direcao == 'B':
        return posicao_inicial
    if posicao_inicial != 1 and posicao_inicial != 4 and posicao_inicial != 7 and direcao == 'E':
        return posicao_inicial - 1
    elif direcao == 'E':
        return posicao_inicial


def obter_digito(sequencia_movimentos, posicao):
    """ obter_digito: cad. carateres x inteiro -> inteiro
    Esta função recebe uma cadeia de carateres correspondente a uma sequência
    de um ou mais movimentos e um inteiro que representa a posição inicial,
    devolvendo o inteiro que corresponde ao dígito a marcar após finalizar
    todos os movimentos."""

    for movimento in sequencia_movimentos:
        posicao = obter_posicao(movimento, posicao)

    return posicao


def obter_pin(conjunto_sequencias_movimentos):
    """obter_pin: tuplo -> tuplo
    Esta função recebe um tuplo com 4 a 10 sequências de movimentos e, após
    testar a validade do seu argumento, devolve o tuplo dos inteiros que contém
    o pin codificado de acordo com o tuplo de movimentos."""

    def valida_obter_pin(conjunto_sequencias_movimentos):
        """ valida_obter_pin: tuplo -> booleano
        Verifica se o argumento da função "obter_pin"
        é ou não válido """

        if type(conjunto_sequencias_movimentos) != tuple or len(conjunto_sequencias_movimentos) < 4 \
                or len(conjunto_sequencias_movimentos) > 10:
            raise ValueError('obter_pin: argumento invalido')
        for sequencia in conjunto_sequencias_movimentos:
            if type(sequencia) != str or len(sequencia) < 1:
                raise ValueError('obter_pin: argumento invalido')
            for caracter in sequencia:
                if caracter != 'C' and caracter != 'B' and caracter != 'E' and caracter != 'D':
                    raise ValueError('obter_pin: argumento invalido')

    valida_obter_pin(conjunto_sequencias_movimentos)
    pin = ()
    dig = 5
    for sequencia in conjunto_sequencias_movimentos:
        dig = obter_digito(sequencia, dig)
        pin = pin + (dig,)
    return pin


def eh_entrada(entrada_universal):
    """eh_entrada: universal -> booleano
    Esta função recebe um argumento de qualquer tipo e devolve True se e só
    se o seu argumento corresponde a uma entrada da BDB (não garante que a
    entrada não é corrupta)"""

    if type(entrada_universal) != tuple or len(entrada_universal) != 3:
        return False
    if type(entrada_universal[0]) != str or type(entrada_universal[1]) != str\
            or type(entrada_universal[2]) != tuple:
        return False
    if entrada_universal[0].lower() != entrada_universal[0]\
            or entrada_universal[1].lower() != entrada_universal[1]:
        return False
    for caracter in entrada_universal[0]:
        if not caracter.isalpha() and caracter != '-':
            return False
    for caracter in entrada_universal[1][1:6]:
        if not caracter.isalpha():
            return False
    if entrada_universal[1][0] != '[' or entrada_universal[1][-1] != ']':
        return False
    if len(entrada_universal[2]) < 2 or len(entrada_universal[1]) != 7:
        return False
    if entrada_universal[0][0] == '-' or entrada_universal[0][len(entrada_universal[0]) - 1] == '-':
        return False
    for num in entrada_universal[2]:
        if type(num) != int or num <= 0:
            return False
    return True


def validar_cifra(cifra, cadeia_de_controlo):
    """validar_cifra: cad. carateres x cad. carateres -> booleano
    Esta função recebe duas cadeias de carateres: cifra e sequência de controlo).
    A função devolve True se e só se a sequência de controlo for coerente com a
    cifra."""

    # Averiguar qual deveria ser a cadeia de controlo correta para a cifra dada:
    cifra = ''.join(sorted(cifra.replace('-', '')))
    contador = 0
    contador_2 = 1

    while contador_2 < len(cifra):
        if cifra[contador] != cifra[contador_2]:
            cifra = cifra[:contador + 1] + ' ' + cifra[contador_2:]
            contador += 1
            contador_2 += 1
        contador += 1
        contador_2 += 1
    lista_letras = cifra.split(' ')
    contador = -1
    lista_letras_ordenadas = lista_letras.copy()

    while contador + 2 < len(lista_letras_ordenadas):
        contador += 1
        if len(lista_letras_ordenadas[contador]) < len(lista_letras_ordenadas[contador + 1]):
            lista_letras_ordenadas = lista_letras_ordenadas[:contador] + [lista_letras_ordenadas[contador + 1]] + \
                                     [lista_letras_ordenadas[contador]] + lista_letras_ordenadas[contador + 2:]
            contador = -1

    cadeia_de_controlo_correta = '[' + lista_letras_ordenadas[0][0] + lista_letras_ordenadas[1][0] + \
                                 lista_letras_ordenadas[2][0] + lista_letras_ordenadas[3][0] + \
                                 lista_letras_ordenadas[4][0] + ']'

    # Comparar aquela que deveria ser a cadeia de controlo correta com a dada:
    if cadeia_de_controlo_correta == cadeia_de_controlo:
        return True
    return False


def filtrar_bdb(lista_entradas_bdb):
    """filtrar_bdb: lista -> lista
    Esta função recebe uma lista que contém uma ou mais entradas da BDB e,
    após verificar a validade do seu argumento, devolve uma lista que apenas
    contém as entradas em que o checksum não é coerente com a cifra correspondente,
    pela mesma ordem que estas aparecem na lista original."""

    if type(lista_entradas_bdb) != list or lista_entradas_bdb == []:
        raise ValueError("filtrar_bdb: argumento invalido")
    lista_nao_coerentes = []
    for entrada_bdb in lista_entradas_bdb:
        if not eh_entrada(entrada_bdb):
            raise ValueError("filtrar_bdb: argumento invalido")
        elif not validar_cifra(entrada_bdb[0], entrada_bdb[1]):
            lista_nao_coerentes = lista_nao_coerentes + [entrada_bdb]
    return lista_nao_coerentes


def obter_num_seguranca(tuplo):
    """ obter_num_seguranca: tuplo -> inteiro
    Esta função calcula o número de segurança a partir do tuplo que lhe é fornecido,
    calculando a menor diferença entre dois valores do tuplo."""

    cont = 0
    diferenca = -1
    while cont < len(tuplo):
        cont2 = 0
        while cont2 < len(tuplo):
            if cont2 != cont:
                if abs(tuplo[cont] - tuplo[cont2]) < diferenca or diferenca == -1:
                    diferenca = abs(tuplo[cont] - tuplo[cont2])
            cont2 += 1
        cont += 1
    return diferenca


def decifrar_texto(cifra, n):
    """decifrar_texto; cad. caracteres x inteiro -> cad.caracteres
    Esta função recebe uma cadeia de caracteres correspondente a uma cifra e
    um número de segurança, que utiliza para descodificar essa cifra.
    A cifra é retornada ao utilizador"""

    n = n % 26
    tuplo_alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
                      , 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    for caracter in range(len(cifra)):
        if caracter < len(cifra):
            if cifra[caracter] == '-':
                cifra = cifra[:caracter] + ' ' + cifra[caracter + 1:]
            elif cifra[caracter] in tuplo_alfabeto:
                posicao = tuplo_alfabeto.index(cifra[caracter])
                if caracter % 2 == 0:
                    cifra = cifra[:caracter] + tuplo_alfabeto[posicao + n + 1] + cifra[caracter + 1:]
                else:
                    cifra = cifra[:caracter] + tuplo_alfabeto[posicao + n - 1] + cifra[caracter + 1:]
        else:
            if cifra[caracter] in tuplo_alfabeto:
                posicao = tuplo_alfabeto.index(cifra[caracter])
                if caracter % 2 == 0:
                    cifra = cifra[:caracter] + tuplo_alfabeto[posicao + n + 1]
                else:
                    cifra = cifra[:caracter] + tuplo_alfabeto[posicao + n - 1]
    return cifra


def decifrar_bdb(lst):
    """decifrar_bdb: lista -> lista
    Esta função recebe como argumento uma lista que contém uma ou mais entradas
    da BDB e, após verificar a validade do seu argumento, devolve uma lista com
    o texto das entradas decifradas na mesma ordem"""

    if type(lst) == list:
        lista_decifrada = []
        for i in lst:
            if eh_entrada(i):
                n_s = obter_num_seguranca(i[2])
                elemento_decifrado = decifrar_texto(i[0], n_s)
                lista_decifrada = lista_decifrada + [elemento_decifrado]
            else:
                raise ValueError('decifrar_bdb: argumento invalido')
        return lista_decifrada
    else:
        raise ValueError('decifrar_bdb: argumento invalido')


def eh_utilizador(info_utilizador):
    """eh_utilizador: universal -> booleano
    Recebe uma entrada universal e verifica se esta corresponde  a um dicionário
    que contéma a informação de utilizador relevante da BDB"""

    if type(info_utilizador) != dict or len(info_utilizador) != 3:
        return False
    if 'name' not in info_utilizador or 'pass' not in info_utilizador or 'rule' not in info_utilizador:
        return False
    if type(info_utilizador['name']) != str or type(info_utilizador['pass']) != str or type(
            info_utilizador['rule']) != dict:
        return False
    if len(info_utilizador['name']) < 1 or len(info_utilizador['pass']) < 1:
        return False
    if len(info_utilizador['rule']) != 2:
        return False
    if 'vals' not in info_utilizador['rule'] or 'char' not in info_utilizador['rule']:
        return False
    if type(info_utilizador['rule']['vals']) != tuple or type(info_utilizador['rule']['char']) != str:
        return False
    if len(info_utilizador['rule']['char']) != 1:
        return False
    if len(info_utilizador['rule']['vals']) != 2:
        return False
    if type(info_utilizador['rule']['vals'][0]) != int or info_utilizador['rule']['vals'][0] <= 0:
        return False
    if type(info_utilizador['rule']['vals'][1]) != int or info_utilizador['rule']['vals'][1] <= 0:
        return False
    if info_utilizador['rule']['vals'][0] > info_utilizador['rule']['vals'][1]:
        return False
    return True


def eh_senha_valida(senha, regra_individual):
    """eh_senha_valida: cad. carateres x dicionário -> booleano
    Função que recebe uma cadeia de carateres correspondente a uma senha
    e um dicionário contendo a regra individual de criação da senha, e devolve
    True se e só se a senha cumpre com todas as regras de definição (gerais
    e individual)."""

    def existe_repetido(senha):
        """cad. caracteres -> booleano
        Verifica se existem dois caracteres iguais seguidas na senha"""
        for caracter in range(len(senha) - 1):
            if senha[caracter] == senha[caracter + 1]:
                return True
        return False

    # Verificar se obedece às regras gerais:
    vogais_minusculas = 0
    for letra in senha:
        if letra in 'aeiou':
            vogais_minusculas += 1
    if vogais_minusculas < 3:
        return False
    if not existe_repetido(senha):
        return False

    # Verificar se obedece à regra individual:
    rep_vogal = 0
    for letra in senha:
        if letra == regra_individual['char']:
            rep_vogal += 1
    if regra_individual['vals'][1] >= rep_vogal >= regra_individual['vals'][0]:
        return True
    return False


def filtrar_senhas(lista_de_entradas):
    """filtrar_senhas: lista -> lista
    Esta função recebe uma lista contendo um ou mais dicionários
    correspondentes a entradas da BDB, e devolve uma lista ordenada
    alfabeticamente com os nomes dos utilizadores com senhas erradas"""

    if type(lista_de_entradas) != list or lista_de_entradas == []:
        raise ValueError('filtrar_senhas: argumento invalido')
    lista_entradas_pass_errada = []
    for entrada in lista_de_entradas:
        if not eh_utilizador(entrada):
            raise ValueError('filtrar_senhas: argumento invalido')
        if not eh_senha_valida(entrada['pass'], entrada['rule']):
            lista_entradas_pass_errada += [entrada['name']]
    return sorted(lista_entradas_pass_errada)

