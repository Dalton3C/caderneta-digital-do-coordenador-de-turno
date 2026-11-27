# Sprint 1 (24–27 Nov 2026; semanas simuladas 1–2)

> **Nota sobre o atraso.** Só começámos a configuração do repositório e do quadro (GitHub Projects)
> às 23h de 24/11 e, por falta de familiaridade com o GitHub Projects e com as restrições
> de protecção da branch `main` (Pull Request e revisão obrigatórios), demorámos mais do que
> o previsto e só terminámos a 25/11. No Dia 1 ficaram feitas a configuração do Git, as leituras
> e o modelo inicial dos ficheiros do repositório, mas não houve trabalho de produto entregue
> nem o quadro ficou operacional. O planeamento foi feito a 25/11 (Dia 2), não a 24/11.
>
> **Nota sobre o quadro.** O GitHub Projects só permite iterações a partir da data actual,
> por isso a iteração «Sprint 1» aparece no quadro a 25–27 Nov. O calendário do enunciado
> mantém-se (Sprint 1: 24–27 Nov) e a etiqueta `sprint-1` será criada a 27/11.

> **Nota sobre a entrega do #9.** O esqueleto da aplicação (#9), previsto para 26/11, foi entregue a 27/11
> por avaria do computador do Dalton. Isso atrasou o #10 e o #11, que dependem dele.

## Sprint Goal

Ter o repositório, o quadro e o acordo de processo (`processo.md`) operacionais, os requisitos
iniciais e o modelo de dados definidos, e uma aplicação FastAPI a correr localmente com login
funcional ligado à base de dados escolhida.

## Planeamento (feito a 25/11/2026)

**Participantes:** Rodolf (Product Owner) e Dalton (Scrum Master). Ambos Developers.
**Duração:** 45 min.
**Capacidade:** 2 pessoas × 3 dias × 6 h = 36 h. Compromisso: ≈ 29 h (80 %), com folga para imprevistos.
**Limites de WIP:** «In progress» ≤ 3 no total (máx. 2 por pessoa); «In review» ≤ 2.
**Estado inicial no quadro:** todas as issues desta sprint em «Ready».

### Issues escolhidas (por ordem de prioridade)

| Ordem | Issue | Título | Responsável | Estim. (h) |
|:-:|:-:|---|---|:-:|
| 1 | #8 | docs: Decisões técnicas (ADR-001 a 003) e registo de IA | Rodolf | 2 |
| 2 | #9 | chore: Esqueleto FastAPI + Jinja2 + Tailwind + CI | Dalton | 4 |
| 3 | #10 | feat: Ligação à BD, modelo Utilizador e migração | Rodolf | 4 |
| 4 | #11 | feat: Login e logout com bcrypt e sessão | Dalton | 4 |
| 5 | #5 | docs: Actores, perfis, requisitos funcionais e não funcionais | Rodolf | 4 |
| 6 | #6 | docs: Histórias de utilizador dos módulos 1 e 2 | Rodolf | 2 |
| 7 | #7 | docs: Modelo de dados v1 | Dalton | 3 |
| 8 | #1 | docs: processo.md — Valores do grupo (Act. 1) | Rodolf | 1,5 |
| 9 | #2 | docs: processo.md — Equipa (Act. 2) | Dalton | 1,5 |
| 10 | #3 | docs: processo.md — Eventos adaptados (Act. 3) | Dalton | 2 |
| 11 | #4 | docs: processo.md — Objectivo do Produto, Sprint 1 e DoD (Act. 4) | Rodolf | 2 |

**Total estimado:** 30 h (Rodolf 15,5 h; Dalton 14,5 h).

### Itens que passam para a Sprint 2 por causa do atraso

- #12 docs: processo.md — Regras do quadro e WIP (Act. 5)
- #13 docs: Histórias dos módulos 3 a 5 e ordem do backlog justificada
- #14 docs: Diagrama de casos de uso

**Se a capacidade não chegar, caem primeiro** as histórias dos módulos 1 e 2 e, a seguir,
o registo das decisões técnicas, que passam para a Sprint 2.

## Daily

### Dia 1 (24/11) — registado a 25/11
- **Rodolf:** Fiz — leituras dos guias (Manifesto Ágil, Scrum Guide, Kanban Guide e GitHub Docs) com notas guardadas; criação do modelo inicial dos ficheiros do repositório (`README.md`, `processo.md`, `docs/ia.md` e `sprints/sprint-1..5.md`), sem os finalizar; início da configuração do quadro às 23h. Vou fazer — tornar o quadro público e dar acesso ao `judsonp`; configurar as 5 iterações, as vistas e as automações; criar as labels e as issues da Sprint 1 com responsável e estimativa; planear a sprint. Impedimentos — pouca familiaridade com o GitHub Projects e com a protecção da `main`; a configuração do quadro começou às 23h e não ficou concluída, e as tarefas planeadas passaram para o Dia 2.
- **Dalton:** Fiz — configuração do Git; leituras dos guias. Vou fazer — (o plano dele para o Dia 1). Impedimentos — pouca familiaridade com a protecção da `main`.

### Dia 2 (25/11)
- **Rodolf:** Fiz — configuração do quadro (acesso público, convite ao `judsonp`, campo de iteração com as 5 sprints, vistas, estados e automações); criação das labels e das 46 issues do Product Backlog (11 da Sprint 1 com critérios de aceitação, responsável e estimativa; as restantes atribuídas às Sprints 2 a 5, por refinar); planeamento da sprint; link do quadro no `README.md` e capturas do quadro em `docs/evidencias/sprint-1/`. Vou fazer — a secção «Valores do grupo» do `processo.md` (#1) e, a seguir, as decisões técnicas (#8). Impedimentos — nenhum de momento.
- **Dalton:** (por registar)

### Dia 3 (26/11)
*(Nota: Registo elaborado a 27/11 devido aos impedimentos)*
- **Rodolf:** Fiz — o ADR-001 a 003, Objectivo do Produto e DoD, Actores/perfis/RF/RNF. Vou fazer — o #10 assim que o #9 estiver fundido. Impedimentos — o #9 não ficou pronto, por isso o #10 não pôde começar.
- **Dalton:** Fiz — Tentativa de conclusão do esqueleto FastAPI. Vou fazer — Abrir o PR #57. Impedimentos — Avaria no computador pessoal, impossibilitando o progresso no código.

### Dia 4 (27/11)
- **Rodolf:** Fiz — Corrigi o CI do PR #57 (pythonpath e README apagado), atualizei a documentação técnica do README e iniciei o modelo de BD (#10). Vou fazer — Fechar a documentação técnica e apoiar nas cerimónias de fim de sprint. Impedimentos — O CI estava vermelho e o README foi apagado por engano, mas já resolvido.
- **Dalton:** Fiz — Recuperei o ambiente de trabalho, abri o PR #57 e fiz a revisão do PR #10 no browser. Vou fazer — Redigir as secções Equipa (#2) e Eventos (#3) no browser e aprovar o PR do CI. Impedimentos — Nenhum (computador recuperado).

## Alterações ao plano durante a sprint (registadas a 27/11)

| Issue | Plano original | O que aconteceu | Motivo |
|---|---|---|---|
| #9 | Dalton, 26/11 | Entregue a 27/11 | Avaria do computador do Dalton |
| #11 | Dalton | Reatribuída a Rodolf | Dependência do #9 e avaria do computador |
| #2, #3 | Dalton | [Dalton no browser / Rodolf com revisão do Dalton] | [..] |
| #7 | Dalton | Passa para a Sprint 2 | Sem capacidade |

## Revisão (27/11)

- **O que foi demonstrado:** A aplicação FastAPI a arrancar localmente (rota `/health` a devolver `{"status":"ok"}`), a ligação à base de dados SQLite funcional, o modelo de dados (com a tabela de utilizadores e os 3 perfis), o quadro Kanban operacional (com iterações e labels) e o fluxo de CI a bloquear erros.
- **Demonstração enviada ao coordenador de turno (data e canal):** 27/11/2026, via WhatsApp (vídeo de 1 minuto a mostrar a app a arrancar e o quadro).
- **Retorno recebido:** Sem retorno do coordenador até ao fecho da sprint. O Product Owner (Rodolf) representou o coordenador, validando que o esqueleto e a base de dados eram o alicerce correto para os próximos módulos, e ajustou o backlog.
- **Itens que não cumpriram a Definição de Pronto (voltam ao Product Backlog):** 
  - #7 (Modelo de dados v1): Movido para a Sprint 2 por falta de capacidade (a equipa focou-se em desbloquear o código).
  - #11 (Login): A dependência do #9 (esqueleto) atrasou o arranque, pelo que o login passa para a Sprint 2.

## Retrospectiva (27/11)

- **O que correu bem:** O quadro público e organizado; o planeamento e as dailies registados via PR; o CI apanhou um erro crítico (README apagado e falha no pytest) antes de chegar à `main`; a capacidade de replaneamento do Scrum perante a avaria de hardware.
- **O que melhorar:** Dependência de um só computador; um PR foi aprovado com o CI vermelho; edição directa da branch do autor (o que criou o bug do README); dailies registadas com um dia de atraso.
- **Acção para a Sprint 2:** Correr `pytest` e `ruff` num clone limpo antes de abrir cada PR; usar a opção "Request changes" no GitHub em vez de editar a branch do colega; só aprovar PRs com o CI verde; o Dalton passa a usar o editor web do GitHub quando o PC falhar; registar a daily no próprio dia.
- **«Desafio a vigiar» actualizado no `processo.md`:** Sim.

## Métricas de fluxo

| Medida | Valor |
|---|---|
| Trabalho em curso (WIP), máximo atingido | 3 itens (limite máximo estipulado pela equipa) |
| Débito (throughput): itens concluídos na sprint | 9 itens |
| Idade do item mais antigo ainda em curso (work item age) | 3 dias (Issue #1 e #8) |
| Tempo de ciclo (cycle time) de 3 issues concluídas | #9: 3 dias ; #8: 2 dias ; #1: 2 dias |

**Interpretação e o que muda na próxima sprint:**
O limite de WIP de 3 itens provou ser adequado para duas pessoas, evitando a sobrecarga. No entanto, o tempo de ciclo do #9 (3 dias) revelou um gargalo: tínhamos um "ponto único de falha" (o computador do Dalton) num item crítico. Na Sprint 2, as tarefas críticas devem ser divididas em PRs menores (como foi feito no final) para permitir que o fluxo não pare caso alguém fique bloqueado.

## Contribuições e revisões

| Membro | Contribuição relevante (código, testes ou documentação) | PR revisto |
|---|---|---|
| Rodolf | Documentação (ADRs, Requisitos, DoD, Histórias), correção do CI (pythonpath e README) no PR #57, e ligação à BD (#10). | PR #57 (Dalton) e revisão do esqueleto. |
| Dalton | Esqueleto FastAPI com Tailwind e CI (#9), rascunhos das secções Equipa e Eventos. | PR #10 (Rodolf) e aprovação do PR #57 no browser. |