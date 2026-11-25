# Documento de Requisitos: Caderneta Digital do Coordenador de Turno

## 1. Actores e Perfis de Utilizador
Com base nos pedidos e nos cenários do enunciado (ex.: o professor que testemunha uma ocorrência; a direcção que pede relatórios), definimos os seguintes perfis de acesso:

| Perfil | Justificação (com base no enunciado) | Permissões Principais |
|---|---|---|
| **Administrador (Direção)** | O cenário menciona que "a direcção pede ao coordenador um resumo das ocorrências". A direção precisa de visão global. | Gerir utilizadores, configurar turnos/cursos/turmas, gerar relatórios globais. |
| **Coordenador de Turno** | É o utilizador principal; o seu papel é gerir ocorrências, contactar encarregados e acompanhar medidas. | Acesso total aos módulos de alunos, ocorrências, medidas e histórico. |
| **Professor / Funcionário** | O cenário menciona que "um professor e um funcionário assistem à discussão". Eles precisam de participar como testemunhas. | Registar ocorrências (como testemunha) e consultar alunos (dados básicos). |

## 2. Requisitos Funcionais (RF)
*Prioridade: [1] Essencial (Produto Mínimo Obrigatório), [2] Importante, [3] Desejável (Sprints futuras).*

| ID | Descrição (mapeada aos pedidos do cliente) | Prioridade |
|---|---|---|
| RF01 | O sistema deve permitir a autenticação por palavra-passe e acesso restrito por perfil. | [1] |
| RF02 | O Coordenador deve poder gerir turmas e alunos. | [1] |
| RF03 | O sistema deve permitir o registo de ocorrências escolares. | [1] |
| RF04 | O sistema deve permitir associar vários alunos a uma única ocorrência. | [1] |
| RF05 | O Coordenador deve poder registar as medidas aplicadas e acompanhar o seu cumprimento. | [1] |
| RF06 | O sistema deve permitir consultar o histórico individual de ocorrências de um aluno. | [1] |
| RF07 | O sistema deve permitir registar e associar encarregados de educação aos alunos. | [2] |
| RF08 | O sistema deve permitir descrever detalhadamente os acontecimentos e registar testemunhas. | [2] |
| RF09 | O Coordenador deve poder registar contactos com encarregados de educação. | [2] |
| RF10 | O sistema deve permitir agendar reuniões de acompanhamento. | [3] |
| RF11 | O sistema deve enviar notificações e lembretes. | [3] |
| RF12 | O sistema deve gerar relatórios e indicadores (ex.: ocorrências por turma). | [3] |

## 3. Requisitos Não Funcionais (RNF)

| ID | Categoria | Descrição |
|---|---|---|
| RNF01 | Segurança | Autenticação por palavra-passe e controlo de acessos (cada perfil só vê o que lhe compete). |
| RNF02 | Privacidade | Todos os dados pessoais usados na demo/publicação devem ser fictícios (Lei n.º 22/11). |
| RNF03 | Usabilidade | A interface deve seguir as 10 heurísticas de Nielsen (ex.: mensagens de erro claras, consistência). |
| RNF04 | Acessibilidade | A interface deve cumprir as WCAG 2.2 (contraste, uso exclusivo por teclado, texto alternativo em imagens). |
| RNF05 | Responsividade | A aplicação web deve adaptar-se a ecrãs de computador e de telemóvel. |
| RNF06 | Tecnologia | Backend em Python (FastAPI), Frontend com Tailwind CSS e base de dados relacional. |

## 4. Pedidos Propostos e Rejeitados/Adiados
Para gerir o âmbito do projecto (20 dias reais), alguns pedidos do coordenador foram analisados:
*   **Propostos (MVP):** Autenticação, gestão de turmas/alunos, ocorrências (com múltiplos alunos), medidas e histórico. São os 5 módulos obrigatórios definidos na página 6 do enunciado.
*   **Adiados para Sprints futuras:** Encarregados de educação, reuniões e relatórios. O grupo vai ordená-los e desenvolvê-los se houver tempo.
*   **Simplificados/Rejeitados:** O pedido de "enviar notificações e lembretes" (ex: SMS ou e-mail externo) foi simplificado para **alertas internos no sistema** (dashboard), evitando custos com APIs de terceiros e focando no que é demonstrável localmente.

## 5. Histórias de Utilizador (Exemplos para o Sprint Backlog)
*   **US01 (RF04):** Como Coordenador de Turno, quero registar uma ocorrência associando vários alunos, para não ter de duplicar o registo quando há uma discussão em grupo.
    *   *Critérios de aceitação:* O formulário deve permitir selecionar múltiplos alunos; a ocorrência deve listar todos os alunos associados; o sistema deve guardar a data/hora e o autor.
*   **US02 (RF06):** Como Coordenador de Turno, quero consultar o histórico de um aluno, para avaliar o seu comportamento ao longo do trimestre.
    *   *Critérios de aceitação:* A página do aluno deve listar cronologicamente todas as ocorrências e medidas aplicadas.