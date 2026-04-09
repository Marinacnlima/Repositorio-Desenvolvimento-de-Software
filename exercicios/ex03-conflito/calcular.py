def calcular_media(valores):
    if not valores:
        raise ValueError("Lista de valores não pode ser vazia")
    return sum(valores) / len(valores)


def classificar(media):
    if media >= 7.0:
        return "Aprovado"
    if media >= 4.0:
        return "Recuperação"
    return "Reprovado"
