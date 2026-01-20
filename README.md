# Projeto Base

Projeto Django criado para ser a base de clone para outros projetos.

## Requisitos

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes ultra-rápido)

## Instalação

```bash
# Instalar uv (se ainda não tiver)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sincronizar dependências
uv sync --all-extras

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## Comandos Úteis

### Com uv

```bash
# Adicionar nova dependência
uv add nome-do-pacote

# Adicionar dependência de desenvolvimento
uv add --dev nome-do-pacote

# Remover dependência
uv remove nome-do-pacote

# Executar comando no ambiente virtual
uv run python manage.py runserver
uv run ruff check .
```

### Ruff (Linting e Formatação)

```bash
# Verificar problemas
uv run ruff check .

# Corrigir automaticamente
uv run ruff check --fix .

# Formatar código
uv run ruff format .
```

### Django

```bash
# Rodar servidor
uv run python manage.py runserver

# Criar migrações
uv run python manage.py makemigrations

# Aplicar migrações
uv run python manage.py migrate
```

## VS Code

O projeto já está configurado para funcionar automaticamente com o VS Code:

- **Formatação automática ao salvar**: O Ruff formata e corrige problemas automaticamente
- **Lint em tempo real**: Erros e avisos aparecem enquanto você digita
- **Tasks configuradas**: Use `Ctrl+Shift+P` → "Tasks: Run Task" para:
  - Ruff: Check
  - Ruff: Fix
  - Ruff: Format
  - uv: Sync Dependencies
  - uv: Add Package
  - Django: Run Server

### Extensões Recomendadas

As extensões recomendadas estão em `.vscode/extensions.json`:
- Python
- Ruff
- Django
- autodocstring

## Estrutura do Projeto

```
curso-django/
├── .venv/              # Ambiente virtual (criado pelo uv)
├── .vscode/            # Configurações do VS Code
├── fundamentos/        # Código do curso
├── pyproject.toml      # Dependências e configuração
├── uv.lock            # Lock file do uv (versionamento exato)
└── README.md          # Este arquivo
```

## Configuração do Ruff

O Ruff está configurado em `pyproject.toml` com:
- Line length: 88 caracteres
- Regras: pycodestyle, pyflakes, isort, flake8-bugbear, flake8-django, e mais
- Exclusões automáticas: migrations, __pycache__, .venv
- Formatação automática ao salvar no VS Code
