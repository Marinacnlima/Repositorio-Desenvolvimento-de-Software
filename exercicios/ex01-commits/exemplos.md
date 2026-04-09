# Exercício 01 — Commits Semânticos

## O que são commits semânticos?

Commits semânticos seguem o padrão **Conventional Commits**, onde cada mensagem tem a forma:

```
<tipo>(<escopo opcional>): <descrição curta>
```

## Tipos mais comuns

| Tipo       | Quando usar                                      |
|------------|--------------------------------------------------|
| `feat`     | Nova funcionalidade ou arquivo                   |
| `fix`      | Correção de um bug                               |
| `docs`     | Alteração em documentação                        |
| `refactor` | Melhoria de código sem mudança de comportamento  |
| `test`     | Adição ou modificação de testes                  |
| `chore`    | Configuração, dependências, gitignore, etc.      |

## Exemplos reais deste repositório

```
feat(hello-world): adiciona função de saudação personalizada
fix(hello-world): corrige validação de nome vazio
docs(readme): descreve estrutura e objetivos do repositório
refactor(hello-world): extrai lógica de validação para função separada
chore(repo): configura estrutura inicial do portfólio
```

## Por que isso importa?

Um histórico de commits legível serve como documentação viva do projeto.
Quando alguém (ou você mesmo, seis meses depois) precisar entender o que mudou
e por quê, os commits semânticos respondem essa pergunta sem precisar abrir cada diff.
