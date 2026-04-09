# Exercício 02 — Branches

## O que é uma branch?

Uma branch é uma linha de desenvolvimento independente. Ela permite que você trabalhe
em uma funcionalidade, correção ou experimento sem afetar o código estável na `main`.

## Fluxo típico

```bash
# criar e mudar para nova branch
git checkout -b feat/nova-funcionalidade

# trabalhar, commitar...
git add .
git commit -m "feat(escopo): adiciona nova funcionalidade"

# trazer de volta para a main via Pull Request
```

## Boas práticas de nomenclatura

Use o padrão `tipo/descricao-curta`:

- `feat/rota-usuarios`
- `fix/validacao-email`
- `docs/atualiza-readme`
- `refactor/extrai-service`

## Branches usadas neste repositório

| Branch                    | Propósito                                      |
|---------------------------|------------------------------------------------|
| `feat/hello-world`        | Mini-projeto principal                         |
| `docs/atualiza-readme`    | Documentação e reflexão                        |
| `feat/exercicios`         | Conteúdo dos exercícios ex01 e ex02            |
| `feat/versao-a`           | Primeira versão para criar conflito            |
| `feat/versao-b`           | Segunda versão para demonstrar conflito        |

## Por que usar branches?

Branches permitem desenvolvimento paralelo sem interferência. Se algo der errado
em uma branch, a `main` continua estável. Essa é a base do trabalho colaborativo
em equipes — cada pessoa trabalha em sua branch e abre um PR para revisão.
