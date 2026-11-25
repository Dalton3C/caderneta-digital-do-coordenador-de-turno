# Decisões técnicas

Cada decisão segue o formato: contexto, opções, decisão, consequências, quando reconsiderar, fontes.
Estado: **Proposta** até o grupo aprovar; **Aceite** depois da revisão do PR.

## ADR-001: Base de dados

**Estado:** Aceite · **Data:** 25/11/2026 · **Responsável:** Rodolf

### Contexto
O domínio é muito relacional (aluno, turma, ocorrência, medida) e há relatórios que cruzam dados (por exemplo, ocorrências por turma). Somos 2 pessoas, com poucos dias, e a aplicação tem de correr localmente a partir do repositório e ser demonstrável sem internet.

### Opções e comparação
| Critério | Supabase (PostgreSQL) | Firebase (Firestore) |
|---|---|---|
| Modelo de dados | Relacional (SQL, tabelas, chaves estrangeiras) | NoSQL orientado a documentos (coleções e documentos) |
| Integridade referencial (chaves estrangeiras) | **Sim** (suporte nativo a `FOREIGN KEY`) | **Não** (a integridade é gerida manualmente na aplicação) |
| Consultas de relatório (junção e agrupamento) | **Sim** (`JOIN`, `GROUP BY`, `SUM`, `COUNT` diretamente em SQL) | **Limitado** (não suporta `JOIN` nativo; agregações complexas exigem código no cliente ou agregações limitadas) |
| Relação N:N ocorrência–aluno | **Trivial** (tabela de junção com duas chaves estrangeiras) | **Complexo** (exige arrays de IDs ou subcoleções, e a junção é feita no código) |
| Integração com FastAPI | **Excelente** (SQLAlchemy 2.0 é o standard para PostgreSQL com async/await) | **Média** (SDK Python do Firebase Admin; não é relacional, pelo que o mapeamento objeto-relacional não se aplica) |
| Plano gratuito e limites | 500 MB de base de dados, 2 projetos ativos, pausa após **7 dias** de inatividade | 1 GiB de armazenamento, **50.000 leituras/dia**, 20.000 escritas/dia, sem pausa por inatividade |
| Esforço de arranque | Moderado (criar projeto, obter connection string, configurar SQLAlchemy e migrações) | Baixo (criar projeto, obter credenciais e usar SDK) |
| Funcionamento offline / local | **Sim** (pode usar SQLite localmente e alternar para PostgreSQL em produção) | **Parcial** (o emulador local existe, mas o fluxo de trabalho é menos direto e a app fica dependente do serviço para dados reais) |

### Decisão
**Supabase (PostgreSQL), acedido via SQLAlchemy 2.0 no FastAPI.**
As duas razões principais são:
1. **A natureza relacional do domínio** (aluno–turma–ocorrência–medida) e a necessidade de **relatórios agregados** (ex.: ocorrências por turma) tornam o SQL a escolha natural; o Firestore obrigaria a duplicar dados e a fazer junções manualmente no código, aumentando o risco e o esforço num prazo de 20 dias.
2. **A integração com FastAPI e SQLAlchemy** é madura e bem documentada, permitindo ainda usar **SQLite localmente** para desenvolvimento e testes offline, o que resolve o requisito de “correr localmente a partir do repositório” e mitiga o problema da pausa por inatividade do plano gratuito do Supabase.

### Consequências
- **Ganhamos:** modelo de dados normalizado, integridade referencial garantida pela base de dados, consultas de relatório expressivas e uma via clara para SQLite local (offline) e PostgreSQL em produção.
- **Aceitamos:** a dependência de um serviço externo (Supabase) para a versão online; a necessidade de configurar a *connection string* e as migrações; e o risco de o projeto gratuito ser pausado após 7 dias de inatividade. Mitigação: usar SQLite no desenvolvimento local e, na versão publicada, manter atividade mínima ou aceitar a pausa (com instruções no README para a retomar).

### Quando reconsiderar
Se o projeto evoluísse para um cenário com **milhões de utilizadores**, **dados altamente desnormalizados** ou **sincronização em tempo real** entre dispositivos, o Firestore poderia ser vantajoso. Para o âmbito atual (relacional, poucos utilizadores, foco em relatórios), o PostgreSQL é mais adequado.

### Fontes
- Supabase. *Do Supabase projects pause when they're inactive?* (consultado a 25/11/2026). https://supabase.com/docs/guides/platform/project-pausing
- Supabase. *Project Pausing* (consultado a 25/11/2026). https://supabase.com/docs/guides/platform/project-pausing
- Firebase. *Understand Cloud Firestore billing* (consultado a 25/11/2026). https://firebase.google.com/docs/firestore/pricing
- Firestore. *Joins e agregações* (consultado a 25/11/2026). https://firebase.google.com/docs/firestore/query-data/aggregation-queries
- SQLAlchemy. *FastAPI + SQLAlchemy 2.0 + PostgreSQL* (consultado a 25/11/2026). https://fastapi.tiangolo.com/tutorial/sql-databases/

## ADR-002: Frontend

**Estado:** Aceite · **Data:** 25/11/2026 · **Responsável:** Rodolf

### Contexto
A aplicação tem de ser web, responsiva, usável no computador e no telemóvel, e cumprir requisitos de **acessibilidade** (WCAG 2.2) e **usabilidade** (heurísticas de Nielsen), incluindo uso exclusivo por teclado. A equipa tem 2 pessoas e 20 dias. O backend é FastAPI.

### Opções e comparação
| Critério | Jinja2 (SSR) + Tailwind CSS | SPA (ex.: React/Vue) + Tailwind CSS |
|---|---|---|
| Nº de projetos a manter | **1** (um único projeto Python; os templates vivem no backend) | **2** (backend API + frontend separado, com build e deploy distintos) |
| Curva de aprendizagem | **Baixa** (HTML + Jinja2; a equipa já conhece Python) | **Média/alta** (React/Vue, gestão de estado, roteamento, build) |
| Acessibilidade e uso por teclado | **Mais fácil de garantir** (HTML semântico, foco nativo, navegação por teclado sem *workarounds*) | **Mais desafiante** (é preciso gerir foco, `tabindex`, ARIA e rotas do lado do cliente) |
| Deploy | **Simples** (um único serviço; ex.: Vercel suporta FastAPI) | **Complexo** (frontend e backend separados; configuração de CORS e rotas) |
| Risco em 20 dias | **Baixo** (menos peças móveis, menos contexto para trocar) | **Alto** (mais tempo gasto em infraestrutura e *glue code*, menos tempo para o domínio) |

### Decisão
**Jinja2 (renderização no servidor) + Tailwind CSS, com HTMX opcional para interatividade pontual.**
As duas razões principais são:
1. **Prazo e equipa:** com 2 pessoas e 20 dias, um único projeto Python (FastAPI + Jinja2) reduz o risco de integração e liberta tempo para o domínio e para os requisitos de acessibilidade.
2. **Acessibilidade nativa:** o HTML renderizado no servidor torna trivial garantir navegação por teclado, foco visível e estrutura semântica, ao contrário de uma SPA, onde a gestão de foco e as rotas do lado do cliente exigem mais cuidado e testes. O Tailwind CSS fornece utilitários para contraste, `focus-visible` e tamanhos de alvo de toque, alinhados com as WCAG 2.2.

### Consequências
- **Ganhamos:** um único repositório, deploy simplificado (ex.: Vercel com FastAPI), e uma base sólida para cumprir os requisitos de acessibilidade e responsividade sem complexidade acrescida.
- **Aceitamos:** menos interatividade “tipo aplicação” (mitigada com HTMX ou pequenos blocos de JavaScript); e o facto de cada navegação recarregar a página (o que é aceitável para o tipo de formulários e listagens do coordenador).

### Quando reconsiderar
Se o projeto evoluísse para **colaboração em tempo real** (ex.: edição simultânea de ocorrências) ou **interações muito ricas** (arrastar e largar, actualizações instantâneas), uma SPA ou uma arquitectura com mais JavaScript no cliente poderia ser necessária. Para o âmbito actual, o SSR é suficiente e mais seguro.

### Fontes
- FastAPI + Jinja2 (consultado a 25/11/2026). https://fastapi.tiangolo.com/advanced/templates/
- Discussão sobre acessibilidade em SPAs vs SSR (consultado a 25/11/2026). https://web.dev/articles/rendering-on-the-web
- Tailwind CSS. *Accessibility patterns* (consultado a 25/11/2026). https://tailwindcss.com/docs/accessibility

## ADR-003: Autenticação

**Estado:** Aceite · **Data:** 25/11/2026 · **Responsável:** Dalton

### Contexto
A aplicação exige **autenticação por palavra-passe** e **acesso por perfil** (cada perfil só vê e faz o que lhe é permitido). A aplicação tem de funcionar **localmente, sem internet** para demonstração, e o código deve ser **explicável na defesa**. O backend é FastAPI.

### Opções e comparação
| Critério | Autenticação própria (bcrypt + sessão por cookie assinado) | Supabase Auth |
|---|---|---|
| Funciona offline | **Sim** (tudo local; o utilizador é validado contra a base de dados local) | **Não** (depende dos servidores do Supabase para validar credenciais e emitir tokens) |
| Controlo dos perfis | **Total** (podemos definir os perfis e as permissões diretamente no modelo de dados) | **Limitado** (roles e permissões geridos pelo Supabase; menos flexível para regras específicas do domínio) |
| Esforço | **Moderado** (implementar hash com bcrypt, criar sessão e *dependency* de autorização) | **Baixo** (SDK pronto a usar; mas exige configuração de *redirects* e gestão de tokens no frontend) |
| Explicabilidade na defesa | **Alta** (todo o fluxo está no código: hash, verificação, cookie, *dependency*) | **Média** (o fluxo é abstraído pelo serviço externo; o professor pode perguntar “onde está o hash?” e a resposta é “no Supabase”) |
| Compatibilidade com deploy sem estado | **Sim** (se usarmos cookie assinado com `itsdangerous` ou JWT; a sessão pode ser *stateless*) | **Sim** (JWT emitido pelo Supabase) |

### Decisão
**Autenticação própria com `passlib[bcrypt]` para hash de palavras-passe e cookie de sessão assinado com `itsdangerous` (ou JWT), gerido por uma *dependency* de perfil no FastAPI.**
As duas razões principais são:
1. **Funcionamento offline e demonstração local:** a autenticação própria não depende de nenhum serviço externo, pelo que a aplicação corre na totalidade a partir do repositório e pode ser demonstrada sem internet, cumprindo o requisito do laboratório.
2. **Controlo e explicabilidade:** ao implementarmos o fluxo (hash, verificação, emissão do cookie, *dependency* de autorização), cada membro da equipa consegue explicar, sozinho, como a autenticação funciona — algo que o professor pode testar na defesa. Além disso, os perfis e as permissões ficam definidos no nosso modelo de dados, sem depender de configurações externas.

### Consequências
- **Ganhamos:** uma solução leve, offline e totalmente controlada, que reforça a compreensão do processo de autenticação e facilita a defesa.
- **Aceitamos:** a responsabilidade de garantir boas práticas de segurança (usar `bcrypt` com *salt*, definir `HttpOnly` e `Secure` nos cookies em produção, e proteger contra CSRF se aplicável). Como mitigações, usaremos as bibliotecas padrão (`passlib`, `itsdangerous`) e manteremos o âmbito simples (sessão por cookie assinado, sem *refresh tokens* complexos).

### Quando reconsiderar
Se o projeto crescesse para **múltiplas aplicações** ou precisasse de **login social** (Google, GitHub) e **gestão de utilizadores em escala**, o Supabase Auth (ou outro serviço gerido, como Clerk/Auth0) seria mais adequado. Para o âmbito atual (equipa pequena, foco offline e explicabilidade), a autenticação própria é a escolha mais alinhada.

### Fontes
- FastAPI. *Security – OAuth2 with Password (and hashing), Bearer with JWT tokens* (consultado a 25/11/2026). https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- Passlib. *Password hashing* (consultado a 25/11/2026). https://passlib.readthedocs.io/en/stable/
- Supabase Auth (consultado a 25/11/2026). https://supabase.com/docs/guides/auth
- Comparação entre auth gerida e auth própria (consultado a 25/11/2026). https://devnik.dev/blog/supabase-vs-custom-auth