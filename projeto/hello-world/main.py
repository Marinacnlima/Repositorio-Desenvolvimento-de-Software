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


def main():
    print(saudar("Mundo"))
    print(despedir("Mundo"))


if __name__ == "__main__":
    main()
