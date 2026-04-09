# Exercício 03 — Registro de Resolução de Conflito

## O que causou o conflito

**Arquivo afetado:** `exercicios/ex03-conflito/calcular.py`

Duas branches foram criadas a partir do mesmo commit na `main` e ambas adicionaram
o mesmo arquivo `calcular.py` com implementações diferentes:

- **`feat/versao-a`**: a função `calcular_media` retornava `0` para listas vazias,
  e `classificar` usava apenas o limiar de `7.0` para aprovação.

- **`feat/versao-b`**: `calcular_media` lançava `ValueError` para listas vazias,
  e `classificar` incluía uma faixa de recuperação (`>= 4.0`) além da aprovação.

Quando `feat/versao-a` foi mergeada primeiro e, em seguida, tentou-se mergear
`feat/versao-b`, o Git detectou conflitos em dois trechos do mesmo arquivo:
no bloco `if not valores` e em toda a função `classificar`.

## Como decidi qual versão manter

Para o conflito em `calcular_media`: escolhi o comportamento da versão B
(`raise ValueError`) porque retornar `0` silenciosamente para uma lista vazia
é enganoso — a média de uma lista vazia é indefinida, não zero.

Para o conflito em `classificar`: mantive o limiar de `7.0` da versão A para
aprovação (mais conservador) e incorporei a faixa de recuperação `>= 4.0` da
versão B, já que ela adiciona granularidade ao resultado sem remover informação.

## Como marquei o conflito como resolvido

1. Editei manualmente o arquivo, removendo as marcações `<<<<<<<`, `=======`
   e `>>>>>>>` e deixando apenas o código final desejado.
2. Rodei `git add exercicios/ex03-conflito/calcular.py` para marcar o arquivo
   como resolvido.
3. Completei o merge com `git commit -m "fix(ex03): resolve conflito de merge entre versao-a e versao-b"`.

O Git não finaliza o merge automaticamente após a resolução — é necessário fazer
o `git add` nos arquivos conflitantes e depois o `git commit` explicitamente.
