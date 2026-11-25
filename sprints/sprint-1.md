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
(a registar no próprio dia)

### Dia 4 (27/11)
(a registar no próprio dia)

## Revisão (27/11)

- **O que foi demonstrado:**
- **Demonstração enviada ao coordenador de turno (data e canal):**
- **Retorno recebido:** (se não houver retorno, o Product Owner representa o coordenador de turno e fica escrito aqui)
- **Itens que não cumpriram a Definição de Pronto (voltam ao Product Backlog):**

## Retrospectiva (27/11)

- **O que correu bem:**
- **O que melhorar:**
- **Acção para a Sprint 2:**
- **«Desafio a vigiar» actualizado no `processo.md`:** sim / não

## Métricas de fluxo

| Medida | Valor |
|---|---|
| Trabalho em curso (WIP), máximo atingido | |
| Débito (throughput): itens concluídos na sprint | |
| Idade do item mais antigo ainda em curso (work item age) | |
| Tempo de ciclo (cycle time) de 3 issues concluídas | #__: __ ; #__: __ ; #__: __ |

**Interpretação e o que muda na próxima sprint:**

## Contribuições e revisões

| Membro | Contribuição relevante (código, testes ou documentação) | PR revisto |
|---|---|---|
| Rodolf | | |
| Dalton | | |