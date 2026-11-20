# Sistema de Biblioteca: Experimento IA vs. À Mão

Repositório experimental para o seminário de **Engenharia de Software II (2026.4)**:
> **Tema 13: Produtividade com IA: Mais Código Significa Melhor Desempenho?**

O objetivo deste projeto é comparar a produtividade, densidade de defeitos, retrabalho e manutenibilidade entre o desenvolvimento de software tradicional (à mão) e assistido por Inteligência Artificial (IA).

---

## 1. Estrutura do Projeto

```text
biblioteca-ia-vs-mao/
├── src/                      # Codigo-fonte das 6 funcoes
│   ├── cadastro.py           # F1 e F2
│   ├── regras.py             # F3 e F4
│   └── consulta.py           # F5 e F6
├── test/                     # Testes unitarios automatizados (pytest)
│   ├── test_cadastro.py      # Bateria de testes para F1 e F2
│   ├── test_regras.py        # Bateria de testes para F3 e F4
│   └── test_consulta.py      # Bateria de testes para F5 e F6
├── docs/
│   ├── prompts/              # Registro obrigatorio dos prompts das funcoes com IA
│   ├── metricas.csv          # Planilha consolidada de metricas
│   └── manutencao.md         # Instrucoes da rodada de manutencao as cegas
├── PLANO_DE_IMPLEMENTACAO.md # Plano cientifico e metodologico completo
├── PROMPT_CONTEXTO_IA.md     # Prompt mestre para colar em outras IAs
├── requirements.txt          # Dependencias (pytest, radon, flake8, pylint)
└── pytest.ini                # Configuracao do pytest
```

---

## 2. Especificação Funcional das 6 Funções

Todas as implementações (feitas à mão ou com IA) devem atender estritamente aos requisitos abaixo:

### Par 1: Cadastro (Responsável: Anderson)
- **F1: `cadastrar_livro(titulo: str, autor: str, isbn: str) -> dict`**
  - Validações: `titulo` e `autor` não podem ser vazios ou conter apenas espaços (lançar `ValueError`).
  - `isbn`: aceita ISBN-10 (10 dígitos, último pode ser 'X') ou ISBN-13 (13 dígitos). Espaços e traços devem ser limpos. Se inválido, lançar `ValueError`.
  - Retorno: `{'id': int | str, 'titulo': str, 'autor': str, 'isbn': str}` normalizado.
- **F2: `cadastrar_usuario(nome: str, cpf: str, email: str) -> dict`**
  - Validações: `nome` não pode ser vazio. `cpf` com ou sem máscara deve conter 11 dígitos numéricos e não ter todos dígitos repetidos. `email` deve conter formato com `@` e domínio válido. Caso inválido, lançar `ValueError`.
  - Retorno: `{'id': int | str, 'nome': str, 'cpf': str, 'email': str}` normalizado.

### Par 2: Regras de Negócio (Responsável: Ale)
- **F3: `calcular_multa(dias_atraso: int, valor_dia: float = 2.0, teto: float = 50.0) -> float`**
  - Se `dias_atraso <= 0`, o valor é `0.0`.
  - Multa = `dias_atraso * valor_dia`. Se ultrapassar `teto`, retorna o valor do `teto`.
- **F4: `validar_emprestimo(usuario_id, livros_emprestados: int, valor_multa_pendente: float, limite_livros: int = 3) -> tuple[bool, str]`**
  - Se `valor_multa_pendente > 0.0`, retorna `(False, "Usuario possui multa pendente")`.
  - Se `livros_emprestados >= limite_livros`, retorna `(False, "Limite maximo de livros atingido")`.
  - Caso contrário, retorna `(True, "Emprestimo autorizado")`.

### Par 3: Consulta (Responsável: Edi)
- **F5: `buscar_livros(termo: str, acervo: list[dict]) -> list[dict]`**
  - `termo` de busca não pode ser vazio (lançar `ValueError`).
  - Busca parcial e *case-insensitive* nos campos `titulo` ou `autor`.
  - Retorna a lista de dicionários correspondentes.
- **F6: `listar_emprestimos_atrasados(emprestimos: list[dict], data_referencia: str) -> list[dict]`**
  - `data_referencia` deve ser validada no formato `YYYY-MM-DD` (lançar `ValueError` se formato inválido).
  - Filtra apenas empréstimos com status `'ativo'` cuja `data_prevista < data_referencia`.

---

## 3. Como Executar os Testes

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute a bateria completa de testes:
```bash
pytest
```

---

## 4. Regras de Commits e Branches

### Branches
- `fN-nome-mao` (ex: `f1-cadastrar-livro-mao`)
- `fN-nome-ia` (ex: `f2-cadastrar-usuario-ia`)
- `manut/fN-mao` ou `manut/fN-ia`

### Mensagens de Commit (Sem acento!)
- Primeiro commit: `chore(fN-modo): inicio` (liga o cronômetro)
- Funções com IA:
  - `docs(fN-ia): prompt v1` (salva o texto do prompt em `docs/prompts/`)
  - `feat(fN-ia): codigo gerado pela IA sem edicao`
  - `fix(fN-ia): correcao pedida a IA (prompt v2)` (se necessário, máximo 3 pedidos)
  - `fix(fN-ia): ajuste manual` (se você precisou alterar o código da IA)
  - `chore(fN-ia): fim` (desliga o cronômetro)
- Funções à mão:
  - `feat(fN-mao): ...`
  - `fix(fN-mao): ...`
  - `chore(fN-mao): fim`
