"""Duarte São José    103708
Projeto 2
Simulação da evolução de um prado ao longo do tempo"""


# TAD_1 -> posicao

# construtores_posicao

def cria_posicao(abcissa, ordenada):
    """cria_posicao: int x int -> posicao
    Recebe dois inteiros, um que corresponde ao valor da abcissa e outro correspondente ao valor da ordenada.
    Após verificar a validade dos argumentos recebidos retorna a posição do prado por eles definida """

    if type(abcissa) != int or type(ordenada) != int or abcissa < 0 or ordenada < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'x': abcissa, 'y': ordenada}


def cria_copia_posicao(p):
    """cria_copia_posicao: posicao -> dict
    Devolve uma cópia da posição recebida."""
    return p.copy()


# seletores_posicao

def obter_pos_x(p):
    """obter_pos_x: posicao -> int
    Devolve a componente x da posição p recebida"""
    return p['x']


def obter_pos_y(p):
    """obter_pos_y: posicao -> int
    Devolve a componente y da posição p recebida"""
    return p['y']


# reconhecedor_posicao

def eh_posicao(arg):
    """eh_posicao: universal -> booleano
    Devolve True caso o seu argumento seja um TAD posicao e False caso não seja"""
    if type(arg) != dict or len(arg) != 2 or 'x' not in arg or 'y' not in arg or type(obter_pos_x(arg)) != int or \
            type(obter_pos_y(arg)) != int or obter_pos_x(arg) < 0 or obter_pos_y(arg) < 0:
        return False
    return True


# teste posicao

def posicoes_iguais(p1, p2):
    """posicoes_iguais: posicao x posicao -> booleano
    Devolve True apenas se p1 e p2 forem posições e forem iguais"""
    return True if eh_posicao(p1) and eh_posicao(p2) and p1 == p2 else False


# transformador_posicao

def posicao_para_str(p):
    """posicao_para_str: posicao -> str
    Devolve a cadeia de caracteres '(x, y)' que representa o seu argumento, sendo os valores
    x e y as coordenadas de p."""

    return str((obter_pos_x(p), obter_pos_y(p)))


# Funções de alto nível associadas ao TAD posicao

def obter_posicoes_adjacentes(p):
    """obter_posicoes_adjacentes: posicao -> tuplo
    Devolve um tuplo com as posições adjacentes à posição p, começando pela
    posição acima de p e seguindo no sentido horário"""
    if obter_pos_y(p) == 0 == obter_pos_x(p):
        pos_dir = cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p))
        pos_baix = cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
        return pos_dir, pos_baix
    if obter_pos_x(p) == 0 and obter_pos_y(p) != 0:
        pos_cim = cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1)
        pos_dir = cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p))
        pos_baix = cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
        return pos_cim, pos_dir, pos_baix
    if obter_pos_y(p) == 0 and obter_pos_x(p) != 0:
        pos_dir = cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p))
        pos_baix = cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
        pos_esq = cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p))
        return pos_dir, pos_baix, pos_esq
    else:
        pos_cim = cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1)
        pos_dir = cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p))
        pos_baix = cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
        pos_esq = cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p))
        return pos_cim, pos_dir, pos_baix, pos_esq


def ordenar_posicoes(t):
    """ordenar_posicoes: tuplo -> tuplo
    Devolve um tuplo contendo as mesmas posições do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado"""
    return tuple(sorted(sorted(t, key=lambda posicao: obter_pos_x(posicao)), key=lambda posicao: obter_pos_y(posicao)))
    #                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #                        ^^tuplo ordenado em função das abcissas^^


# TAD_2 -> animal

# construtores_animal

def cria_animal(s, r, a):
    """cria_animal: str x int x int -> animal
    Recebe uma cadeia de caracteres s não vazia correspodente à espécie do animal e dois valores
    inteiros correspondentes à frequência de reproduçãao r e à frequência de alimentação a.
    Após verificar a validade dos seus argumentos, devolve o animal. Animais com frequência de alimentação
    maior que 0 são considerados predadores, caso contrário são considerados presas."""
    if type(s) != str or type(r) != int or type(a) != int:
        raise ValueError('cria_animal: argumentos invalidos')
    if s == '' or r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    animal = {'espécie': s, 'reprodução': r, 'idade': 0}
    if a != 0:
        animal['fome'] = 0
        animal['alimentação'] = a
        return animal
    return animal


def cria_copia_animal(a):
    """cria_copia_animal: cria_copia_animal: animal -> animal
    Recebe um animal a (predador ou presa) e devolve uma
    nova cópia do animal."""
    return a.copy()


# seletores_animal

def obter_especie(a):
    """obter_especie: obter_especie: animal -> str
    Devolve a cadeia de caracteres correspondente à espécie do
    animal"""
    return a['espécie']


def obter_freq_reproducao(a):
    """obter_freq_reproducao: animal -> int
    Devolve a frequência de reprodução do animal a"""
    return a['reprodução']


def obter_freq_alimentacao(a):
    """obter_freq_alimentacao: animal -> int
    Devolve a frequência de alimentação do animal a (as presas devolvem sempre 0)."""
    if len(a) == 5:
        return a['alimentação']
    return 0


def obter_idade(a):
    """obter_idade: animal -> int
    Devolve a idade do animal a"""
    return a['idade']


def obter_fome(a):
    """obter_fome: animal -> int
    Devolve a fome do animal a (as presas devolvem sempre 0)"""
    if len(a) == 5:
        return a['fome']
    return 0


# modificadores_animal


def aumenta_idade(a):
    """aumenta_idade: animal -> animal
    Devolve o próprio animal depois de o modificar destrutivamente incrementando
    o valor da sua idade em uma unidade"""
    a['idade'] += 1
    return a


def reset_idade(a):
    """reset_idade: animal -> animal
    Devolve o próprio animal depois de o modificar destrutivamente zerando
    o valor da sua idade"""
    a['idade'] = 0
    return a


def aumenta_fome(a):
    """aumenta_fome: animal -> animal
    Devolve o próprio animal depois de o modificar destrutivamente incrementando
    o valor da sua fome em uma unidade"""
    if len(a) == 3:
        return a
    a['fome'] += 1
    return a


def reset_fome(a):
    """reset_fome: animal -> animal
    Devolve o próprio animal depois de o modificar destrutivamente zerando
    o valor da sua fome"""
    if len(a) == 3:
        return a
    a['fome'] = 0
    return a


# reconhecedores_animal

def eh_animal(arg):
    """eh_animal: universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal e
    False caso contrário"""
    if type(arg) != dict or (len(arg) != 3 and len(arg) != 5) or 'espécie' not in arg or 'reprodução' not in arg \
            or 'idade' not in arg:
        return False
    if len(arg) == 5 and ('fome' not in arg or 'alimentação' not in arg):
        return False
    if type(arg['espécie']) != str or type(arg['reprodução']) != int or type(arg['idade']) != int:
        return False
    if arg['espécie'] == '' or arg['reprodução'] <= 0:
        return False
    if len(arg) == 5 and (arg['fome'] < 0 or arg['alimentação'] <= 0):
        return False
    return True


def eh_predador(arg):
    """eh_predador: universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal do
    tipo predador e False caso contrário"""
    return True if eh_animal(arg) and obter_freq_alimentacao(arg) != 0 else False


def eh_presa(arg):
    """eh_presa: universal -> booleano
    Devolve True caso o seu argumento seja um TAD animal do
    tipo presa e False caso contrário."""
    return True if eh_animal(arg) and obter_freq_alimentacao(arg) == 0 else False


# teste_animal

def animais_iguais(a1, a2):
    """animais_iguais: animal x animal -> booleano
    Devolve True apenas se a1 e a2 são animais e são iguais"""
    return True if eh_animal(a1) and eh_animal(a2) and a1 == a2 else False


# transformadores_animal

def animal_para_char(a):
    """animal_para_char: animal -> str
    Devolve a cadeia de caracteres dum único elemento correspondente ao primeiro carácter
    da espécie do animal passada por argumento, em maiúscula para predadores e em minúscula para
    presas"""
    return obter_especie(a)[0].lower() if eh_presa(a) else obter_especie(a)[0].upper()


def animal_para_str(a):
    """animal_para_str: animal -> str
    Devolve a cadeia de caracteres que representa o animal"""
    return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ';' \
        + str(obter_fome(a)) + '/' + str(obter_freq_alimentacao(a)) + ']' if obter_freq_alimentacao(a) != 0 \
        else obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ']'


# Funções de alto nível associadas ao TAD animal


def eh_animal_fertil(a):
    """eh_animal_fertil: animal -> booleano
    devolve True caso o animal a tenha atingido a idade de reprodução e False caso contrário"""
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """eh_animal_faminto: animal -> booleano
    Devolve True caso o animal a tenha atingindo um valor de fome igual ou superior
    à sua frequência de alimentação e False caso contrário. As presas devolvem sempre False"""
    if eh_presa(a):
        return False
    return obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """reproduz_animal: animal -> animal
    Recebe um animal a devolvendo um novo animal da mesma
    espécie com idade e fome igual a 0, e modificando destrutivamente o animal passado
    como argumento a alterando a sua idade para 0."""
    reset_idade(a)
    return reset_fome(cria_copia_animal(a))


# TAD_3 -> prado

# construtores_prado

def cria_prado(d, r, a, p):
    """cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    Recebe uma posição d correspondente à posição que
    ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
    mais posições correspondentes aos rochedos que não são as montanhas dos
    limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da
    mesma dimensão do tuplo a com as posições correspondentes ocupadas pelos
    animais; e, após verificar a validade dos seus argumentos, devolve o prado que
    representa internamente o mapa e os animais presentes"""
    if not eh_posicao(d) or type(r) != tuple or type(a) != tuple or type(p) != tuple:
        raise ValueError('cria_prado: argumentos invalidos')
    if len(r) < 0 or len(a) < 1 or len(p) != len(a):
        raise ValueError('cria_prado: argumentos invalidos')
    for elemento in r:
        if not eh_posicao(elemento) or (obter_pos_x(elemento) <= 0 or obter_pos_x(elemento) >= obter_pos_x(d)) \
                or (obter_pos_y(elemento) <= 0 or obter_pos_y(elemento) >= obter_pos_y(d)):
            raise ValueError('cria_prado: argumentos invalidos')
    for elemento in a:
        if not eh_animal(elemento):
            raise ValueError('cria_prado: argumentos invalidos')
    for elemento in p:
        if not eh_posicao(elemento) or (obter_pos_x(elemento) <= 0 or obter_pos_x(elemento) >= obter_pos_x(d)) \
                or (obter_pos_y(elemento) <= 0 or obter_pos_y(elemento) >= obter_pos_y(d)):
            raise ValueError('cria_prado: argumentos invalidos')
    for rocha in r:
        for pos in p:
            if posicoes_iguais(rocha, pos):
                raise ValueError('cria_prado: argumentos invalidos')
    lista_animais_e_respetivas_posicoes = []
    contador = 0
    while contador < len(a):
        lista_animais_e_respetivas_posicoes += [[a[contador]] + [p[contador]]]
        contador += 1
    return {'dimensao_prado': d, 'rochedos_nao_limitantes': r,
            'animais_e_respetivas_posicoes': lista_animais_e_respetivas_posicoes}


def cria_copia_prado(m):
    """cria_copia_prado: prado -> prado
    Recebe um prado e devolve uma nova cópia do prado"""
    return m.copy()


# seletores_prado

def obter_tamanho_x(m):
    """obter_tamanho_x: prado -> int
    Devolve o valor inteiro que corresponde à dimensão Nx
    do prado"""
    return obter_pos_x(m['dimensao_prado']) + 1


def obter_tamanho_y(m):
    """obter_tamanho_y: prado -> int
    Devolve o valor inteiro que corresponde à dimensão Ny
    do prado"""
    return obter_pos_y(m['dimensao_prado']) + 1


def obter_numero_predadores(m):
    """obter_numero_predadores: prado -> int
    Devolve o número de animais predadores no prado"""
    n_predadores = 0
    for animal in m['animais_e_respetivas_posicoes']:
        if eh_predador(animal[0]):
            n_predadores += 1
    return n_predadores


def obter_numero_presas(m):
    """obter_numero_presas: prado -> int
    Devolve o número de animais presa no prado"""
    n_presas = 0
    for animal in m['animais_e_respetivas_posicoes']:
        if eh_presa(animal[0]):
            n_presas += 1
    return n_presas


def obter_posicao_animais(m):
    """obter_posicao_animais: prado -> tuplo posicoes
    Devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado"""
    tuplo_posicoes = ()
    for animal_e_posicao in m['animais_e_respetivas_posicoes']:
        tuplo_posicoes += (animal_e_posicao[1],)
    return ordenar_posicoes(tuplo_posicoes)


def obter_animal(m, p):
    """obter_animal: prado x posicao -> int
    Devolve o animal do prado que se encontra na posição p"""
    for animal_e_pos in m['animais_e_respetivas_posicoes']:
        if posicoes_iguais(p, animal_e_pos[1]):
            return animal_e_pos[0]


# modificadores_prado

def eliminar_animal(m, p):
    """eliminar_animal: prado x posicao -> prado
    Modifica destrutivamente o prado m eliminando o animal da posição p
    deixando-a livre. Devolve o próprio prado"""
    for animal_e_pos in range(len(m['animais_e_respetivas_posicoes'])):
        if posicoes_iguais(p, m['animais_e_respetivas_posicoes'][animal_e_pos][1]):
            m['animais_e_respetivas_posicoes'] = m['animais_e_respetivas_posicoes'][:animal_e_pos] + \
                                                  m['animais_e_respetivas_posicoes'][animal_e_pos + 1:]
            return m
    return m


def mover_animal(m, p1, p2):
    """mover_animal: prado x posicao x posicao -> prado
    modifica destrutivamente o prado m movimentando
    o animal da posição p1 para a nova posição p2, deixando livre a posi¸c˜ao onde
    se encontrava. Devolve o próprio prado."""
    for animal_e_pos in range(len(m['animais_e_respetivas_posicoes'])):
        if posicoes_iguais(p1, m['animais_e_respetivas_posicoes'][animal_e_pos][1]):
            m['animais_e_respetivas_posicoes'][animal_e_pos][1] = p2
            return m
    return m


def inserir_animal(m, a, p):
    """mover_animal: prado x animal x posicao -> prado
    modifica destrutivamente o prado m acrescentando na posição p do
    prado o animal a passado com argumento. Devolve o próprio prado"""
    m['animais_e_respetivas_posicoes'] += [[a, p]]
    return m


# reconhecedores_prado

def eh_prado(arg):
    """eh_prado: universal -> booleano
    Devolve True caso o seu argumento seja um TAD prado e False
    caso contrário."""
    if type(arg) != dict or len(arg) != 3 or 'dimensao_prado' not in arg or\
            'rochedos_nao_limitantes' not in arg or 'animais_e_respetivas_posicoes' not in arg:
        return False
    if not eh_posicao(arg['dimensao_prado']) or type(arg['rochedos_nao_limitantes']) != tuple or \
            type(arg['animais_e_respetivas_posicoes']) != list:
        return False
    if len(arg['rochedos_nao_limitantes']) < 0 or len(arg['animais_e_respetivas_posicoes']) < 1:
        return False
    for elemento in arg['rochedos_nao_limitantes']:
        if not eh_posicao(elemento) or (obter_pos_x(elemento) <= 0
                                        or obter_pos_x(elemento) >= obter_pos_x(arg['dimensao_prado'])) \
                or (obter_pos_y(elemento) <= 0 or obter_pos_y(elemento) >= obter_pos_y(arg['dimensao_prado'])):
            return False
    for elemento in arg['animais_e_respetivas_posicoes']:
        if type(elemento) != list or not eh_animal(elemento[0]) or not eh_posicao(elemento[1]):
            return False
        for rocha in arg['rochedos_nao_limitantes']:
            if posicoes_iguais(rocha, elemento[1]):
                return False
    for rocha in arg['rochedos_nao_limitantes']:
        for animal_e_pos in arg['animais_e_respetivas_posicoes']:
            if posicoes_iguais(rocha, animal_e_pos[1]):
                return False
    return True


def eh_posicao_animal(m, p):
    """eh_posicao_animal: prado x posicao -> booleano
    Devolve True apenas no caso da posição p do prado
    estar ocupada por um animal"""
    for pos_e_an in m['animais_e_respetivas_posicoes']:
        if posicoes_iguais(pos_e_an[1], p):
            return True
    return False


def eh_posicao_obstaculo(m, p):
    """eh_posicao_obstaculo: prado x posicao -> booleano
    Devolve True apenas no caso da posiçao p do prado
    corresponder a uma montanha ou rochedo"""
    if obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1 or \
            obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho_y(m) - 1:
        return True
    for pos_r in m['rochedos_nao_limitantes']:
        if posicoes_iguais(pos_r, p):
            return True
    return False


def eh_posicao_livre(m, p):
    """eh_posicao_livre: prado x posicao -> booleano
    Devolve True apenas no caso da posição p do prado
    corresponder a um espaço livre (sem animais, nem obstáculos)"""
    if not eh_posicao_obstaculo(m, p) and not eh_posicao_animal(m, p):
        return True
    return False


# reconhecedores_prado_extra

def eh_posicao_presa(m, p):
    """eh_posicao_presa: prado x posicao -> booleano
    Devolve True apenas no caso da posiçao p do prado
    estar ocupada por um animal do tipo presa"""
    if eh_posicao_animal(m, p) and eh_presa(obter_animal(m, p)):
        return True
    return False


def eh_posicao_predador(m, p):
    """eh_posicao_predador: prado x posicao -> booleano
    Devolve True apenas no caso da posiçao p do prado
    estar ocupada por um animal do tipo predador"""
    if eh_posicao_animal(m, p) and eh_predador(obter_animal(m, p)):
        return True
    return False


# teste_prado

def prados_iguais(p1, p2):
    """prados_iguais: prado x prado -> booleano
    Devolve True apenas se p1 e p2 forem prados e forem iguais"""
    if eh_prado(p1) and eh_prado(p1):
        return p1 == p2
    return False


# transformador_prado

def prado_para_str(m):
    """prado_para_str: prado -> str
    Devolve uma cadeia de caracteres que representa o prado"""
    y = 0
    str_prado = ''
    while y <= obter_tamanho_y(m) - 1:
        x = 0
        linha = ''
        while x <= obter_tamanho_x(m) - 1:
            if (x == 0 and y == 0) or (x == obter_tamanho_x(m) - 1 and y == 0) or \
                    (x == obter_tamanho_x(m) - 1 and y == obter_tamanho_y(m) - 1) or\
                    (x == 0 and y == obter_tamanho_y(m) - 1):
                linha += '+'
            elif x == 0 or x == obter_tamanho_x(m) - 1:
                linha += '|'
            elif y == 0 or y == obter_tamanho_y(m) - 1:
                linha += '-'
            elif eh_posicao_livre(m, cria_posicao(x, y)):
                linha += '.'
            elif eh_posicao_animal(m, cria_posicao(x, y)):
                linha += animal_para_char(obter_animal(m, cria_posicao(x, y)))
            elif eh_posicao_obstaculo(m, cria_posicao(x, y)):
                linha += '@'
            x += 1
        if y != obter_tamanho_y(m) - 1:
            str_prado += linha + '\n'
        else:
            str_prado += linha
        y += 1
    return str_prado


# Funções de alto nível associadas ao TAD prado

def obter_valor_numerico(m, p):
    """obter_valor_numerico: prado x posicao -> int
    Devolve o valor numérico da posição p correspondente
    à ordem de leitura no prado m"""
    return obter_pos_y(p) * (obter_tamanho_x(m)) + obter_pos_x(p)


def obter_movimento(m, p):
    """obter_movimento: prado x posicao -> posicao
    devolve a posi¸c˜ao seguinte do animal na posi¸c˜ao p dentro
    do prado m de acordo com as regras de movimento dos animais no prado"""
    destinos_viaveis = obter_posicoes_adjacentes(p)
    vn_posicao = obter_valor_numerico(m, p)
    if eh_posicao_presa(m, p):
        destino = 0
        while destino < len(destinos_viaveis):
            if not eh_posicao_livre(m, destinos_viaveis[destino]):
                destinos_viaveis = destinos_viaveis[:destino] + destinos_viaveis[destino + 1:]
                destino = -1
            destino += 1
        if destinos_viaveis == ():
            return p
        return destinos_viaveis[vn_posicao % len(destinos_viaveis)]
    numero_presas = 0
    destino = 0
    while destino < len(destinos_viaveis):
        if eh_posicao_presa(m, destinos_viaveis[destino]):
            numero_presas += 1
        if eh_posicao_obstaculo(m, destinos_viaveis[destino]) or \
                eh_posicao_predador(m, destinos_viaveis[destino]):
            destinos_viaveis = destinos_viaveis[:destino] + destinos_viaveis[destino + 1:]
            destino = -1
        destino += 1
    if numero_presas == 0:
        if destinos_viaveis == ():
            return p
        return destinos_viaveis[vn_posicao % len(destinos_viaveis)]
    destino = 0
    while destino < len(destinos_viaveis):
        if not eh_posicao_presa(m, destinos_viaveis[destino]):
            destinos_viaveis = destinos_viaveis[:destino] + destinos_viaveis[destino + 1:]
            destino = -1
        destino += 1
    if destinos_viaveis == ():
        return p
    return destinos_viaveis[vn_posicao % len(destinos_viaveis)]


# Funções adicionais

def geracao(m):  # na reproducao dois no mm sitio e dps ao mover move qual ? o primeiro ?
    """geracao: prado -> prado
    Função auxiliar que modifica o prado m fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio
    prado"""
    lista_usadas = []
    for pos in obter_posicao_animais(m):
        if eh_posicao_predador(m, pos):
            if not any(posicoes_iguais(pos_usada, pos) for pos_usada in lista_usadas):
                an = obter_animal(m, pos)
                aumenta_fome(aumenta_idade(an))
                pos_f = obter_movimento(m, pos)
                if not posicoes_iguais(pos, pos_f):
                    if eh_animal_fertil(an):
                        if eh_posicao_presa(m, pos_f):
                            lista_usadas += [pos_f]
                            eliminar_animal(m, pos_f)
                            reset_fome(an)
                            mover_animal(m, pos, pos_f)
                            inserir_animal(m, reproduz_animal(an), pos)
                        else:
                            mover_animal(m, pos, pos_f)
                            inserir_animal(m, reproduz_animal(an), pos)
                    else:
                        if eh_posicao_presa(m, pos_f):
                            lista_usadas += [pos_f]
                            eliminar_animal(m, pos_f)
                            reset_fome(an)
                        mover_animal(m, pos, pos_f)
        if eh_posicao_presa(m, pos):
            an = obter_animal(m, pos)
            aumenta_idade(an)
            pos_f = obter_movimento(m, pos)
            if not posicoes_iguais(pos, pos_f):
                if eh_animal_fertil(an):
                    mover_animal(m, pos, pos_f)
                    inserir_animal(m, reproduz_animal(an), pos)
                else:
                    mover_animal(m, pos, pos_f)
    for pos in obter_posicao_animais(m):
        if eh_animal_faminto(obter_animal(m, pos)):
            eliminar_animal(m, pos)
    return m


def simula_ecossistema(f, g, v):
    """simula_ecossistema: str x int x booleano -> tuplo
    Função principal que permite simular o ecossistema de um
    prado. A função recebe uma cadeia de caracteres f, um valor inteiro g e um valor booleano v e devolve o
    tuplo de dois elementos correspondentes ao número de predadores e
    presas no prado no fim da simulação. A cadeia de caracteres f passada por argumento
    corresponde ao nome do ficheiro de configuração da simulação. O valor inteiro g corresponde ao número de gerações
    a simular. O argumento booleano v ativa o modo verboso (True) ou o modo quiet (False).
    No modo quiet mostra-se pela saída standard o prado, o número de animais e o número de geração no início
    da simulação e após a última geração. No modo verboso, após cada geração, mostra-se também o prado, o número de
    animais e o número de geração, apenas se o número de animais predadores ou presas se tiver alterado."""
    fich_config = open(f, 'r')
    primeira_linha = eval(fich_config.readline().replace('\n', ''))
    d = cria_posicao(primeira_linha[0], primeira_linha[1])
    r = ()
    for tuplo in eval(fich_config.readline()):
        r += (cria_posicao(tuplo[0], tuplo[1]),)
    a = ()
    p = ()
    linha = fich_config.readline()
    while linha != '':
        linha = eval(linha)
        a += (cria_animal(linha[0], linha[1], linha[2]),)
        p += (cria_posicao(linha[3][0], linha[3][1]),)
        linha = fich_config.readline()
    pr = cria_prado(d, r, a, p)
    if v:
        for ger in range(g + 1):
            if ger == 0:
                print('Predadores: ' + str(obter_numero_predadores(pr)) + ' vs Presas: ' +
                      str(obter_numero_presas(pr)) + ' (Gen. ' + str(ger) + ')')
                print(prado_para_str(pr))
            else:
                n_pred_antes = obter_numero_predadores(pr)
                n_presas_antes = obter_numero_presas(pr)
                geracao(pr)
                n_pred_depois = obter_numero_predadores(pr)
                n_presas_depois = obter_numero_presas(pr)
                if n_presas_antes != n_presas_depois or n_pred_antes != n_pred_depois:
                    print('Predadores: ' + str(obter_numero_predadores(pr)) + ' vs Presas: ' +
                          str(obter_numero_presas(pr)) + ' (Gen. ' + str(ger) + ')')
                    print(prado_para_str(pr))
    else:
        for ger in range(g + 1):
            if ger == 0:
                print('Predadores: ' + str(obter_numero_predadores(pr)) + ' vs Presas: ' +
                      str(obter_numero_presas(pr)) + ' (Gen. ' + str(ger) + ')')
                print(prado_para_str(pr))
            elif ger != g:
                geracao(pr)
            else:
                geracao(pr)
                print('Predadores: ' + str(obter_numero_predadores(pr)) + ' vs Presas: ' +
                      str(obter_numero_presas(pr)) + ' (Gen. ' + str(ger) + ')')
                print(prado_para_str(pr))
    fich_config.close()
    return obter_numero_predadores(pr), obter_numero_presas(pr)
