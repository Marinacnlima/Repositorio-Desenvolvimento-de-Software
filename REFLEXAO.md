# Reflexão — Portfólio Git

## O que foi difícil

A parte mais complicada para mim foi entender o estado do repositório durante um merge conflict.
Quando o Git pausa o merge e mostra aquelas marcações `<<<<<<<`, `=======` e `>>>>>>>` no arquivo,
minha primeira reação foi de pânico. Eu não sabia exatamente o que tinha acontecido com o
histórico naquele momento — se o merge tinha sido feito pela metade, se eu podia desfazer,
o que `HEAD` significava ali.

Tentei algumas vezes resolver o conflito mas acabei com o arquivo num estado inconsistente
porque não entendi que precisava remover as marcações manualmente e depois dar `git add` para
sinalizar que a resolução estava completa. Rodei `git merge --abort` e comecei de novo até
entender o fluxo correto.

Outra dificuldade foi nomear os commits de forma descritiva sem ser genérico. No início, minha
tendência era escrever coisas como "atualiza arquivo" ou "pequenos ajustes", que não comunicam
absolutamente nada. Forçar-me a pensar no *tipo* e no *escopo* antes de commitar me obrigou a
ter clareza sobre o que eu estava mudando — e às vezes isso me fez perceber que estava tentando
agrupar coisas demais num único commit.

## O que ficou claro

Entendi de verdade que branches são baratas e descartáveis. Antes, eu achava que criar uma branch
era algo pesado, que você fazia para grandes funcionalidades. Mas ao longo deste exercício ficou
claro que qualquer trabalho paralelo merece sua própria branch — seja uma correção pequena, seja
uma atualização de documentação.

O conceito que mais "clicou" foi o de que a `main` deve refletir sempre um estado estável e
funcional. As branches existem para proteger isso. Quando você trabalha em uma branch e algo dá
errado, é só deletar. A `main` continua intacta. Isso mudou completamente a forma como penso no
fluxo de trabalho.

Também ficou claro por que os Pull Requests existem mesmo em repositórios individuais. Abrir
um PR me forçou a escrever uma descrição do que fiz — e isso me fez perceber algumas inconsistências
no meu trabalho que eu não teria notado se tivesse feito o merge direto pela linha de comando.
É uma etapa de revisão, mesmo que você seja o único autor.

## O que ainda é confuso

Ainda não entendo completamente o `git rebase` e quando ele é mais adequado que o `git merge`.
Sei que o rebase reescreve o histórico de uma forma mais linear, mas não sei como isso interage
com repositórios remotos já publicados — ouvi falar que fazer rebase em branches compartilhadas
é problemático, mas não sei exatamente por quê nem como detectar quando estou numa situação de
risco.

Também fiz funcionar o cherry-pick uma vez durante um teste, mas não sei ao certo em que cenários
reais ele seria preferível a um merge normal. E o comando `git reflog` — eu o usei para recuperar
um commit que achei que tinha perdido, mas não entendo bem como ele funciona internamente nem
por quanto tempo os dados ficam disponíveis lá.

Essas são as dúvidas que pretendo resolver nas próximas semanas conforme o trabalho em equipe
exigir decisões sobre estratégia de branches e histórico.
