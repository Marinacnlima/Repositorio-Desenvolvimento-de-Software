def validar_nome(nome):
    if not nome or not nome.strip():
        raise ValueError("Nome não pode ser vazio")
    return nome.strip()


def saudar(nome):
    nome_valido = validar_nome(nome)
    return f"Olá, {nome_valido}! Bem-vindo ao hello-world."


def despedir(nome):
    nome_valido = validar_nome(nome)
    return f"Até logo, {nome_valido}! Foi um prazer."


def cumprimentar_lista(nomes):
    return [saudar(n) for n in nomes]


def main():
    nomes = ["Mundo", "Marina", "Git"]
    for msg in cumprimentar_lista(nomes):
        print(msg)


if __name__ == "__main__":
    main()
