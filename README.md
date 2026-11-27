# Caderneta Digital do Coordenador de Turno

Projecto integrador de Engenharia de Software I (ISPTEC, 2026/2027).

- **Turma:** EIN5_M3
- **Grupo:** G??
- **Membros:** Dalton da Costa (20231175, @Dalton3C), Rodolf Gouveia (20210247, @Andadeuane221)
- **Repositório:** https://github.com/Dalton3C/caderneta-digital-do-coordenador-de-turno
- **Quadro Kanban:** https://github.com/users/Dalton3C/projects/1
- **Aplicação publicada:** (se existir)
- **Documentos:** [processo.md](processo.md) · [registo de IA](docs/ia.md) · [sprints](sprints/) · [evidencias](docs/evidencias/) 

## 1. Documentação técnica

### Requisitos
- Git
- Python 3.12 (a versão usada no CI; confirma com `python --version`)
- Node.js e npm: **só** para recompilar o CSS. O `app/static/css/app.css` já está no repositório, por isso não são precisos para executar a aplicação.

### Instalar
```bash
git clone https://github.com/Dalton3C/caderneta-digital-do-coordenador-de-turno.git
cd caderneta-digital-do-coordenador-de-turno
python -m venv .venv
source .venv/bin/activate          # Windows (PowerShell): .venv\Scripts\Activate.ps1
                                   # in case of error, execute: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
                                   #and then: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
cp .env.example .env               # Windows: copy .env.example .env
```

### Configuração (`.env`)
| Variável | Para quê | Valor por defeito |
|---|---|---|
| `DATABASE_URL` | Base de dados | `sqlite:///./caderneta.db` (ficheiro local, funciona offline) |
| `SECRET_KEY` | Assinar a sessão | Muda o valor fora do desenvolvimento |

O `.env` nunca vai para o Git.

### Executar
```bash
uvicorn app.main:app --reload
```
Abre http://127.0.0.1:8000. A rota http://127.0.0.1:8000/health devolve `{"status":"ok"}`.

### Testes e verificação de código
```bash
pytest
ruff check .
```

### Alterar os estilos (Tailwind CSS)
```bash
npm install
npm run css:dev      # recompila ao guardar
npm run css:build    # compilação final (commit do app.css)
```

### Estrutura do repositório
| Pasta ou ficheiro | Conteúdo |
|---|---|
| `app/` | Código da aplicação (FastAPI, templates, estáticos) |
| `tests/` | Testes automáticos |
| `docs/` | Decisões técnicas, registo de IA, evidências |
| `sprints/` | Registo de cada sprint |
| `processo.md` | Acordo de trabalho da equipa |

### Base de dados
```bash
alembic upgrade head        # cria as tabelas
python -m scripts.seed      # cria 3 utilizadores fictícios (admin, coordenador, professor)
```
Palavra-passe de desenvolvimento dos utilizadores fictícios: `Demo#2026`. Não usar em produção.

## 2. Manual do utilizador
(a preencher)

## 3. Relatório de testes
(a preencher)