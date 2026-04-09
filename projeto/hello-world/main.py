def saudar(nome):
    if not nome or not nome.strip():
        raise ValueError("Nome não pode ser vazio")
    return f"Olá, {nome.strip()}! Bem-vindo ao hello-world."


def main():
    print(saudar("Mundo"))


if __name__ == "__main__":
    main()
