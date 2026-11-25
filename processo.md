# Processo da equipa: Caderneta Digital

Acordo de trabalho do grupo. Cada secção corresponde a uma actividade da Parte I do Lab #02.

## Valores do grupo

Estes são os quatro valores do Manifesto Ágil e o que o nosso grupo decide fazer, na Caderneta Digital, quando a esquerda e a direita entram em conflito.

| Valor do Manifesto | Decisão concreta do grupo | O que continua a ter valor (lado direito) |
|---|---|---|
| Indivíduos e interacções mais do que processos e ferramentas | Quando um de nós fica bloqueado ou não tem a certeza do que fazer ou de como o fazer, avisa o colega por WhatsApp ou chamada em vez de esperar pela daily escrita, e o que ficar decidido é registado na issue ou no PR. Cada PR é revisto pelo colega, para que os dois percebam o que foi feito. Só adoptamos uma ferramenta nova se os dois a usarmos e ficar escrita em «Ferramentas». | Os processos e as ferramentas dão-nos estrutura: a Definição de Pronto, os limites de WIP, o GitHub Projects e a revisão obrigatória nos PRs (a `main` está protegida). |
| Software em funcionamento mais do que documentação abrangente | No fim de cada sprint existe um Incremento que cumpre a Definição de Pronto, corre localmente, é demonstrado na revisão e fica marcado com a etiqueta `sprint-N`; um item que não cumpre a Definição de Pronto volta ao Product Backlog. Os documentos são curtos e actualizados quando o software muda. | Os documentos exigidos continuam a ter valor: requisitos, casos de uso, modelo de dados, README e relatório de testes explicam o que o software faz e como executá-lo. |
| Colaboração com o cliente mais do que negociação de contratos | No fim de cada sprint enviamos ao coordenador de turno uma demonstração de 1 a 2 minutos no grupo de WhatsApp e registamos o retorno no `sprint-N.md`; as dúvidas vão com captura de ecrã e contexto. Se não houver retorno, o Product Owner representa o coordenador e fica escrito. | O enunciado e o produto mínimo (os cinco módulos) continuam a definir o âmbito que temos de entregar. |
| Responder a mudanças mais do que seguir um plano | Quando um atraso, um bloqueio ou o retorno do coordenador mostra que o plano deixou de servir, o Product Owner reordena o Product Backlog e a equipa ajusta o que cabe na sprint no próprio dia, e fica registado no `sprint-N.md`. O Sprint Goal mantém-se durante a sprint; o que se renegoceia é o âmbito. Foi o que fizemos na Sprint 1: com um dia de atraso, mantivemos as datas e passámos três itens para a Sprint 2. | O plano continua a orientar-nos: o Sprint Goal, o roadmap das cinco sprints e o prazo de entrega de 13/12. |

**Porque «mais do que» não significa «em vez de».** O Manifesto afirma que há valor nos itens da direita, mas que valoriza mais os da esquerda; não manda eliminá-los. Ler «em vez de» levar-nos-ia a não escrever documentação nenhuma. No nosso projecto, valorizar mais o software em funcionamento do que a documentação abrangente não nos dispensa dos requisitos, dos casos de uso, do modelo de dados e do README, que o enunciado exige e que explicam o que o software faz. Significa que, quando o tempo apertou na Sprint 1, passámos para a Sprint 2 o diagrama de casos de uso e as histórias dos módulos 3 a 5, e mantivemos no plano o esqueleto da aplicação e o login. Assim, a documentação acompanha o software em vez de o preceder.

*Fonte: Beck et al., Manifesto for Agile Software Development, 2001, agilemanifesto.org.*

## Equipa

(Actividade 2 — Sprint 1)

## Eventos

(Actividade 3 — Sprint 1)

## Objectivo do Produto e Definição de Pronto

**Objectivo do Produto (Product Goal):**
Centralizar a gestão do coordenador de turno numa única aplicação web, eliminando a dispersão por cadernos e folhas de cálculo. A aplicação deve permitir registar ocorrências disciplinares complexas (com múltiplos alunos e testemunhas), acompanhar as medidas aplicadas e consultar o histórico dos alunos de forma rápida, segura e acessível.

**Objectivo da Sprint 1 (Sprint Goal):**
Estabelecer a fundação do projecto: configurar o repositório, o quadro Kanban e o processo Scrum, tomar as decisões técnicas estruturantes (ADR) e preparar o esqueleto da aplicação, garantindo que a equipa domina o fluxo de trabalho (issues, ramos, PRs e reviews).

**Definição de Pronto (Definition of Done - DoD):**
Um item do Sprint Backlog só é considerado "Pronto" (e conta como Incremento) quando:
1. O código está implementado e a aplicação corre localmente sem erros.
2. Cumpre todos os critérios de aceitação definidos na respectiva Issue.
3. O código foi revisto e aprovado por pelo menos um colega (Pull Request com merge).
4. Passa nos testes (quando aplicável) e não quebra funcionalidades anteriores.
5. Os dados de teste usados são fictícios (em conformidade com a Lei n.º 22/11).
6. A documentação associada (README, `processo.md` ou ficheiros da sprint) foi actualizada.

**Porque cada artefacto tem um compromisso associado? (Baseado no Scrum Guide 2020)**
O Scrum Guide estabelece que cada artefacto contém um compromisso que lhe dá foco e valor:
* O **Product Backlog** compromete-se com o **Product Goal** (a visão de longo prazo), garantindo que a equipa não se perde em tarefas aleatórias.
* O **Sprint Backlog** compromete-se com o **Sprint Goal** (o objectivo de curto prazo), dando flexibilidade à equipa para ajustar as tarefas diárias desde que o objectivo da sprint seja cumprido.
* O **Incremento** compromete-se com a **Definição de Pronto (DoD)**, garantindo a qualidade e que o software está realmente utilizável.

**O que acontece se um item não cumprir a DoD no fim da sprint?**
Se um item não cumprir a DoD, **não é apresentado na Sprint Review** como parte do Incremento. Em vez disso, o item regressa ao **Product Backlog** para ser reavaliado pelo Product Owner e re-priorizado numa sprint futura. O trabalho não é desperdiçado, mas reconhece-se formalmente que a funcionalidade ainda não está concluída.

## Regras do quadro

(Actividade 5 — Sprint 2)

## Como combinamos o Scrum e o Kanban

(Actividade 7 — Sprint 2)

## Ferramentas

(Actividade 7 — Sprint 2. Cada ferramenta adicional: porquê, quem usa, evidência de uso.)

## Regras de uso da IA

(Actividade 8 — Sprint 2. Ver também [docs/ia.md](docs/ia.md).)

## Desafio a vigiar

**Desafio actual (provisório, Sprint 1):** familiaridade com as ferramentas (GitHub Projects,
Pull Requests, protecção da `main`) e início tardio de tarefas de configuração.

**O que aconteceu:** começámos a configuração às 23h de 24/11 e só a concluímos a 25/11,
o que atrasou o arranque da Sprint 1 em um dia.

**O que vamos fazer:** ensaiar o fluxo completo (ramo, commit, push, PR, revisão, merge) antes de
trabalhar a sério; no primeiro dia de cada sprint, verificar em 10 minutos que os dois
conseguem fazer `git push`, abrir o quadro e abrir um PR; consultar primeiro a documentação oficial
(GitHub Docs) quando surgir um bloqueio.

(Esta secção é revista em todas as retrospectivas. O desafio da Actividade 6, retirado do estudo
de Ahmad, Markkula e Oivo (2013), será acrescentado na Sprint 2.)

## Kanban, WIP e métricas

(Regras do quadro, limites de WIP e definições das medidas de fluxo. Sprint 2.)