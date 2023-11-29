def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios aluno.
    :param n : uma ou mais notas dos alunos(aceita varias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "BOA"
        elif r['média'] >= 5:
            r['situação'] = "RAZOAVEL"
        else:
            r['situação'] = "RUIM"
    return r


resp = notas(5.5, 2.3, 1.5, sit=True)
print(resp)