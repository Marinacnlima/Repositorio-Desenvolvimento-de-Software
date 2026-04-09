def calcular_media(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)


def classificar(media):
    if media >= 7.0:
        return "Aprovado"
    return "Reprovado"
