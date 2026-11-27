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

| Membro | Responsabilidade | Tarefas concretas neste projecto |
|---|---|---|
| Rodolf | Product Owner e Developer | Define o Objectivo do Produto; escreve e ordena as issues e os critérios de aceitação; representa o coordenador de turno quando não há retorno (e fica escrito no `sprint-N.md`); decide o que se demonstra na revisão |
| Dalton | Scrum Master e Developer | Garante que o Scrum é compreendido e aplicado; facilita os eventos; vigia os limites de WIP; calcula as medidas de fluxo; cria a etiqueta `sprint-N`; ajuda a remover impedimentos |
| Ambos | Developers | Planeiam a Lista da Sprint, constroem o Incremento cumprindo a Definição de Pronto, revêem o código um do outro e adaptam o plano diariamente |

**Responsabilidades e não papéis.** O Scrum Guide 2020 usa o termo *accountabilities* (responsabilidades) em vez de papéis. Um papel sugere um cargo numa hierarquia, enquanto uma responsabilidade indica por que resultado cada pessoa responde. Numa equipa de duas pessoas, isto permite acumular: os dois são Developers e cada um responde também por uma outra parte, sem que um seja chefe do outro. Foi o que vivemos na Sprint 1: quando o computador do Dalton falhou, o Rodolf assumiu temporariamente issues dele, porque a responsabilidade de entregar o Incremento é da equipa e não de uma pessoa.

*Fonte: Schwaber e Sutherland, The Scrum Guide, 2020, secção «The Scrum Team», scrumguides.org.*

## Eventos

| Evento | Propósito | Participantes | Máximo no Guia (sprint de 1 mês) | Duração escolhida | O que sai do evento |
|---|---|---|---|---|---|
| Sprint | Contentor dos outros eventos; produz um Incremento | Equipa | 1 mês | 4 dias reais (a Sprint 1 ficou com 3 no quadro, por causa do atraso) | Incremento marcado com `sprint-N` |
| Planeamento | Definir porquê, o quê e como | Rodolf e Dalton | 8 h | 45 min, no 1.º dia | Sprint Goal e issues escolhidas no `sprint-N.md` |
| Daily | Inspeccionar o progresso e adaptar o plano | Rodolf e Dalton | 15 min | Escrita, até 10 min, 3 linhas por membro | Entrada diária no `sprint-N.md` |
| Revisão | Inspeccionar o Incremento com o coordenador | Equipa e coordenador (por demonstração) | 4 h | 30 min, no último dia | Demonstração, retorno e Lista do Produto ajustada |
| Retrospectiva | Melhorar o processo | Rodolf e Dalton | 3 h | 20 min, a seguir à revisão | Melhorias e secção «Desafio a vigiar» actualizada |

**Justificação.** Uma sprint de 4 dias corresponde a cerca de um quinto de um mês, o que daria 1h36 de planeamento, 48 min de revisão e 36 min de retrospectiva. Como somos duas pessoas com contacto diário, reduzimos ainda mais. A daily é escrita porque os dois conhecemos o trabalho um do outro e cada um regista o seu bloco no próprio dia. A revisão e a retrospectiva fazem-se na mesma sessão, mas com propósitos separados: a revisão olha para o produto e a retrospectiva olha para a forma de trabalhar. Na Sprint 1 o planeamento fez-se no 2.º dia por causa do atraso de arranque, e isso ficou registado.

*Fonte: Schwaber e Sutherland, The Scrum Guide, 2020, secção «Scrum Events», scrumguides.org.*

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

| Ferramenta | Porquê | Quem usa | Evidência |
|---|---|---|---|
| pytest | Testes automáticos | Rodolf e Dalton | `tests/`; execução no CI |
| ruff | Verificação de estilo e erros simples | Rodolf e Dalton | CI (`ruff check .`) |
| GitHub Actions | Executar ruff e pytest em cada PR | Rodolf e Dalton | Separador Actions; PR #57 |
| Tailwind CSS (CLI) | Compilar o CSS responsivo | Rodolf e Dalton | `app/static/css/app.css` |

## Regras de uso da IA

(Actividade 8 — Sprint 2. Ver também [docs/ia.md](docs/ia.md).)

## Desafio a vigiar

**Desafio actual (provisório, Sprint 1):** familiaridade com as ferramentas (GitHub Projects, Pull Requests, protecção da `main`) e dependência de um único computador/pessoa num item crítico.

**O que aconteceu:** 
1. Começámos a configuração do quadro às 23h de 24/11, o que atrasou o arranque da Sprint 1 em um dia.
2. Na reta final da sprint, o computador do Dalton avariou, bloqueando a entrega do esqueleto FastAPI (#9), que era o caminho crítico para a base de dados (#10) e para o login (#11).
3. O CI falhou no PR #57 porque o README foi apagado por engano durante uma edição cruzada da branch do colega.

**O que vamos fazer (Acções para a Sprint 2):** 
- Ensaiar o fluxo completo (ramo, commit, push, PR, revisão, merge) no primeiro dia da sprint.
- Consultar primeiro a documentação oficial (GitHub Docs) quando surgir um bloqueio.
- **Mitigação do hardware:** Se o PC de um membro falhar, esse membro usará o editor web do GitHub para fazer alterações simples (ex: documentação) e o colega assumirá temporariamente os PRs de código, registando a alteração de responsabilidade no `sprint-N.md`.
- **Regra de revisão:** Nunca editar a branch de outra pessoa. Se houver um erro, usar o botão "Request changes" no PR com um comentário a explicar o que deve ser corrigido.

*(Esta secção é revista em todas as retrospectivas. O desafio da Actividade 6, retirado do estudo de Ahmad, Markkula e Oivo (2013), será acrescentado na Sprint 2.)*